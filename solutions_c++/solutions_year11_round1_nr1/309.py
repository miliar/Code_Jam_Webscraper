#include <stdio.h>
__int64 gcd(__int64 m,__int64 n){
    if(n==0)return m;
    if(m==0) return n;
	if(n%m==0) return m;
	else return gcd(n%m,m);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cs;
    __int64 n,pd,pg,den,num,den2,num2;
    scanf("%d",&t);
    for(cs=1;cs<=t;++cs){
        bool stat=true;
        scanf("%I64d%I64d%I64d",&n,&pd,&pg);
        den=100/gcd(pd,100);
        if(den>n) stat=false;
        if(stat){
            num=pd/gcd(pd,100);
            den2=100/gcd(pg,100);
            num2=pg/gcd(pg,100);
            if(num2==0&&num!=0) stat=false;
            if(num2==den2&&num!=den) stat=false;
        }
        if(stat) printf("Case #%d: Possible\n",cs);
        else printf("Case #%d: Broken\n",cs);
    }
    return 0;
}
