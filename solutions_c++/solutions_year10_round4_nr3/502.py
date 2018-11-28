#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <cmath>
#include <cctype>
using namespace std;
#define max(a,b) ((a)>(b)?(a):(b))
int nsc, sc;
int rect;
int field[200][200];
int accf[200][200];
int l, r, u,d;
#define inf 1000000000
bool dead(int move){
	for(int i=u; i<=d; i++)
		for(int j=l; j<=r;j++)
			if (field[i][j]==move) return false;
	return true;
}
void init(){
	scanf("%d", &rect);
	memset(field, 0, sizeof(field));
	l=inf,u=inf, r=-inf, d=-inf;
	for(int i=0; i<rect; i++){
		int x, y, xx, yy;
		scanf("%d %d %d %d", &y, &x, &yy, &xx);
		l=min(l, y);
		u=min(u, x);
		r=max(r, yy);
		d=max(d, xx);
		for(int j=x; j<=xx; j++)
			for(int p=y; p<=yy; p++){
				field[j][p]=1;
			}
	}
	int move=1;
	while (true){
		if (dead(move)) break;
		move++;
		for(int x=u; x<=d; x++)
			for(int y=l; y<=r; y++){
				if (field[x][y-1]==move-1 && field[x-1][y]==move-1){
					accf[x][y]=move;
				}
				else if (field[x][y-1]!=move-1 && field[x-1][y]!=move-1){
					accf[x][y]=0;
				}
				else{
					if (field[x][y]==move-1)
						accf[x][y]=move;
				}
			}
		for(int x=u; x<=d; x++)
			for(int y=l; y<=r; y++)
				field[x][y]=accf[x][y];

	}
	printf("Case #%d: %d\n", sc, move-1);
}
void solve(){
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}