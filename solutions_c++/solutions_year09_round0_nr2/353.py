#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   clr(a)      memset((a),0,sizeof (a));
#define   mabs(a)     ((a)>0?(a):(-(a))) 
#define   inf         1000000000
#define  MAXM     (1<<7)  
#define  MAXN     101
#define  eps      1e-6
#define  MOD      50261
typedef __int64 int64;
FILE *fin;
FILE *fout;
int H,W;
int G[MAXN][MAXN];
bool visited[MAXN][MAXN];
int flag[MAXN][MAXN];
// North, West, East, South.
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
bool inbound(int x,int y)
{
	return x>=0&&x<H&&y>=0&&y<W;
}
int dfs(int x,int y)
{
	int i;
	int mini=-1,int minf=G[x][y];
	REP(i,4)
	{
        int nx=x+dx[i];
		int ny=y+dy[i];
		if(!inbound(nx,ny)) continue;
	    if(G[nx][ny]<minf) 
		{
			minf=G[nx][ny];
			mini=i;
		}
	}
	if(mini==-1)
	{
        visited[x][y]=true;
		return flag[x][y]=x*100+y;
	}
	else
	{
		int nx=x+dx[mini],ny=y+dy[mini];
		if(!visited[nx][ny])
		{
	       visited[nx][ny]=true;
		   flag[nx][ny]=dfs(nx,ny);
		}
		return flag[nx][ny];
	}
}
map<int,int> mii;
int main()
{
   	fin=fopen("B-large.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int N;
	fscanf(fin,"%d",&N);
    int rounds;
	for (rounds=1;rounds<=N;rounds++)
	{
		fscanf(fin,"%d%d",&H,&W);
		REP(i,H) REP(j,W) fscanf(fin,"%d",&G[i][j]); 
		clr(visited);
		REP(i,MAXN) REP(j,MAXN) flag[i][j]=-1;
		REP(i,H) REP(j,W) 
		{
			if (!visited[i][j])
			{
                 visited[i][j]=true;
				 flag[i][j]=dfs(i,j);
			}
		}
        mii.clear();
		int cnt='a';
		REP(i,H) REP(j,W)
		{
			if(mii.find(flag[i][j])==mii.end())
			{
                mii[flag[i][j]]=cnt++;
			}
		}
		REP(i,H) REP(j,W)
		{
			flag[i][j]=mii[flag[i][j]];
		}
	    printf("Case #%d:\n",rounds);
        fprintf(fout,"Case #%d:\n",rounds);
		REP(i,H)
		{
			REP(j,W-1)
			{
				printf("%c ",(char)flag[i][j]);
				fprintf(fout,"%c ",(char)flag[i][j]);
			}
			printf("%c\n",(char)flag[i][j]);
			fprintf(fout,"%c\n",(char)flag[i][j]);
		}
	}
}
