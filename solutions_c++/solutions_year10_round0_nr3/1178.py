#include<stdio.h>
#include<string.h>
typedef long long LL;

LL r,k,g[1010],n;
LL a[1010],b[1010];

LL f(LL id) {
    LL ans = 0,j=id,i=0;
    for (; i < r; ++i) {
        LL sum = 0;
        LL jx = j;
        while (1) {
            sum += g[j++];
            if (j >= n)j = 0;
            if (sum + g[j] > k || jx == j)break;
        }
        ans += sum;
    }
    return ans;
}

LL ff(LL id,LL &st,LL &len,LL &jxj,bool &rxr) {
    LL ans = 0,j=id,i=0;
    memset(a,-1,sizeof(a));
    memset(b,-1,sizeof(b));
    for (; i < r; ++i) {
        if(a[j]==-1){
            a[j]=ans;
            b[j]=i;
        }
        else{
            rxr=true;
            jxj=j;
            st=b[j];
            len=i-st;
            return ans;
        }
        int sum = 0;
        int jx = j;
        while (1) {
            sum += g[j++];
            if (j >= n)j = 0;
            if (sum + g[j] > k || jx == j)break;
        }
        ans += sum;
    }
    rxr=false;
    return ans;
}

int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    LL i,j,x,t;
    scanf("%I64d",&t);
    for(x=1;x<=t;++x){
        scanf("%I64d%I64d%I64d",&r,&k,&n);
        for(i=0;i<n;++i){
            scanf("%I64d",&g[i]);
        }
        LL star,len,ans=0,sum,s1;
        bool falg;
        s1=ff(0,star,len,j,falg);
        if (falg) {
            ans += a[j];
            LL rx = s1 - a[j];
            r -= b[j];
            ans += (r / len * rx);
            r %= len;
            ans += f(j);
        }
        else ans=s1;
        printf("Case #%I64d: %I64d\n",x,ans);
    }
    return 0;
}
