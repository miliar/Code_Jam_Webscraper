#include <iostream>
#include <cstdio>
using namespace std;
int gcd(int m,int n)
{
	if (n==0) return m;
	else return gcd(n,m%n);
}
int main()
{
    int tt;
    cin >> tt;
    for (int tc=1;tc<=tt;tc++)
    {
    	int pd,pg;
    	long long n;
    	cin >> n >> pd >> pg;
    	printf("Case #%d: ",tc);
    	if (pg==100)
    	{
    		if (pd==100) {printf("Possible\n");continue;}
    		else {printf("Broken\n");continue;}
    	}
    	else if (pg==0)
    	{
    		if (pd==0) {printf("Possible\n");continue;}
    		else {printf("Broken\n");continue;}
    	}
    	else
    	{
    		//printf("%d %dmmmmmmmmm\n",n,gcd(pd,100));
    		if (n>=100/gcd(pd,100)) printf("Possible\n");
    		else printf("Broken\n");
    	}
    }
    return 0;
}
