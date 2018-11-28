
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <complex>

using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>

int cond = (ll)1;
#define db(x) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }

char tab[10][10];

void solve() {
	rep (i, 4)
		rep (j, 4) scanf(" %c", &tab[i][j]);

	bool dot = false;
	rep (i, 4) rep(j, 4) dot |= tab[i][j] == '.';
	
	int dx[4] = { 0, 1, 1, -1};
	int dy[4] = { 1, 1, 0, 1};

	rep (i, 4) rep (j, 4) {
		rep (d, 4) {
			bool ok = true;
			string str = "";
			rep (dd, 4) {
				int ddx = i + dx[d] * dd;
				int ddy = j + dy[d] * dd;
				if (ddx >= 0 && ddx < 4 && ddy >= 0 && ddy < 4) {
					str += tab[ddx][ddy];
				}
				else ok = false;
			}
			if (ok) {
				//cerr << str << endl;
				int x = 0, o = 0, t = 0;
				rep (dd, 4) if (str[dd] == 'X') x++;
				else if (str[dd] == 'O') o++;
				else if (str[dd] == 'T') t++;
				//cout << x <<" " << o << " " << t << " " << str << endl;

				if (x == 4 || x == 3 && t == 1) {
					printf("X won");
					return;
				}
				else if (o == 4 || o == 3 && t == 1) {
					printf("O won");
					return;
				}

			}
		}
	}

	// Grocka 16/11
	if (dot) printf("Game has not completed");
	else printf("Draw");
}

int main(int argc, char ** argv) {
	//  freopen("../1.in","r",stdin); 
	//  freopen("../2.in","r",stdin); 
	//  freopen("../3.in","r",stdin); 
	//  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
	//  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
	//  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
	//  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
	//  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout)

	cond = argc >= 2 && argv[1][0] == 'q' ? 1 << 30 : 0;
	int t;
	scanf("%d", &t);
	fo (i, 1, t) {
		//cerr << __LINE__ << " " << i << endl;
		printf("Case #%d: ", i);
		solve();
		printf("\n");
		fflush(stdout);
		cerr.flush();
	}
	return 0;
}


