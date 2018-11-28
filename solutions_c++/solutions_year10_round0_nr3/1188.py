#include<stdio.h>
#include<stdlib.h>
long long a[2000];
long long s[2000];
long long next[2000];
int main(){
    freopen("C-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
        int r,k,n;
        scanf("%d %d %d",&r,&k,&n);
        for(int i=0;i<n;i++)scanf("%lld",&a[i]);
        for(int i=0;i<n;i++){
            int now=i+1;
            s[i]=a[i];
            while(s[i]+a[now%n]<=k&& (now%n)!=i){
                s[i]+=a[now%n];
                now++;
            }
            next[i]=now%n;
        }
        long long sum=0;
        int now=0;
        for(int i=0;i<r;i++){
            sum+=s[now];
            now=next[now];
        }
        printf("Case #%d: %lld\n",test,sum);
    }
}
