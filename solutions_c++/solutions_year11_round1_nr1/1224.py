#include<cstdio>
#define LL long long
int gcd(LL a,LL b){
	return b?gcd(b,a%b):a;
}
int main(){
    int C,cc,n,d,g,t;
    freopen("ain.txt","r",stdin);
    freopen("aou.txt","w",stdout);
	scanf("%d",&C);
	for(cc=1;cc<=C;++cc){
		scanf("%d%d%d",&n,&d,&g);
		printf("Case #%d: ",cc);
		if((d>0&&g==0)||(d<100 && g>=100)){
			puts("Broken");
			continue;
		}
		t=100/gcd(d,100);
		puts(t<=n?"Possible":"Broken");
	}
	return 0;
}
