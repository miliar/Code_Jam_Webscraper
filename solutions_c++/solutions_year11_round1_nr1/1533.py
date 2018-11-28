#include<iostream>
#include<cstdio>

using namespace std;

long gcd(long a,long b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	long cs=0,t,n,pd,pg,g;

	cin >> t;

	while( t-- ){
		printf("Case #%ld: ",++cs);
		cin >> n >> pd >> pg;
		g = gcd(100,pd);
		if(n<100/g||(pd<100&&pg==100) || (pd>0&&pg==0) )
			printf("Broken");
		else{
			printf("Possible");
			//printf(" %ld %ld %ld - %ld %ld\n",n,pd,pg,g,100/g);
		}
		printf("\n");
	}
	return 0;
}

