#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

const int maxn=15;
int n,m,t[maxn*10],a[maxn*10][maxn],b[maxn*10][maxn],now[maxn],ans[maxn],best;

void check()
{
	bool flag;
	for (int i=0;i<m;i++)
	{
		flag=false;
		for (int j=0;j<t[i];j++)
			if (now[a[i][j]]==b[i][j]) {flag=true;break;}
		if (!flag) return;
	}
	int temp=0;
	for (int i=1;i<=n;i++)
		if (now[i]) temp++;
	if (temp<best) {
		for (int i=1;i<=n;i++) ans[i]=now[i];
		best=temp;
	}
}

void sub(int s)
{
	if (s>n)
	{
		check();
		return;
	}
	for (int i=0;i<2;i++)
	{
		now[s]=i;
		sub(s+1);
	}
}

void solve()
{
	best=maxn;
	sub(1);
	if (best==maxn) cout<<" IMPOSSIBLE";
	else
		for (int i=1;i<=n;i++)
			printf(" %d",ans[i]);
	cout<<endl;
}

int main()
{
	int T,kase=0;
	cin>>T;
	while (T--)
	{
		cin>>n;
		cin>>m;
		for (int i=0;i<m;i++)
		{
			cin>>t[i];
			for (int j=0;j<t[i];j++)
				scanf("%d%d",&a[i][j],&b[i][j]);
		}
		cout<<"Case #"<<++kase<<":";
		solve();
	}
	return 0;
}
