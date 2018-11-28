#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;
const int nmax = 105;

const int x0[] = {-1,0,0,1};
const int y0[] = {0,-1,1,0};

int h[nmax][nmax];
int g[nmax][nmax][4];
int ans[nmax][nmax],was[nmax][nmax];

void rec(int x,int y,int n,int m,int mark){
	was[x][y] = 1;
	ans[x][y] = mark;

	for (int i = 0;i < 4; ++i){
		int xx = x + x0[i];
		int yy = y + y0[i];
		if (xx >= 0 && yy >= 0 && xx < n && yy < m && was[xx][yy] == 0 && g[x][y][i] == 1)
			rec(xx,yy,n,m,mark);
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int ntest;
	cin >> ntest; 
	for (int test = 1;test <= ntest; ++test){
		int n,m;
		cin >> n >> m;
		for (int i = 0;i < n; ++i)
			for (int j = 0;j < m; ++j)
				cin >> h[i][j];

		memset(g,0,sizeof(g));

		for (int i = 0;i < n; ++i)
			for (int j = 0;j < m; ++j){
				int tt = h[i][j];
				int t = -1;

				for (int k = 0;k < 4; ++k){
					int ii = i + x0[k];
					int jj = j + y0[k];
					if (ii >= 0 && jj >= 0 && ii < n && jj < m){
						if (h[i][j] > h[ii][jj] && h[ii][jj] < tt){
							tt = h[ii][jj];
							t = k;
						}
					}
				}
				if (t != -1){
					g[i][j][t] = 1;
					int ii = i + x0[t];
					int jj = j + y0[t];
					g[ii][jj][3-t] = 1;
				}
			}
		memset(ans,0,sizeof(ans));
		memset(was,0,sizeof(was));

		int mark = 0;

		for (int i = 0;i < n; ++i)
			for (int j = 0;j < m; ++j)
				if (was[i][j] == 0){
					rec(i,j,n,m,mark);
					++mark;
				}
		printf("Case #%i:\n",test);
		for (int i = 0;i < n; ++i){
			printf("%c",ans[i][0] + 'a');
			for (int j = 1;j < m; ++j) printf(" %c",ans[i][j] + 'a');
			printf("\n");
		}
				
	}
	
	return 0;
}