#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
long long n,d,g;
int t;

long long gcd(long long x,long long y)
{
	if(y==0) return x; else return gcd(y,x%y);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int test=1;test<=t;test++)
	{
		cin>>n>>d>>g;
		printf("Case #%d: ",test);
		if (g==100 && d<100) printf("Broken\n");
		else if(g==0 && d>0) printf("Broken\n");
		else if(n<100/gcd(100,d)) printf("Broken\n");
		else printf("Possible\n");
	}
}
	