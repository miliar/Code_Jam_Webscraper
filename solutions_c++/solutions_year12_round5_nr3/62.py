#include<stdio.h>
#include<algorithm>
using namespace std;
#define MAX 2000000000000000001ll
struct data{
    long long P,S;
    bool operator<(const data& b)const{return P<b.P||(P==b.P&&S>b.S);}
}a[200];
int M,F,N;
long long day[200],need[200];
long long cost(long long mm){
    if(mm>a[N-1].S+1)return MAX;
    int tmp=lower_bound(day,day+N,mm-1)-day;
    long long v;
    if(tmp==0)v=a[0].P*mm+F;
    else v=need[tmp-1]+(mm-a[tmp-1].S-1)*a[tmp].P;
    return v;
}
long long f(long long x){
    if(x*(F+a[0].P)>M)return 0;
    long long ll=1,rr=a[N-1].S+1;
    while(ll<rr){
        long long mm=(ll+rr+1)>>1;
        long long v=cost(mm);
        if(v*x>M)rr=mm-1;
        else ll=mm;
    }
    long long v1=cost(ll);
    long long v2=cost(ll+1);
    long long res=ll*x+min((M-v1*x)/(v2-v1),x);
    return res;
}
int main(){
    int cs=0,T,i,j,k;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d",&M,&F,&N);
        for(i=0;i<N;i++)scanf("%d%d",&a[i].P,&a[i].S);
        sort(a,a+N);
        for(i=k=1;i<N;i++)
            if(a[i].S>a[k-1].S)a[k++]=a[i];
        N=k;
        for(i=0;i<N;i++)day[i]=a[i].S;
        need[0]=F+a[0].P*(a[0].S+1);
        for(i=1;i<N-1;i++)
            need[i]=need[i-1]+a[i].P*(a[i].S-a[i-1].S);
        long long an=0;
        if(F+a[0].P>M){
            printf("Case #%d: 0\n",++cs);
            continue;
        }
        for(i=1;i<=M;i++){
            long long tmp=f(i);
            if(tmp==0)break;
            an=max(an,tmp);
        }
        printf("Case #%d: %I64d\n",++cs,an);
    }
}
