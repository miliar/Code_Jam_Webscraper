#include<cstdio>
using namespace std;
typedef int ll;
int f(int a){
	return (a>=0)?a:-1*a;
}	
ll gcd(ll a, ll b)
{
	if(!b)	return a;
	return gcd(b,a%b);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		int n;
		scanf("%d",&n);
		ll a[1002];
		for(int i=0;i<n;i++)	scanf("%d",&a[i]);
		ll hcf=0,hcf1=0;
		for(int i=0;i<n;i++)	hcf1=gcd(hcf1,a[i]);
		if(n==2)	 hcf=f(a[0]-a[1]);
		else{
			hcf=gcd(f(a[0]-a[1]),f(a[1]-a[2]));hcf=gcd(hcf,f(a[0]-a[2]));
		}
		ll ans=hcf-(a[0]%hcf);if(hcf==hcf1)ans=0;	
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}			
