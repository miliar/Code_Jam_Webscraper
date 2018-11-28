#include <iostream>
#include <cstdio>

typedef long long LL;

using namespace std;

int t;

int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}

bool test(int n,int pd,int pg)
{
	if(pg==0)return pd==0;
	if(pg==100)return pd==100;
	if(pd==0)return true;
	int a=pd,b=100;
	int g=gcd(a,b);
	b/=g;
	return b<=n;
}

int main()
{
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		LL n,pd,pg;	
		cin>>n>>pd>>pg;
		printf("Case #%d: ",i);
		if(test(n,pd,pg))printf("Possible\n");else printf("Broken\n");
	}
}
