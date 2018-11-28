#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

typedef long long LL;

const int maxp=1000005;

bool a[maxp+5];
int prime[maxp+5],pp;

LL n;

void eratos(){
     pp=0;
     memset(a,true,sizeof(a));
     a[1]=false;
     for (int i=2;i<=maxp;i++)
         if (a[i]) {
            prime[++pp]=i;
            for (int j=i+i;j<=maxp;j+=i) 
                a[j]=false;
         }
}


void solve(){
     cin>>n;
     if (n==1) {
        printf("0\n"); 
        return ;
     }
     LL ans=0;
     for (int i=1;i<=pp;i++) {
         if (prime[i]>n) break;
         double temp=log(double(n))/log(double(prime[i]));
         ans+=int(temp+1e-10)-1;
     }
     ans++;
     cout<<ans<<endl;
}

int main(){
    
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    
    eratos();
    int test;
    cin>>test;
    for (int tot=1;tot<=test;tot++) {
        printf("Case #%d: ",tot);
        solve();
    }
    
    
    return 0;
}
