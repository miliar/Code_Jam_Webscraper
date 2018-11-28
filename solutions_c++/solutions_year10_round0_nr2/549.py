#include<iostream>
using namespace std;
long gcd(long a,long b)
{
	if (b==0) return a;
	else return gcd(b,a%b);
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("b.out","w",stdout);
	long a[10];
	long testcase;
	scanf("%ld",&testcase);
	for (long cc=1;cc<=testcase;cc++)
	{
		long n;
		scanf("%ld",&n);
		for (int i=1;i<=n;i++) scanf("%ld",&a[i]);
		long g=abs(a[1]-a[2]);
		if (n==3) g=gcd(g,abs(a[2]-a[3]));
		if ((a[1]%g)!=0) g=g-(a[1]%g); else g=0;
		printf("Case #%ld: %ld \n",cc,g);
	}

}