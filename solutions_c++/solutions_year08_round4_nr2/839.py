#include <cstdio>
typedef long long ll;
void Solve(int);
int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++) Solve(i+1);
	return 0;
}
void Solve(int x)
{
	ll P,M,N;
	scanf("%lld %lld %lld",&N,&M,&P);
	for(ll a=0;a<=N;a++)
		for(ll b=0;b<=N;b++)
			for(ll c=0;c<=M;c++)
				for(ll d=0;d<=M;d++)
					if((c*b) - (a*d)==P)
					{
						printf("Case #%d: 0 0 %lld %lld %lld %lld\n",x,a,c,b,d);
						return;
					}
	printf("Case #%d: IMPOSSIBLE\n",x);

}
