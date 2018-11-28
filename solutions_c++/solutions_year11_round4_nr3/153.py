#include<stdio.h>
#include<algorithm>
using namespace std;
#define SIZE 1000000
bool p[SIZE];
int pn,pp[SIZE];
int f(int x,long long n){
    int an=0;
    while(n>=x)an++,n/=x;
    return an;
}
main(){
    int T,t=0,i,j,an;
    long long n;
    for(i=2;i*i<SIZE;i++)
        if(!p[i])
            for(j=i+i;j<SIZE;j+=i)p[j]=1;
    for(i=2;i<SIZE;i++)
        if(!p[i])pp[pn++]=i;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%lld",&n);
        if(n==1)an=0;
        else{
            an=1;
            for(i=0;i<pn&&(long long)pp[i]*pp[i]<=n;i++){
                an+=f(pp[i],n)-1;
            }
        }
        printf("Case #%d: %d\n",t,an);
    }
}
