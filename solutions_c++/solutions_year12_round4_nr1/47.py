#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const int MAXN=10009;
int T;
int n;
long l[MAXN],d[MAXN],f[MAXN],m;

void init()
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
		scanf("%ld %ld",&d[i],&l[i]);
	scanf("%ld",&m);
}

bool work()
{
	memset(f,0,sizeof(f));
	f[1]=d[1];
	for (int i=1;i<=n;i++)
	{
		if (m-d[i]<=f[i]) return true;
		for (int j=i+1;j<=n;j++)
			if (d[j]-d[i]<=f[i])
			{
				f[j]=max(f[j],d[j]-d[i]);
				f[j]=min(f[j],l[j]);
			}
	}
	return false;
}

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		init();
		printf("Case #%d: ",t);
		if (work()) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}
