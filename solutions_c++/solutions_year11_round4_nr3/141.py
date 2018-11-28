#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long LL;
int T;
LL N;
bool HS[1000005];
int Cal(int x,LL y) {
    int t=0;
    LL ans=1;
    while (ans<=y) {
          ans*=x;
          ++t;
    }
    return t-1;
}
int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    cin>>T;
    for (int cnt=1;cnt<=T;++cnt) {
        cin>>N;
        int ans=0;
        if (N!=1) ans=1;
        memset(HS,false,sizeof(HS));
        for (int i=2;(LL)i*i<=N;++i) 
            if (!HS[i]) {
               ans+=Cal(i,N)-1;
               int t=i+i;
               while ((LL)t*t<=N) {
                     HS[t]=true;
                     t+=i;
               }
            }
        printf("Case #%d: %d\n",cnt,ans);
    }
    return 0;
}
