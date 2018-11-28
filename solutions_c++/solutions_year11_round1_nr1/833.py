#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

typedef long long ll;
ll n,pd,pg;

ll gcd(ll a,ll b){
    if(a%b==0) return b;
    return gcd(b,a%b);
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,r=1;
    scanf("%d",&cas);
    while(cas--){
        cin>>n>>pd>>pg;
        printf("Case #%d: ",r++);
        ll p1=100,p2=100;
        int ok=0;
        if(pd==0 && pg!=100) { printf("Possible\n"); continue; }
        if(pd==0 && pg==100) { printf("Broken\n"); continue; }
        if(pg==0 && pd!=0) { printf("Broken\n"); continue; }
        
        ll g1=gcd(pd,p1), g2=gcd(pg,p2);
        pd/=g1, p1/=g1;
        pg/=g2, p2/=g2;
        
        if(p1<=n){
            if(p1==1 && p2==1) ok=1;
            else if(p2!=1){
                ok=1;
            }
        } 
        if(ok) printf("Possible\n");
        else printf("Broken\n");
    }
}
