#include <iostream>
#include <cstdio>
#include <cstring>
#define Maxn 3000001
using namespace std;

bool vis[Maxn];

int numberOfDigits(int v) 
{
    int ans;
    for (;v;v/=10) ans++;
    return --ans;
}

const int decPow[7] = {1,10,100,1000,10000,100000,1000000}; 

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int k,T,a,b,i,j,n,num,ans;
    cin>>T;
    for (k=1;k<=T; k++) {
        memset(vis,0,sizeof(vis));
        cin>>a>>b;
        ans=0;
        num = numberOfDigits(a); 
        for (i=a; i<=b; i++) {
            n=0;
            while (!vis[i]) {
                if (i/decPow[num] && i<=b && i>=a) {
                    n++;
                    vis[i]=1;
                }
                i=(i-(i/decPow[num])*decPow[num])*10+(i/decPow[num]);
            }
            ans += n*(n-1)/2;
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
