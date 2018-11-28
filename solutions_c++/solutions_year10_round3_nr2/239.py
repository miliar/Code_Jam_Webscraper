#include <cstdio>

int t;
long long l, p, c;

long long max(long long a, long long b){
	return a>b ? a : b;
}

long long sqrt(long long p){
	long long l=0, r=p, mid;
	while(l!=r){
		mid= (l+r)/2;
		if(mid*mid < p) l = mid+1;
		else r = mid;
	}
	return l;
}

int func(long long l, long long r){
//	printf("func %I64d %I64d\n", l, r);
	int rtn= 0;
	if(l*c >= r)rtn= 0;
	else rtn= max(func(l, sqrt(r/l)*l), func(sqrt(r/l)*l, r))+1;
//	printf(">>>>> %I64d %I64d: %d\n", l, r, rtn);
	return rtn;
}

int main(){
	scanf("%d", &t);
	for(int cnt=1; cnt<=t; cnt++){
		scanf("%I64d%I64d%I64d", &l, &p, &c);
		printf("Case #%d: %d\n", cnt, func(l, p));
	}
}
