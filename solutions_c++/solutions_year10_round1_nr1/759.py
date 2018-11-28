#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<set>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstdlib>
#include<deque>
#include<list>
#include<stack>
using namespace std;

#define INF 0x7fffffff
typedef long long LL;

int main()
{
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.in","r",stdin);
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.out","w",stdout);

	int csNum,cs;
	int n,k,i,j,l,t,d,ans;
	char mp[105][105],lmp[105][105],rmp[105][105];
	scanf("%d",&csNum);
	for(cs=1;cs<=csNum;cs++)
	{
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)
			scanf("%s",mp[i]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				lmp[n-j-1][i]=mp[i][j];
				rmp[j][n-i-1]=mp[i][j];
			}
		for(i=0;i<n;i++)
		{
			t=n-1;
			for(j=n-1;j>=0;j--)
			{
				if(lmp[j][i]!='.')
				{
					if(j!=t)
					{
						lmp[t][i]=lmp[j][i];
						lmp[j][i]='.';
					}
					t--;
				}
			}
		}
		for(i=0;i<n;i++)
		{
			t=n-1;
			for(j=n-1;j>=0;j--)
			{
				if(rmp[j][i]!='.')
				{
					if(j!=t)
					{
						rmp[t][i]=rmp[j][i];
						rmp[j][i]='.';
					}
					t--;
				}
			}
		}
		bool fr=0,fb=0;
		int x,y,dir[4][2]={{0,1},{1,0},{1,1},{1,-1}};
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				for(d=0;d<4;d++)
				{
					/*for(l=0;l<k;l++)
					{
						x=i+dir[d][0]*l;
						y=j+dir[d][1]*l;
						if(x<0||x>=n||y<0||y>=n||lmp[x][y]!='R')
							break;
					}
					if(l==k)
						fr=1;*/
					for(l=0;l<k;l++)
					{
						x=i+dir[d][0]*l;
						y=j+dir[d][1]*l;
						if(x<0||x>=n||y<0||y>=n||rmp[x][y]!='R')
							break;
					}
					if(l==k)
						fr=1;
					/*for(l=0;l<k;l++)
					{
						x=i+dir[d][0]*l;
						y=j+dir[d][1]*l;
						if(x<0||x>=n||y<0||y>=n||lmp[x][y]!='B')
							break;
					}
					if(l==k)
						fb=1;*/
					for(l=0;l<k;l++)
					{
						x=i+dir[d][0]*l;
						y=j+dir[d][1]*l;
						if(x<0||x>=n||y<0||y>=n||rmp[x][y]!='B')
							break;
					}
					if(l==k)
						fb=1;
				}
			}
		printf("Case #%d: ",cs);
		if(!fr&&!fb)
			printf("Neither\n");
		else if(fr&&!fb)
			printf("Red\n");
		else if(!fr&&fb)
			printf("Blue\n");
		else if(fr&&fb)
			printf("Both\n");
	}
}