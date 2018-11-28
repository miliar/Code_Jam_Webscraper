#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
using namespace std;

int gcd(int a,int b){
	if(b==0)return a;
	return gcd(b,a%b);
}

int main(){
	int t,h,i,pd,pg;
	long long n;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%lld%d%d",&n,&pd,&pg);
		i=100/gcd(pd,100);
		printf("Case #%d: ",h);
		if(pd<100 && pg==100)printf("Broken\n");
		else if(pd>0 && pg==0)printf("Broken\n");
		else if(i<=n)printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}
