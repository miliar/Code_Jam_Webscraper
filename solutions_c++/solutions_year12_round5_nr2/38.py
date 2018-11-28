#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;

int dx[6] = {1,0,-1,-1,0,1};
int dy[6] = {1,1,0,-1,-1,0};

set<pair<int,int> > seen;
map<pair<int,int>, pair<int,int> > ufpar;
map<pair<int,int>, int > ufstr; // cornerness
map<pair<int,int>, set<int> > ufstr2; // edgeness

void RESET() {
seen = set<pair<int,int> >();
ufpar = map<pair<int,int>, pair<int,int> >();
ufstr = map<pair<int,int>, int>();
ufstr2 = map<pair<int,int>, set<int> >();
}

pair<int,int> ufPar(pair<int,int> i) {
	if (ufpar.count(i)) {
		return ufpar[i] = ufPar(ufpar[i]);
	} else {
		return i;
	}
}
void ufMerge(pair<int,int> i, pair<int,int> j) {
	i = ufPar(i);
	j = ufPar(j);
	if (i == j) return;
	ufpar[j] = i;
	ufstr[i] += ufstr[j];
	for (set<int>::iterator itr = ufstr2[j].begin(); itr != ufstr2[j].end(); itr++) {
		ufstr2[i].insert(*itr);
	}
}
void insert(pair<int,int> i) {
	seen.insert(i);
	ufstr[i] = 0;
	for (int k = 0; k < 6; k++) {
		pair<int,int> j = make_pair(i.first+dx[k],i.second+dy[k]);
		if (seen.count(j)) {
			ufMerge(i,j);
		}
	}
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);

		int size, nMoves;
		scanf("%d%d",&size,&nMoves);
		size--;
		RESET();
		int curMove;
		printf("Case #%d: ",test);
		for (curMove = 1; curMove <= nMoves; curMove++) {
			int x, y;
			bool isBridge = 0, isFork = 0, isRing = 0;
			scanf("%d%d",&x,&y);

			{
				map<int, pair<int,int> > mm;
				for (int k = 0; k < 6; k++) {
					pair<int,int> t = make_pair(x+dx[k],y+dy[k]);
					if (seen.count(t)) mm[k] = ufPar(t);
				}
				for (int i = 0; i < 6; i++) {
					if (!mm.count(i)) continue;
					int j = i+1;
					while (j < 6 && mm.count(j)) {j++;}
					for (; j < 6; j++) {
						if (!mm.count(j) || mm[j] != mm[i]) continue;
						bool succ=0;
						for (int k = j+1; k < 6; k++) {succ = succ || (!mm.count(k));}
						for (int k = 0; k < i; k++) {succ = succ || (!mm.count(k));}
						if (succ) {
							isRing=1;
						}
					}
				}
			}

			insert(make_pair(x,y));
			if ((x%size==1%size) && (y%size==1%size) && (x!=size+1 || y!=size+1)) {
				ufstr[ufPar(make_pair(x,y))]++;
			} else if (x == 1) {
				ufstr2[ufPar(make_pair(x,y))].insert(0);
			} else if (y == 1) {
				ufstr2[ufPar(make_pair(x,y))].insert(1);
			} else if (x-y == size) {
				ufstr2[ufPar(make_pair(x,y))].insert(2);
			} else if (y-x == size) {
				ufstr2[ufPar(make_pair(x,y))].insert(3);
			} else if (x == size*2+1) {
				ufstr2[ufPar(make_pair(x,y))].insert(4);
			} else if (y == size*2+1) {
				ufstr2[ufPar(make_pair(x,y))].insert(5);
			}
			if (ufstr[ufPar(make_pair(x,y))] >= 2) {
				isBridge = 1;
			}
			if (ufstr2[ufPar(make_pair(x,y))].size() >= 3) {
				isFork = 1;
			}

			string s = "";
			if (isBridge) {
				if (s != "") s += "-";
				s += "bridge";
			}
			if (isFork) {
				if (s != "") s += "-";
				s += "fork";
			}
			if (isRing) {
				if (s != "") s += "-";
				s += "ring";
			}
			if (isBridge || isFork || isRing) {
				printf("%s in move %d\n",s.c_str(),curMove);
				break;
			}
			if (curMove == nMoves) {
				printf("none\n");
			}
		}
		for (curMove++; curMove <= nMoves; curMove++) {int x, y; scanf("%d%d",&x,&y);}
		
		
	}
}
