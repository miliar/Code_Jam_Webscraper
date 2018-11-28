
/*Paresh Verma*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<list>
#include<map>

#define pub push_back
#define pob pop_back

using namespace std;

long long gcd(long long x, long long y){
	if(y==0)
		return x;
	return gcd(y, x%y);
}

int main(){
	int i,j,k,l,T;
	long long n,pd,pg;
	scanf("%d",&T);
	bool res;
	for(i=1;i<=T;i++){
		scanf("%lld%lld%lld\n",&n,&pd,&pg);
		printf("Case #%d: ",i);
		if(pd==0){
			if(pg==100){
			printf("Broken\n");
			continue;
			}
			printf("Possible\n");
			continue;
		}
		if(pg==0){
			if(pd!=0){
			printf("Broken\n");
			continue;
			}
			printf("Possible\n");
			continue;
		}
		if(pg==100){
			if(pd!=100){
			printf("Broken\n");
			continue;
			}
			printf("Possible\n");
			continue;
		}

		long long a,b,c,d,e,f;
		double x,y,z;
		x=(double)pg*1.0/pd;
		y=(double)(100-pg)/(double)(100-pd);
		a=gcd(pd,100);
		b=100/a;
		if(n<b){
			printf("Broken\n");
			continue;
		}
		

		printf("Possible\n");
	}
	return 0;
}
