#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int test,t,n,m;
bool a[109][109],b[109][109];

void init()
{
	int r;
	n=0;	m=0;
	cin>>r;
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	for (int i=1;i<=r;i++)
	{
		int X1,Y1,X2,Y2;
		cin>>X1>>Y1>>X2>>Y2;
		n=max(n,X2);	m=max(m,Y2);
		for (int xx=X1;xx<=X2;xx++)
			for (int yy=Y1;yy<=Y2;yy++)
				a[xx][yy]=1;
	}
}

bool ok()
{
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
			if (a[i][j]) return false;
	return true;
}

int work()
{
	int ans=0;
	while(true)
	{
		if (ok()) return ans;
		ans++;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				if(a[i][j])
				{
					if ((!a[i-1][j]) && (!a[i][j-1])) b[i][j]=0; else b[i][j]=1;
				}
				else if (a[i-1][j] && a[i][j-1]) b[i][j]=1; else b[i][j]=0;
		memcpy(a,b,sizeof(a));
	}
	return ans;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>test;
	for (t=1;t<=test;t++)
	{
		init();
		cout<<"Case #"<<t<<": "<<work()<<endl;
	}
	fclose(stdin);	fclose(stdout);
	return 0;
}



