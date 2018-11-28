#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

const int maxn=1000;
int n,m,s,p,ca;
int a[maxn],f[maxn][maxn];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>ca;
	for (int l=1; l<=ca; l++)
	{
		cin>>n>>m>>p;
		for (int i=1; i<=n; i++) cin>>a[i];
		memset(f,200,sizeof(f));
		f[0][0]=0;
		for (int i=1; i<=n; i++)
			for (int j=0; j<=m; j++)
			{
				f[i][j]=max(f[i][j],f[i-1][j]);
				if ((j!=0) && (a[i]>1))
				{
					if ((a[i]+1)/3+1>=p) f[i][j]=max(f[i][j],f[i-1][j-1]+1); else f[i][j]=max(f[i][j],f[i-1][j-1]);
				}
				int tmp=a[i]/3;
				if (a[i]%3!=0) ++tmp;
                if (tmp>=p) f[i][j]=max(f[i][j],f[i-1][j]+1); else f[i][j]=max(f[i][j],f[i-1][j]);
			}
		cout<<"Case #"<<l<<": "<<f[n][m]<<endl;
	}
	
	return 0;
}
