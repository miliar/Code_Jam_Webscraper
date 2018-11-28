#include<cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        int MIN=10000000,sum=0,v=0;
        for(int i=0;i<n;i++){
            int a;
            scanf("%d",&a);
            if(a<MIN) MIN=a;
            v^=a;
            sum+=a;
        }
        if(v) { printf("Case #%d: NO\n",++ca);}
        else printf("Case #%d: %d\n",++ca,sum-MIN);
    }
}
