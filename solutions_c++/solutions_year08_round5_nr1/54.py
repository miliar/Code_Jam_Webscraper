// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 
int tab[230][230][4];
char bufor[200];
int r;
int mamy;
int ruch[4][2] = { {0,1},{1,0},{0,-1},{-1,0}};
int main() {
int ile;
scanf("%d",&ile);
FOR(iile,1,ile) {


	int px = 105;
	int py = 105;
	int kier = 0;
	REP(x,210) REP(y,210) REP(z,4) tab[x][y][z] = 0;
int n;
	mamy = 0;
	LL pole = 0;
	scanf("%d",&n);
	REP(i,n) {
		scanf("%s%d",bufor,&r);
		REP(j,r) {
			int k = strlen(bufor);
			REP(z,k) {
				if (bufor[z] == 'R') kier++;
				if (bufor[z] == 'L') kier--;
				kier+=4;
				kier %=4;
				if (bufor[z] == 'F') {
					int dx = px + ruch[kier][0];
					int dy = py + ruch[kier][1];
					if (kier == 0) {
						tab[px][py][1] = 1;
					}
					if (kier == 1) {
						tab[px][py][0] = 1;
						pole += dy;
					}
					if (kier == 2) {
						tab[dx][dy][1] = 1;
					}
					if (kier == 3) {
						pole -= dy;
						tab[dx][dy][0] = 1;
					}
					px = dx;
					py = dy;
				}
			}
		}
		
	}
	REP(x,210) REP(y,210) {
		bool jest[4];
		REP(i,4) jest[i] = false;
		{
			px = x;
			py = y+1;
			while (py<=210) {
				if (tab[px][py][0]) { jest[0] = true; break; }
				py++;
			}
		}
		{
			 px = x;
			 py = y;
			while (py>=0) {
				if (tab[px][py][0]) { jest[1] = true; break; }
				py--;
			}
		}
		{
			 px = x+1;
			 py = y;
			while (px<=210) {
				if (tab[px][py][1]) { jest[2] = true; break; }
				px++;
			}
		}
		{
			 px = x;
			 py = y;
			while (px>=0) {
				if (tab[px][py][1]) { jest[3] = true; break; }
				px--;
			}
		}
		if ((jest[0]&&jest[1]) || (jest[2]&&jest[3])) mamy++;

	}

	if (pole < 0) pole = -pole;
	mamy -= pole;
printf("Case #%d: %d\n",iile,mamy);
}
return 0;
}

