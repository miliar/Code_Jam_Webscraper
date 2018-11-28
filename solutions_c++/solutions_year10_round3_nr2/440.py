#include <stdio.h>

using namespace std;
#define LL long long

LL pro(int a,int b,int c) {
	int i;
	if (b<=a*c) return 0;
	LL x = a,p = 1,tmp = 0;
	while (true) {
		if (b<=x*c) break;
		tmp++; x*= c; p++;
	}
	//printf ("%lld\n",p);
	p = (p+1)/2;
	x = 1;
	for (i=1;i<=p;i++)
		x *= c;
	return 1+pro(a,a*x,c);
}

int main (){
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	LL t,ii,l,p,c;
	scanf ("%lld",&t);
	for (ii=1;ii<=t;ii++) {
		scanf ("%lld%lld%lld",&l,&p,&c);
		printf ("Case #%lld: %lld\n",ii,pro(l,p,c));
	}
	return 0;
}
