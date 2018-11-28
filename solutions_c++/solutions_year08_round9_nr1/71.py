#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

const int nMax = 5005;
const int INF = 10000;

pair<int,pair<int,int> > tab[nMax];

void testcase(int tNum) {

	printf("Case #%d: ",tNum);	
	
	int N;
	scanf("%d",&N);
	FOR(i,0,N) scanf("%d %d %d",&tab[i].FI,&tab[i].SE.FI,&tab[i].SE.SE);
	sort(tab, tab+N);
	int res = 0;
	FOR(nA,0,N) {
		multiset<pair<int,int> > B;
		FOR(i,0,nA+1) B.insert(tab[i].SE);
		multiset<int> C;
		multiset<int>::iterator itC=C.end();
		int acc = 0;
		FORE(it,B) {
			C.insert(it->SE);
			int left = INF - tab[nA].FI - it->FI;
			if(it->SE <= left) {
				acc++;
				if(it->SE > *itC) itC++;
			}
			if(itC==C.end()) {
				if(C.size()==1)
					itC = C.begin(); else
					break;
			}
			//printf("a=%d b=%d left=%d acc=%d c=%d\n",tab[nA].FI,it->FI,left,acc,*itC);
			//FORE(it2,C) printf("%d ",*it2);
			//printf("\n");
			while((*itC)>left && itC!=C.begin()) { itC--; acc--; }
			if((*itC)>left && itC==C.begin()) break;
			res = max(res, acc);
		}
	}
	printf("%d\n",res);
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
