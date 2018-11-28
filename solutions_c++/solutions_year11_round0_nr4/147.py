#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int t,n,ans;
int a[1100],bl[1100];


int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	cin >> t;
	for (int k=1;k<=t;k++)
	{
		cin >> n;
		for (int i=1;i<=n;i++) cin >> a[i];
		ans = 0;
		memset(bl,0,sizeof bl);
		for (int i=1;i<=n;i++) if (bl[i]==0)
		{
			int len = 0, now = i;
			bl[i] = 1;
			now = a[now];
			while (now!=i)
			{
				bl[now] = 1;
				len++;
				now = a[now];
			}
			ans += len==0?0:(len + 1);
		}
		printf("Case #%d: %d.000000\n",k,ans);
	}
	return 0;
}
