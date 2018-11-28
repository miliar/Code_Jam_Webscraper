#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;
typedef long long LL;
LL gcd(LL a,LL b){
	return b==0?a:gcd(b,a%b);
}
int main(int argc, const char *argv[])
{
	int times;
	scanf("%d",&times);
	LL N,PD,PG;
	for(int tm=1;tm<=times;tm++){
		cin>>N>>PD>>PG;
		LL wd=PD,nd=100,wg=PG,ng=100;
		LL d=gcd(wd,nd);
		wd/=d;nd/=d;

		printf("Case #%d: ",tm);
		if(ng==wg && nd!=wd)printf("Broken\n");
		else if(wd!=0 && wg==0)printf("Broken\n");
		else if(N<nd)printf("Broken\n");
		else printf("Possible\n");
	}
	return 0;
}
