#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
bool f[100][100];
const int p=1000000007;
int n,b,Test,t,ans,a[100];

void trans(int k)
{
	a[0]=0;
	while (k>0)
	{
		a[++a[0]]=k%b;
		k/=b;
	}
}

void dfs(int last,int now)
{
	if (now==0) ans++;
	for (int i=last;i<=now;i++)
	{
		trans(i);
		bool ok=true;
		for (int j=1;j<=a[0];j++)
			if (f[j][a[j]]) { ok=false; break; }
		if (ok)
		{
			for (int j=1;j<=a[0];j++)
				f[j][a[j]]=true;
			dfs(i+1,now-i);
			trans(i);
			for (int j=1;j<=a[0];j++)
				f[j][a[j]]=false;
		}
	}
}

void work()
{
	cin>>n>>b;
	ans=0;
	memset(f,0,sizeof(f));
	dfs(1,n);
	cout<<"Case #"<<t<<": "<<ans<<endl;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d.out","w",stdout);
	cin>>Test;
	for (t=1;t<=Test;t++) work();
	fclose(stdin);	fclose(stdout);
	return 0;
}