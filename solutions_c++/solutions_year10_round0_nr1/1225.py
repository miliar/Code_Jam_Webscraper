#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	long testcase;
	scanf("%ld",&testcase);
    long right=0,n,k;
	for (long cc=0;cc<testcase;cc++) 
	{
		scanf("%ld%ld",&n,&k);
		n=1<<n;
		k=k % n;
		if (k==n-1) right=1; else right=0;
		printf("Case #%ld: ",cc+1);
		if (right) printf("ON \n");
		else printf("OFF \n");
	}
}