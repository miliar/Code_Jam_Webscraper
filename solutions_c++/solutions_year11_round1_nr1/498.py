#include<stdio.h>
#include<string.h>
inline int abs(int a){
	if(a<0)return -a;
	else return a;
}
#define max(a,b) ((a>b) ? (a) : (b))
//com a[128];
int solve(){
	long long n,d,g,k=100;
	
	scanf("%lld%lld%lld",&n,&d,&g);
	if(g==100 && d!=100 || g==0 && d!=0){
		printf("Broken");
		return 0;
	}

	if(d%2==0){
		d/=2;
		k/=2;
	}
	if(d%2==0){
		d/=2;
		k/=2;
	}if(d%5==0){
		d/=5;
		k/=5;
	}
	if(d%5==0){
		d/=5;k/=5;
	}
	if(n>=k)printf("Possible");
	else printf("Broken");
	return  0;
}
int main(){
	int t;
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	scanf("%d",&t);
	for(int I=1;I<=t;I++){
		printf("Case #%d: ",I);
		solve();
		putchar('\n');
	}
	return 0;
}