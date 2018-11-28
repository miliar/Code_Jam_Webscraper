#include<cstdio>
#include<iostream>
#define fo(i,u,d) for(long long i=u;i<=d;i++)
using namespace std;
long long R,C,n;
long long a[2000];
long long hash[2000];
long long va[2000];
int caa;
void init(){
    cin>>R>>C>>n;
    fo(i,1,n)cin>>a[i];
}
void work(){
    fo(i,1,n)hash[i]=-1;
    long long now=1;
    long yy,xx;
    fo(i,1,1100){
        long long sum=0;
        long long tot=0;
        if (hash[now]!=-1){
            yy=i-1;
            xx=hash[now];
            break;
        }
        hash[now]=i;
        while ((sum+a[now]<=C)&&(tot+1<=n)){
            tot++;
            sum+=a[now];
            now++;
            if (now>n)now=now-n;
        }
        va[i]=sum;
    }
    long long ans=0;
    if (R<xx){
        fo(i,1,R)ans+=va[i];
    }else{
        long long pp=0;
        fo(i,xx,yy)pp+=va[i];
        fo(i,1,xx-1)ans+=va[i];
        R=R-(xx-1);
        ans+=R/(yy-xx+1)*pp;
        fo(i,1,R%(yy-xx+1))ans+=va[xx+i-1];
    }
    cout<<"Case #"<<caa<<": "<<ans<<endl;
}
int main(){
    freopen("CCC.in","r",stdin);
    freopen("CCC.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    fo(i,1,ca){
        caa=i;
        init();
        work();
    }
    return 0;
}
