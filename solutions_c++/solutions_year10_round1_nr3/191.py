#include<iostream>
#include<stdio.h>
using namespace std;
long testcase,ans,a1,b1,a2,b2;

int gcd(int a,int b)
{
	if (a<b) { int tem=a; a=b; b=tem; }
	if (a==b) return 0;
	if (a>=b+b) return 1;
	return (1-gcd(b,a%b));
}

int work()
{
	ans=0;
	for (int a=a1;a<=a2;a++)
	{
		for (int b=b1;b<=b2;b++) ans+=gcd(a,b);
	}

}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%ld ",&testcase);
	for (int ttt=1;ttt<=testcase;ttt++)
	{
		scanf("%ld %ld %ld %ld ",&a1,&a2,&b1,&b2);
		work();
		printf("Case #%ld: %ld \n",ttt,ans);
	}
}
