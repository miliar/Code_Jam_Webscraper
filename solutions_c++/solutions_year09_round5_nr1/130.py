#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define debug(x) cout << '>' << #x << ':' << x << '\n';
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define mp make_pair
#define inf 2123123123
#define pb push_back
#define reset(Z,Y) memset(Z,Y,sizeof(Z))

#define eps 1e-11
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

#define A first
#define B second

typedef long long ll;
typedef long double ld;

using namespace std;

int n;

map< pair<int, pair<int,int> >, int > m;

vector< pair<int,int> > box;

vector< pair<int,int> > wanted;

int isanswer(void) {
	if (wanted == box) return 1;
	return 0;
	}

int isdanger(void) {
	int reach[6];
	reset(reach,0);
	reach[0] = 1;
	forn(i,n) forn(j,n) if (reach[j]) forn(k,n) if (abs(box[j].B - box[k].B) + abs(box[j].A - box[k].A) == 1) reach[k] = 1;
	forn(i,n) if (!reach[i]) return 1;
	return 0;
	}

void dehash(int val,int x,int y) {
	box[0] = mp(x,y);
	forn(i,n - 1) {
		int w = val % 12;
		val /= 12;
		int v = val % 12;
		val /= 12;
		box[i + 1] = mp(v,w);
		}
	sort(all(box));
	}

int hash(void) {
	
	int ret = 0;
	for (int i = n - 1;i >= 1;i--) {
		ret *= 12;
		ret += box[i].A;
		ret *= 12;
		ret += box[i].B;
		}
	return ret;
	}
	
	
queue< pair<int, pair<int,int> > > q;


void insert(int val) {
	
	
	int gg = hash();
	pair<int, pair<int,int> > pip = mp(gg, mp(box[0].A,box[0].B));
	if (m.find(pip) != m.end()) return;
	/*debug(val);
			forn(i,n) {
				printf("%d %d\n",box[i].A,box[i].B);
				}
*/
	q.push(pip);
	m[pip] = val;
	}

int r,col;



int main() {
	int z;
	scanf("%d",&z);
	forn(zz,z) {
		scanf("%d%d",&r,&col);
		vector<string> peta;
		char dumi[100];
		forn(i,r) {
			scanf("%s",dumi);
			peta.pb(dumi);
			}
		box.clear();
		wanted.clear();
		forn(i,r) forn(j,col) {
			if (peta[i][j] == 'x' || peta[i][j] == 'w') wanted.pb(mp(i,j));
			if (peta[i][j] == 'o' || peta[i][j] == 'w') box.pb(mp(i,j));
			}
		sort(all(wanted));
		n = sz(box);
		/*forn(i,n) {
				printf("%d %d\n",box[i].A,box[i].B);
				}*/
		m.clear();
		while (!q.empty()) q.pop();
		insert(0);
		int found = 0;
		int ret = 0;
		while (!q.empty()) {
			int a=q.front().A,b=q.front().B.A,c=q.front().B.B;
			q.pop();
			int d = m[mp(a,mp(b,c))];
			dehash(a,b,c);
		/*	printf("dari sini\n");
			debug(d);
			forn(i,n) {
				printf("%d %d\n",box[i].A,box[i].B);
				}*/
			if (isanswer()) {
				found = 1;
				ret =d;
				break;
				}
			//is danger?
			int bahaya = isdanger();
			forn(i,n) {
				if (box[i].A != 0) {
					if (box[i].A != r - 1) {
						int yes = 1;
						forn(j,n) if (j != i) if (box[j].B == box[i].B) if (abs(box[j].A - box[i].A) == 1) {
							yes = 0;
							break;
							}
						if (!yes) continue;
						if (peta[box[i].A - 1][box[i].B] == '#') continue;
						if (peta[box[i].A + 1][box[i].B] == '#') continue;
						box[i].A += 1;
						if (!(bahaya && isdanger())) insert(d+1);
						box[i].A -= 2;
						if (!(bahaya && isdanger())) insert(d+1);
						box[i].A += 1;
						}
					}
				}
			
			forn(i,n) {
				if (box[i].B != 0) {
					if (box[i].B != col - 1) {
						int yes = 1;
						forn(j,n) if (j != i) if (box[j].A == box[i].A) if (abs(box[j].B - box[i].B) == 1) {
							yes = 0;
							break;
							}
						if (!yes) continue;
						if (peta[box[i].A][box[i].B+1] == '#') continue;
						if (peta[box[i].A][box[i].B-1] == '#') continue;
						box[i].B += 1;
						if (!(bahaya && isdanger())) insert(d+1);
						box[i].B -= 2;
						if (!(bahaya && isdanger())) insert(d+1);
						box[i].B += 1;
						}
					}
				}
			}
		if (!found) ret = -1;
		printf("Case #%d: %d\n",zz + 1,ret);
		}
	
	return 0;
	}



