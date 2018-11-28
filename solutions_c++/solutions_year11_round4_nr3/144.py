#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

#define LL long long

int p[1000050],u[1000050],tes,pri;
LL n;

LL solve(LL n)
{
	LL ans=(n>1);
	for (int i=1;i<=pri;i++)
		if (p[i]>n) break;
		else
		{
			LL pp=p[i]; pp=pp*p[i];
			while (pp<=n) { ans++; pp=pp*p[i]; }
			//cout <<p[i]<<" "<<ans<<endl;
		}
	return ans;
}

void prepare()
{
	for (int i=2;i<=1000000;i++)
		if (!u[i])
		{
			p[++pri]=i;
			for (int j=i+i;j<=1000000;j+=i) u[j]=1;
		}
}


int main()
{
	freopen("c.out","w",stdout);
	prepare();
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		printf("Case #%d: ",ttt);
		scanf("%lld",&n);
		printf("%lld\n",solve(n));
	}
}
