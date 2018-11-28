#include<cstdio>
#include<cstring>
using namespace std;
typedef long long ll;
ll n,m;
ll a,b,c;
ll abb(ll x)
{
	return x<0?-x:x;
}
ll gcd(ll a,ll b)
{
	return !b?a:gcd(b,a%b);
}
int main()
{
	freopen("fair.in","r",stdin);
	freopen("fair.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	for(int round=1;round<=cs;++round)
	{
		printf("Case #%d: ",round); 
		scanf("%lld",&n);
		scanf("%lld%lld",&a,&b);
		if(n==2) {			
			ll d=abb(a-b);
			if(d==1)	 printf("0\n");
			else printf("%lld\n",(d-a%d)%d);
		}else {
			scanf("%lld",&c);
			ll d=gcd(abb(a-b),abb(b-c));
			d=gcd(d,abb(a-c));
			if(d==1) printf("0\n");
			else printf("%lld\n",(d-a%d)%d);
		}
	}
	return 0;
}
