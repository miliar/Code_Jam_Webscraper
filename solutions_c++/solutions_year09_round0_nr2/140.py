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
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cout<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
int H[110][110];
int L[110][110];
char Lc[110][110];
int W,HS;
int dx[]={-1,0,0, 1};
int dy[]={ 0,-1,1,0};
bool sink(int a,int b)
{
	bool ok=true;
	REP(i,4)
	{
		int nx=a+dx[i];;
		int ny=b+dy[i];
		if (nx<0||ny<0||nx>=HS||ny>=W)
			continue;
		if (H[nx][ny]<H[a][b])
		{
			return false;
		}
	}
	return true;
}
int dfs(int x,int y)
{
//	DEB(x);
//	DEB(y);
	if (L[x][y]!=-1)
		return L[x][y];
	int hm=INF;
	int px,py;
	
	REP(i,4)
	{
		int nx=x+dx[i];;
		int ny=y+dy[i];
		if (nx<0||ny<0||nx>=HS||ny>=W)
			continue;
		if (hm>H[nx][ny])
		{
			hm=H[nx][ny];
			px=nx;
			py=ny;
		}
	}
//	DEB(hm);
	int l=dfs(px,py);
	L[x][y]=l;
	return L[x][y];
}


int dfs2(int x,int y,char p)
{
//	DEB(x);
//	DEB(y);
	Lc[x][y]=p;
	REP(i,4)
	{
		int nx=x+dx[i];;
		int ny=y+dy[i];
		if (nx<0||ny<0||nx>=HS||ny>=W)
			continue;
		if (L[x][y]==L[nx][ny]&&Lc[nx][ny]==0)
		{
			Lc[nx][ny]=p;
			dfs2(nx,ny,p);
		}
	}
//	DEB(hm);
	
	return 0;
}



int main ()
{
//	int p=1000;
//	printf ("%d %d\n",100,100);
//	REP(i,100)
//	{REP(j,100)
//		printf ("%d ",i+j);
//		printf ("\n");
//	}
//	return 0;
	int c;
	scanf ("%d",&c);

	FOR(cas,1,c)
	{
		memset(L,-1,sizeof L);
		memset(Lc,0,sizeof Lc);
		scanf ("%d%d",&HS,&W);
		REP(i,HS)REP(j,W)
		{
			scanf ("%d",&H[i][j]);
		}
		int cont=0;
		REP(i,HS)REP(j,W)
			if (sink(i,j))
				L[i][j]=cont++;
		REP(i,HS)REP(j,W)
		{
			if (L[i][j]==-1)
				L[i][j]=dfs(i,j);
		}
		char cl='a';
		REP(i,HS)REP(j,W)
		{
			if(Lc[i][j]==0)
			{
				Lc[i][j]=cl;
				dfs2(i,j,cl);
				cl++;
			}
		}
		
		printf ("Case #%d:\n",cas);
		REP(i,HS)
		{
			REP(j,W)
			{
				if (j==W-1)
				printf ("%c\n",Lc[i][j]);
				else
				printf ("%c ",Lc[i][j]);
			}
		}
	}
	return 0;
}

