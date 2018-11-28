#include <cstdio>
#include <cstring>
#include <cassert>
#include <utility>
#include <set>
#include <algorithm>
using namespace std;

#ifdef mahou_shoujo_madoka
    #define LLF "%I64d"
    #define ASSERT(x) assert(x)
#else
    #define LLF "%lld"
    #define ASSERT(x)
#endif

typedef pair<int,int> PII;

int main(){
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        int x,s,r,o,n;
        vector<PII> u;
        scanf("%d%d%d%d%d",&x,&s,&r,&o,&n);
        for(int i=0;i<n;i++){
            int p,q,w;
            scanf("%d%d%d",&p,&q,&w);
            u.push_back({s+w,q-p});
            x-=q-p;
        }
        u.push_back({s,x});
        sort(u.begin(),u.end());
        double ans=0,c=o;
        for(auto& v:u){
            double l=min(v.second*1.0,c*(v.first+r-s));
            ans+=(v.second-l)/v.first+l/(v.first+r-s);
            c-=l/(v.first+r-s);
        }
        printf("Case #%d: %.12f\n",t,ans);
    }
}