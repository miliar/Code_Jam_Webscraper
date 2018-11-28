#include<cstdio>
#include<algorithm>
#define L 10000
using namespace std;

int a,b,p,now,tmp,ans;
bool prime[L];
int i,j,T,I,d,k;
int s[100],ma;

int main(){
    for (i=0;i<10000;++i) prime[i]=1;
    for (i=2;i*i<10000;++i)
        if (prime[i])
            for (j=i*i;j<10000;j+=i)
                prime[j]=0;
    scanf("%d",&T);
    while (T--){
        printf("Case #%d: ",++I);
        scanf("%d%d",&d,&k);
        for (i=0;i<k;++i) scanf("%d",&s[i]);
        now=1;
        ans=-2;
        for (i=0;i<d;++i) now=now*10;
        if (k==1) {printf("I don't know.\n");continue;}
        ma=0;
        for (i=0;i<k;++i)
            ma=max(ma,s[i]);
        for (p=ma+1;p<now;++p)
            if (prime[p])
                for (a=0;a<p;++a){
                    b=-2;
                    for (i=0;i<k-1;++i)
                        if (b==-2)
                            b=((s[i+1]-s[i]*a)%p+p)%p;
                        else if (b!=((s[i+1]-s[i]*a)%p+p)%p)
                            b=-1;
                    if (b==-1) continue;
//                    printf("%d %d %d\n",a,b,p);
                    tmp=(a*s[k-1]+b)%p;
                    if (ans==-2) ans=tmp;
                    else if (ans!=tmp) ans=-1;
                }
        if (ans==-1) puts("I don't know.");
        else printf("%d\n",(int)ans);
    }
}
