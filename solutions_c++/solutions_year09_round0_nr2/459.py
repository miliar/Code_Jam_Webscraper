#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))

int r,c,vis[101][101];
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int m[101][101];
char label[101][101];
int  dfs(int rr,int cc)
{
	if (vis[rr][cc]!=-1) return vis[rr][cc];
	int ret = c * rr + cc;
	int mi = m[rr][cc];
	REP(i,4) if (rr + dx[i] >= 0 && rr + dx[i] < r && cc + dy[i] >= 0 && cc + dy[i] < c) mi <?= m[rr+dx[i]][cc+dy[i]];
	if (mi < m[rr][cc]) 
	REP(i,4) if (rr + dx[i] >= 0 && rr + dx[i] < r && cc + dy[i] >= 0 && cc + dy[i] < c && m[rr+dx[i]][cc+dy[i]]==mi)
	{
	 ret = dfs(rr+dx[i],cc+dy[i]);
	 break;
	}
	return vis[rr][cc] = ret;
}

int main()
{
	int t;
	int basin[30];
	int ff[10000];
	int f[10000];
	scanf("%d",&t);
	REP(T,t)
	{
		_m(ff,0);
		_m(f,-1);
		_m(vis,-1);
		scanf("%d %d" ,&r,&c);
		REP(i,r) REP(j,c) scanf("%d",&m[i][j]);
		while (1)
		{
			int ma = -1;
			REP(i,r) REP(j,c) if (vis[i][j]==-1) ma >?= m[i][j];
			REP(i,r) REP(j,c) if (vis[i][j]==-1 && m[i][j]==ma) vis[i][j] = dfs(i,j);
			if (ma==-1) break;
		}
		int idx = 0;
		REP(i,r) REP(j,c) if (f[vis[i][j]] == -1) f[vis[i][j]]=idx++;
		REP(i,r*c) if (f[i]!=-1) 
		{
			REP(j,r) REP(k,c) if (vis[j][k]==i) label[j][k] = f[i]+'a';
		}
		printf("Case #%d:\n",T+1);
		REP(i,r) 
		{
			REP(j,c)
			{
				 printf("%c ",label[i][j]);
				 if (j < c-1) printf( " ");
			}
			puts("");
		}
	}
	return 0;	
}
