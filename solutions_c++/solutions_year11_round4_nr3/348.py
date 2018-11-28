#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

#define LL long long
LL now;
LL gcd(LL a,LL b)
{
	if (b==0) return a;
	return gcd(b,a%b);
}
const int MAXN = 1000005;
LL prime[MAXN],ps;
bool isp[MAXN];
int main()
{
	memset(isp,1,sizeof(isp));
	isp[1]=false;
	ps=0;
	for (int i=2;i<MAXN;i++)
	{
		if (isp[i]) prime[++ps]=i;
		for (int j=1;prime[j]*i<MAXN;j++)
		{
			isp[prime[j]*i]=false;
			if (i%prime[j]==0) break;
		}
	}
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		LL n;
		cin >> n;
		LL ans=0;
		for (int i=1;prime[i]*prime[i]<=n;i++)
		{
			LL now=prime[i];
			int tot=0;
			for (;now<=n;tot++)
				now *= prime[i];
			ans += tot-1;
		}
		if (n>1) ans++;
		cout << "Case #" << tcase << ": " << ans << endl;
	}
	return 0;
}
