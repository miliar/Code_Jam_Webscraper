#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n,k,b,tim;

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d%d%d%d",&n,&k,&b,&tim);
        int chi[55],vc[55];
        for (int j=0; j<n; j++)
            scanf("%d",&chi[n-j]);
        for (int j=0; j<n; j++)
            scanf("%d",&vc[n-j]);
        int ret=0,cnt=0,last=0;
        for (int j=1; j<=n; j++) {
            if ((b-chi[j]-1)/vc[j]+1<=tim) {
               cnt++;
               ret+=last;
               }
               else last++;
            if (cnt==k) break;
            }
        if (cnt<k) printf("Case #%d: IMPOSSIBLE\n",i+1);
           else printf("Case #%d: %d\n",i+1,ret);
               
        }
    
}
