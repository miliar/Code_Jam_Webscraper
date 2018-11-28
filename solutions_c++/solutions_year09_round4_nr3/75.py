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
#define inf 2123123123LL
#define eps 0.0000001
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)
#define mp make_pair
#define I(M) (typeof((M).begin()))
#define pb push_back

#define pipii pair< int, pair<int, pair<int, pair<int,int> > > >

typedef long long ll;
typedef long double ld;

using namespace std;

int hub[150][150]; //hub[a][b] is true if b can be located BELOW a
int dist[150][150];
int nilai[150][150];
int con[150][150];
int n,m;
int best[150];
int sudah[150];

int ret;

int depth;

int masuk[150];

void find(int pos,int jml) {
	depth++;
	if (depth >= 10000000) return;
	if (pos >= n) {ret = max(ret,jml); return;}
	if (n + 1 - pos + jml <= ret) return;
	//try to put pos into the group!
	int valid = 1;
	forn(i,n) {
		if (masuk[i]) 
			if (con[pos][i]) {
				valid = 0;
				break;
				}
			}
	if (valid) {
		masuk[pos] = 1;
		find(pos + 1,jml + 1);
		masuk[pos] = 0;
		}
	find(pos + 1,jml);
	}

int main() {
	
	int zz;
	scanf("%d",&zz);
	forn(z,zz) {
		printf("Case #%d: ",z + 1);
		scanf("%d%d",&n,&m);
		forn(i,n) forn(j,m) scanf("%d",&nilai[i][j]);
		forn(i,150) forn(j,150) hub[i][j] = 0;
		depth = 0;
		forn(i,n) forn(j,n) if (i != j) {
			//test if i can be located below j
			int bisa = 1;
			forn(k,m) if (nilai[i][k] >= nilai[j][k]) bisa = 0;
			if (bisa) hub[j][i] = 1;
			}
		
		//generate the graph
		//a starting node : n, connects to every node with length 1.
		forn(i,n) hub[n][i] = 1;
		
		//find the longest distance between each node
		
		forn(i,n + 1) {
			memset(best,-1,sizeof(best));
			memset(sudah,0,sizeof(sudah));
			best[i] = 0;
			queue<int> q;
			q.push(i);
			while (!q.empty()) {
				int a = q.front();
				q.pop();
				forn(j,n) {
					if (hub[a][j] == 0) continue;
					if (best[j] >= best[a] + hub[a][j]) continue;
					best[j] = best[a] + hub[a][j];
					q.push(j);
					}
				}
			forn(j,n + 1) dist[i][j] = best[j];
			}
		
		memset(con,0,sizeof(con));
		
		vector<int> hahaha;
		
		forn(i,n) hahaha.pb(i);
		random_shuffle(all(hahaha));
		
		
		
		forn(i,n) forn(j,n) if (dist[hahaha[i]][hahaha[j]] > 0 && i != j) con[i][j] = 1;
		forn(i,n) forn(j,n) if (con[i][j] == 1) con[j][i] = 1;
		ret = 0;
		
		//forn(i,n) forn(j,n) printf("%d %d %d\n",i,j,con[i][j]);
		
		//find the number of charts needed!
		find(0,0);
		printf("%d\n",ret);
		}
		
		
	
	}

