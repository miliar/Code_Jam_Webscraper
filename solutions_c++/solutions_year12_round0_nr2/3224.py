#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++) {
        int n,s,p;
        scanf("%d%d%d",&n,&s,&p);
        int ans=0,num,l1,l2;
        l1=max(p-1,0)*2+p;
        l2=max(p-2,0)*2+p;
        for (int i=1;i<=n;i++) {
            scanf("%d",&num);
            if (num>=l1) ans+=1;
            else if (num>=l2 && s>0) {
                ans+=1;
                s-=1;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
