#include<stdio.h>
long long work(long long a,long long b){
	long long res;
	long long bit;
	res=1;
	bit=a;
	while(b){
		if(b&1) res*=bit;
		bit*=bit;
		b>>=1;
	}
	return res;
}
long long log2(long long a){
	int i;
	int b;
	b=1;
	for(i=0;b<a;i++){
		b*=2;
	}
	return i;
}
int main(){
	long long T;
	long long l,p,c;
	long long i;
	long long a;
	int cases=0;
	freopen("e:\\B-large.in","r",stdin);
	freopen("e:\\B-large.out","w",stdout);
	scanf("%lld",&T);
	while(T--){
		scanf("%lld %lld %lld",&l,&p,&c);
		a=l;
		for(i=0;a<p;i++){
			a*=c;
		}
		printf("Case #%d: %lld\n",++cases,log2(i));
	}
}