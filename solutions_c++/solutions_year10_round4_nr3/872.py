#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int T,casenum,p,one,i,j,k,n,ans,x1,x2,y1,y2,s;
int g[2000][2000];
bool flag,l;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>n;
		memset(g,0,sizeof(g));
		s=0;
		ans=1;
		for (i=1;i<=n;i++)
		{
			cin>>x1>>y1>>x2>>y2;
			s=max(s,x2);s=max(s,y2);
			for (j=x1;j<=x2;j++)
				for (k=y1;k<=y2;k++)
					g[j][k]=1;
		}
		while (1)
		{
			flag=false;l=false;
			for (i=s+1;i>=1;i--)
				for (j=s+1;j>=1;j--)
				{
					if (g[i-1][j]==0&&g[i][j-1]==0) g[i][j]=0;
					else
					{
						if ((g[i-1][j]==1&&g[i][j-1]==1)||g[i][j]==1)
						{
							g[i][j]=1;
							flag=true;
							if (i>s||j>s) l=true;
						}
					}

				}
			if (flag)
			{
				ans++;
				if (l) s++;
			}
			else break;
		}
		cout<<ans<<endl;
	}
	return 0;
}
