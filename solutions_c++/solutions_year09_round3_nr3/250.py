#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;

int t,n,m;

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d%d",&n,&m);
        vector<int> v(m);
        for (int j=0; j<m; j++)
            scanf("%d",&v[j]);
        sort(v.begin(),v.end());
        int p[10005]; memset(p,0,sizeof(p));
        p[0]=-1; p[n+1]=-1;
        int ans=0,ret=2147483647;
        do {
            ans=0; memset(p,0,sizeof(p)); p[0]=-1; p[n+1]=-1;
            for (int j=0; j<m; j++) {
                p[v[j]]=-1;
                int ti=v[j]-1;
                while (p[ti]==0) {
                   ans++; ti--;
                   }
                ti=v[j]+1;
                while (p[ti]==0) {
                   ans++; ti++;
                   }
                //printf("%d: %d\n",v[j],ans);
                }
            ret=min(ans,ret);
            } while (next_permutation(v.begin(),v.end()));
        printf("Case #%d: %d\n",i+1,ret);
        }
    
}
