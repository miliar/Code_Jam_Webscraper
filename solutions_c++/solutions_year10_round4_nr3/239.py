#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:16777216")
using namespace std;

#define bit(n) (1<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;

#define N 111

int main()
{
	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);
	int TST,tst=0;
	for(scanf("%d",&TST);TST--;)
	{
		printf("Case #%d: ",++tst);fprintf(stderr,"%d\n",tst);
		int m,i,j,k;
		int a[N][N]={0};
		for(scanf("%d",&m);m--;)
		{
			int x1,y1,x2,y2,x,y;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(x=x1;x<=x2;x++)
				for(y=y1;y<=y2;y++)
					a[x][y]=1;
		}
		for(k=0;;k++)
		{
			bool die=true;
			int b[N][N]={0};
			for(i=1;i<N;i++)
				for(j=1;j<N;j++)
					if(a[i][j]==1)
					{
						die=false;
						if(a[i-1][j]==0 && a[i][j-1]==0) b[i][j]=0; else b[i][j]=1;
					}
					else
					{
						if(a[i-1][j]==1 && a[i][j-1]==1) b[i][j]=1; else b[i][j]=0;
					}
			if(die) break;
			for(i=1;i<N;i++)
				for(j=1;j<N;j++)
					if(a[i][j]=b[i][j]) die=false;
		}
		printf("%d\n",k);
	}
	return 0;
}
