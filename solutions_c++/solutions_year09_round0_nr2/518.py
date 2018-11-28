#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

int n, m, a[200][200];
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
char cur;
char c[200][200];

bool isgood(int x, int y){
	return x>=0 && y>=0 && x<n && y<m;
}

char dfs(int x, int y){
	if (c[x][y])
		return c[x][y];
	int ma = 1000000000;
	int dir = -1;
	REP(i,4){
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (isgood(nx, ny) && a[nx][ny] < ma){
			ma = a[nx][ny];
			dir = i;
		}
	}
	if (ma < a[x][y]){
		int nx = x + dx[dir];
		int ny = y + dy[dir];
		c[x][y] = dfs(nx, ny);
		return c[x][y];
	}
	else{
		c[x][y] = cur++;
		return c[x][y];
	}
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		FILL(c);
		cur = 'a';
		printf("Case #%d:\n", it+1);
		scanf("%d%d", &n, &m);
		REP(i,n)
			REP(j,m)
				scanf("%d", &a[i][j]);
		REP(i,n){
			REP(j,m)
				printf("%c ", dfs(i,j));
			puts("");
		}
	}
}
