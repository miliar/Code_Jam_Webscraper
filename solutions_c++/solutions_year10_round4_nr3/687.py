#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;

const int maxn = 210;
bool t[maxn][maxn];

int main(){
	freopen("bacterias.in","r",stdin);
	//freopen("out.txt","r",stdout);

	int NC; cin >> NC;
	forn(nc, NC){
		int r; cin >> r;

		vector<ii> alive;
		forn(i, r){
			int x0, x1, y0, y1; cin >> x0 >> y0 >> x1 >> y1;
			forsn(h,x0,x1+1) forsn(k,y0,y1+1){
				if(!t[k][h]) { alive.pb(mp(k, h)); t[k][h] = true; }
			}
		}
		//cout << "ea " << endl;
		//forn(i, si(alive)) cout << alive[i].second << "," << alive[i].first << " "; cout << endl;


		int res = 0;
		while(!alive.empty()){
			res++;
			vector<ii> alive2;
			bool tt[maxn][maxn];
			memset(tt, false, sizeof(tt));

			//forn(i, si(alive)) cout << alive[i].second << "," << alive[i].first << " "; cout << endl;

			forn(i, si(alive)){
				ii act = alive[i];
				int y = act.first, x = act.second;
				if((t[y-1][x] || t[y][x-1]) && !tt[y][x]) { alive2.pb(mp(y, x)); tt[y][x] = true; }

				//cout << "1 "; forn(i, si(alive2)) cout << alive2[i].second << "," << alive2[i].first << " "; cout << endl;
				if(t[y+1][x-1] && !tt[y+1][x]) { alive2.pb(mp(y+1, x)); tt[y+1][x] = true; }
				if(t[y-1][x+1] && !tt[y][x+1]) { alive2.pb(mp(y, x+1)); tt[y][x+1] = true; }
			}
			alive = alive2;
			forn(i, maxn) forn(j, maxn) t[i][j] = tt[i][j];
		}

		cout << "Case #" << nc+1 << ": " << res << endl;
	}

	return 0;
}
