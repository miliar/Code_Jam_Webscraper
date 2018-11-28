#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n,r,cap,a[1005],v[1005],next[1005];
long long mst[1005];
vector<int> rec;

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    for (int i=0; i<t; i++) {
        scanf("%d%d%d",&r,&cap,&n);
        for (int j=0; j<n; j++)
            scanf("%d",&a[j]);
        for (int j=0; j<n; j++) {
            mst[j]=0;
            int ind=j;
            long long cnt=0;
            while (cnt+a[ind]<=cap) {
               cnt+=a[ind];
               ind++;
               ind%=n;
               if (ind==j) break;
               }
            next[j]=ind;
            mst[j]=cnt;
            }
        memset(v,-1,sizeof(v));
        rec.clear();
        int at=0,step=0;
        while (v[at]==-1) {
           v[at]=step;
           step++;
           rec.push_back(at);
           at=next[at];
           }
        long long ans=0,cycans=0;
        int cyc=step-v[at];
        for (int j=0; j<min(r,v[at]); j++) ans+=mst[rec[j]];
        r-=v[at];
        
        if (r>0) {
           for (int j=v[at]; j<v[at]+r%cyc; j++)
               ans+=mst[rec[j]];
           for (int j=v[at]; j<rec.size(); j++)
               cycans+=mst[rec[j]];
           ans+=cycans*(r/cyc);
           }
        //printf("%d %lld\n",cyc,cycans);
        printf("Case #%d: %lld\n",i+1,ans);
        }
    
}
