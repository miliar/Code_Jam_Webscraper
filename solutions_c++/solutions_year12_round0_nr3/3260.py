#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int aa;
int get(int num) {
    int l1=0;
    aa=1;
    for (;num>0;) {
        num=num/10;
        aa*=10;
        l1+=1;
    }
    aa/=10;
    return l1;
}
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;t++) {
        int a,b,ans=0;
        scanf("%d%d",&a,&b);
        for (int i=a;i<=b;i++) {
            int l=get(i);
            int n=i;
            for (int j=1;j<l;j++) {
                n=n/10+(n%10)*aa;
                if (a<=n && n<i) ans+=1;
                if (n==i) break;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
