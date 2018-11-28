#include<stdio.h>

__int64 aa[1000001],dp[1000001],dp1[1000001],tt;


int main() {
    __int64 a[1001],c,cnt,i,j,l,n,t,t1,t2,tmin;
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%I64d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%I64d %I64d %I64d %I64d",&l,&tt,&n,&c);
        for(i=0;i<c;i++)scanf("%I64d",&a[i]);
        for(i=0;i<n;i++)aa[i]=a[i%c];
        for(i=0;i<=l;i++){dp[i]=0;dp1[i]=0;}
        for(i=0;i<n;i++) {
            for(j=0;j<=l;j++)dp1[j]=dp[j];
            for(j=0;j<=l;j++) {
                t1=dp1[j]+(2*aa[i]); //regular speed to i-th star
                if(j) {
                    t2=dp1[j-1]; //high speed to i-th star (speed booster)
                    if(t2>=tt)t2+=aa[i];
                    if(t2<=(tt-(2*aa[i])))t2+=(2*aa[i]);
                    if(t2==dp1[j-1]) {
                        t2=tt+(aa[i]-((tt-t2)/2));
                    }
                    if(t1>t2)dp[j]=t2;
                    else dp[j]=t1;
                }
                else dp[j]=t1;
            }
        }
        printf("Case #%I64d: %I64d\n",cnt,dp[l]);
    }
    return 0;
}
