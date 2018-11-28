#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;
int T,casenum,n,k,i,j,l,K;
string s;
const int dx[4]={1,1,0,-1};
const int dy[4]={0,1,1,1};
char g[100][100];
char f[100][100];
int len[100];
bool flag[4];
bool red,blue;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>n>>K;
		getline(cin,s);
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n;j++)
				scanf("%c",&g[i][j]);
			getline(cin,s);
		}
		memset(f,0,sizeof(f));
		for (i=1;i<=n;i++)
		{
			len[i]=0;
			for (j=n;j>=1;j--)
				if (g[i][j]!='.')
				{
					len[i]++;
					f[i][len[i]]=g[i][j];
				}
		}
		blue=red=false;
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
			{
				for (k=0;k<4;k++)
					flag[k]=true;
				for (k=0;k<4;k++)
					for (l=1;l<K;l++)
					{
						if (i+l*dx[k]<1||i+l*dx[k]>n||j+l*dy[k]<1||j+l*dy[k]>n)
						{
							flag[k]=false;
							continue;
						}
						if (f[i+l*dx[k]][j+l*dy[k]]!=f[i][j]) flag[k]=false;
					}
				if (flag[0]||flag[1]||flag[2]||flag[3])
				{
					if (f[i][j]=='B') blue=true;
					if (f[i][j]=='R') red=true;
				}
			}
		if (blue&&red) cout<<"Both";
		else
		{
			if (blue) cout<<"Blue";
			else
			{
				if (red) cout<<"Red";
				else cout<<"Neither";
			}
		}
		cout<<endl;
	}
	return 0;
}
