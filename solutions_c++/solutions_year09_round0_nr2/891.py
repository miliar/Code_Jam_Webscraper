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


#define debug(x) cout << '>' << #x << ':' << x << '\n';
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define inf 2123123123
#define eps 0.0000001
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)
#define mp make_pair
#define I(M) (typeof((M).begin()))
#define pb push_back

typedef long long ll;
typedef long double ld;

using namespace std;

int main() {
	int arahx[4] = {0,-1,1,0};
	int arahy[4] = {-1,0,0,1};
	int n;
	scanf("%d",&n);
	int basin[105][105];
	int sampe[2][105][105];
	int susu[105][105];
	char label[105][105];
	forn(i,n) {
		printf("Case #%d:\n",i + 1);
		forn(j,105) forn(k,105) basin[j][k] = inf,susu[j][k] = 0,label[j][k] = '1';
		int row,col;
		scanf("%d%d",&row,&col);
		forn(j,row) forn(k,col) scanf("%d",&basin[k + 1][j + 1]);
		
		vector< pair<int, pair<int,int> > > vp;
		forn(j,row) forn(k,col) vp.pb(mp(basin[k + 1][j + 1],mp(k + 1,j + 1)));
		sort(all(vp));
		
		forn(j,sz(vp)) {
			int x = vp[j].second.first;
			int y = vp[j].second.second;
			int alt = vp[j].first;
			int lowest = inf;
			forn(k,4) {
				lowest = min(lowest,basin[x + arahx[k]][y + arahy[k]]);
				}
			if (lowest >= alt) {
				sampe[0][x][y] = x;sampe[1][x][y] = y;
				susu[x][y] = 1;
				//debug(x);
				//debug(y);
				continue;
				}
			forn(k,4) {
				int dx = x + arahx[k];
				int dy = y + arahy[k];
				if (basin[dx][dy] > lowest) continue;
				//printf("%d %d : %d %d\n",x,y,dx,dy);
				//debug(dx);
				//debug(dy);
				sampe[0][x][y] = sampe[0][dx][dy];
				sampe[1][x][y] = sampe[1][dx][dy];
				break;
				}
			}
		char he = 'a';
		
		
		forn(j,row) {forn(k,col) {
			if (k != 0) printf(" ");
			int xx = sampe[0][k + 1][j + 1];
			int yy = sampe[1][k + 1][j + 1];
			if (label[xx][yy] == '1') {
				label[xx][yy] = he;
				he++;
				}
			printf("%c",label[xx][yy]);
			}
			printf("\n");
			}
		}
		
		
		
	
	return 0;
	}

