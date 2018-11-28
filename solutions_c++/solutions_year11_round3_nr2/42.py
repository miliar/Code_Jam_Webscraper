#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int T;
ll t;
ll a[2000000];
ll r[2000000];
ll sum,ans;
int l,n,c;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=1;k<=T;k++){
        scanf("%d%lld%d%d",&l,&t,&n,&c);
        sum=0;
        for (int i=1;i<=c;i++){
            scanf("%lld",&a[i]);
            sum+=a[i];
        }
        for (int i=c+1;i<=n;i++){
            a[i]=a[i-c];
            sum+=a[i];
        }
        int i=1;
        while (t!=0&&i<=n){
            if (t>=2*a[i]){
                t-=2*a[i];
                r[i]=0;
            }else{
                r[i]=a[i]-t/2;
                t=0;
            }
            i++;
        }
        while (i<=n){
            r[i]=a[i];
            i++;
        }
        sort(r+1,r+n+1);
        ans=2*sum;
        for (int i=n;i>n-l;i--) ans-=r[i];
        printf("Case #%d: %lld\n",k,ans);
    }
    return 0;
}
