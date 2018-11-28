#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

map <string,int> hash;
int num,n,m,a[105],b[1005],f[1005][105],ans;

void solve()
{
	memset(f,0,sizeof(f));
	ans=1005;
	int jj;
	b[0]=-1;
	for (int i=1;i<=n;i++)
	{
		for (int j=0;j<m;j++)
			if (b[i]==a[j]) {jj=j;break;}
		for (int k=0;k<m;k++)
		{
			f[i][k]=f[i-1][k];
			for (int j=0;j<m;j++)
				if (f[i-1][j]+1<f[i][k]) f[i][k]=f[i-1][j]+1;
			if (k==jj) f[i][k]=1005;
		}
	}
	for (int i=0;i<m;i++)
		if (f[n][i]<ans) ans=f[n][i];

	/*
	for (int i=0;i<=n;i++){
		for (int j=0;j<m;j++)
			cout<<f[i][j]<<" ";
		cout<<endl;
	}
	*/
}

int main()
{
	int T,kase=0;
	char s[200];
	cin>>T;
	while (T--)
	{
		cin>>m;
		hash.clear();
		gets(s);
		num=0;
		for (int i=0;i<m;i++)
		{
			gets(s);
			hash[s]=++num;
			a[i]=num;
		}
		cin>>n;
		gets(s);
		for (int i=1;i<=n;i++)
		{
			gets(s);
			b[i]=hash[s];
		}
		solve();
		cout<<"Case #"<<++kase<<": "<<ans<<endl;
	}
	return 0;
}
