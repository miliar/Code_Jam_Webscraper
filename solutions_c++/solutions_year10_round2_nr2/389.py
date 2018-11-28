#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
int N,K,B,T;
int pos[51], v[51];
int rec[51], rn;
struct cmp {
    bool operator()(const int a, const int b) {
        int la=B-pos[a], lb=B-pos[b];
        if(la*v[b]!=lb*v[a]) return la*v[b]>lb*v[a];
        else return pos[a]<pos[b];
    }    
};
bool cmp2(int a, int b) {
    return pos[a]>pos[b];
}


int main() {
    int tt;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out","w", stdout);
    scanf("%d",&tt);
    int n,K,cas=1;
    while(tt--) {
        scanf("%d%d%d%d",&N,&K,&B,&T);
        for(int i=0; i<N; i++) scanf("%d",&pos[i]);
        for(int i=0; i<N; i++) scanf("%d",&v[i]);
        int ans=0, rn=0;
        for(int i=N-1; i>=0; i--) {
            int tmp=B-pos[i];
            if(tmp>T*v[i]) ans+=(K-rn);
            else {
                rn++;
                if(rn>=K) break;
            }
        }
        if(rn<K) printf("Case #%d: IMPOSSIBLE\n",cas++);
        else printf("Case #%d: %d\n", cas++, ans);
    }
    //system("pause");
    return 0;
}
