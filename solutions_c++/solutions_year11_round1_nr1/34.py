#include<stdio.h>
long long n;
int pd,pg;
inline int gcd(int a,int b){if(b)while((a%=b)&&(b%=a));return a+b;}
inline bool solve(){
    if(pg==0){
	if(pd==0)return 1;
	return 0;
    }
    if(pg==100){
	if(pd==100)return 1;
	return 0;
    }
    if(pd==0){
	if(pg==100)return 0;
	return 1;
    }
    return n>=100/gcd(100,pd);
}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
	scanf("%lld%d%d",&n,&pd,&pg);
	printf("Case #%d: %s\n",cas++,solve()?"Possible":"Broken");
    }
}
