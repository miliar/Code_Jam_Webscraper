#include<stdio.h>

int main() {
    int c[1000],cc,cmin,cnt,i,j,n,no,sum,sum1[32],t;
    freopen("c1.in","r",stdin);
    freopen("c1.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%d",&n);
        cmin=9999999;sum=0;
        for(i=0;i<32;i++)sum1[i]=0;
        for(i=0;i<n;i++) {
            scanf("%d",&c[i]);
            sum+=c[i];
            if(c[i]<cmin)cmin=c[i];
            cc=c[i];j=0;
            while(cc) {
                sum1[j]+=(cc%2);
                cc/=2;j++;
            }
        }
        no=0;
        for(i=0;i<32;i++)if(sum1[i]%2)no=1;
        if(no)printf("Case #%d: NO\n",cnt);
        else printf("Case #%d: %d\n",cnt,sum-cmin);
    }
    //while(1);
    return 0;
}
