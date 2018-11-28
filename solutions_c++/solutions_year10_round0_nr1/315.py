#include<cstdio>
#include<iostream>
#include<cstring>
#define fo(i,u,d) for(long long i=u;i<=d;i++)
using namespace std;
long long n,k;
int ca,caa;
long long a[1000];
void init(){
    cin>>n>>k;
}
void work(){
    memset(a,0,sizeof(a));
    int t=0;
    while (k){
        t++;
        a[t]=k&1;
        k/=2;
    }
    bool ans=1;
    fo(i,1,n)if (a[i]==0)ans=0;
    if (ans){
        printf("Case #%d: ON\n",caa);
    }else{
        printf("Case #%d: OFF\n",caa);
    }
}
int main(){
    freopen("AA.in","r",stdin);
    freopen("AA.out","w",stdout);
    cin>>ca;
    fo(i,1,ca){
        caa=i;
        init();
        work();
    }
    return 0;
}
