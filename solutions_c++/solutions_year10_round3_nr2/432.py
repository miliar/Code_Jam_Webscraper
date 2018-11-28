#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
using namespace std;

long long T,L,P,C;

int main()
{
	long long ans;
	int Case=1;
	freopen("B-large.in","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%lld",&T);
	for(;T>0;T--)
	{
		scanf("%I64d%I64d%I64d",&L,&P,&C);
		L = L*C;
		printf("Case #%d: ",Case++);
		for(ans=0;L<P;)
		{
			ans++;
			L*=C;
			C*=C;
		}
		printf("%I64d\n",ans);
	}
	return 0;
}
