#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <queue>
#include <algorithm>
#include <map>
#include <stack>
#include <vector>
#include <stdlib.h>
#include <cmath>
#include <fstream>
using namespace std;
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define INF 0x7f7f7f7f
#define INFL (1LL<<60)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas = 0;
	while(T--)
	{
		int cnt =0;
		int n,m;
		scanf("%d%d",&n,&m);
		char mat[60][60]={0};
		for(int i=0;i<n;i++)
		{
			scanf("%s",mat[i]);
			for(int j=0;j<m;j++)
				if(mat[i][j] == '#')
					cnt++;
		}
		printf("Case #%d:\n",++cas);
		if(cnt%4)
		{
			printf("Impossible\n");
			continue;
		}
		bool flag = true;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				if(mat[i][j] == '#')
				{
					int dx[3] = {0,1,1};
					int dy[3] = {1,0,1};
					char ff[4] = {'\\','\\','/'};
					mat[i][j] = '/';
					for(int k = 0;k<3;k++)
					{
						int tx = i+dx[k],ty = j+dy[k];
						if(tx<n&&ty<m&&mat[tx][ty]=='#')
						{
							mat[tx][ty]=ff[k];
						}
						else 
						{
							flag =false;
							break;
						}
					}
					if(!flag)break;
				}
				if(!flag)break;
			}
		if(!flag)
		{
			printf("Impossible\n");
			continue;
		}
		else
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<m;j++)
				{
					printf("%c",mat[i][j]);
				}
				printf("\n");
					
			}
		}
	}
    return 0;
}
