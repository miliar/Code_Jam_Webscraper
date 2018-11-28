#include<cstdio>


int Z;
long long N,D,G;
long long da,db,ga,gb;

long long gcd(long long a,long long b){
	long long t;
	if (a>b){ t = a ; a = b ; b = t; }
	while (a>0){ t = a; ; a = b%a; b = t; }
	return b;
}

int main(){
	scanf("%d",&Z);
	for (int z=1;z<=Z;++z){
		bool ok = true;
	
		scanf("%lld%lld%lld",&N,&D,&G);
		long long g = gcd(D,100LL);
		da = D/g;	db = 100LL/g;
		
		if (db>N) ok = false;
		if (G==0 && D>0) ok = false;
		if (G==100 && D!=100) ok = false;
		
		printf("Case #%d: ",z);
		if (ok) puts("Possible");
		else puts("Broken");
	}

	return 0;
}
