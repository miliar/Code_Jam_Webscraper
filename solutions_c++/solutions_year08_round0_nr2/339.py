#include <iostream>
#include <cmath>
using namespace std;
typedef struct Journey {
    int start,end,type;
    bool seen;
    bool operator<(const Journey& j) const {
        return start<j.start;
    }
};
Journey js[300];
int ans[2];
int main() {
    int N; scanf("%d",&N);
    for (int cn=1; cn<=N; cn++) {
        int T,NA,NB;scanf("%d %d %d",&T,&NA,&NB);
        for (int i=0; i<NA+NB; i++) {
            int h,m;
            scanf("%d:%d",&h,&m);
            js[i].start=h*60+m;
            scanf("%d:%d",&h,&m);
            js[i].end=h*60+m;
            js[i].type=(i<NA?0:1);
            js[i].seen=false;
        }
        ans[0]=ans[1]=0;
        sort(js,js+NA+NB);
        for (int i=0; i<NA+NB; i++) {
            if (js[i].seen) continue;
            ans[js[i].type]++;
            js[i].seen=true;
            int curend=js[i].end+T;
            int curtype=js[i].type;
            for (int j=i+1; j<NA+NB; j++) {
                if (js[j].seen || js[j].type==curtype || js[j].start<curend) continue;
                js[j].seen=true;
                curtype=js[j].type;
                curend=js[j].end+T;
            }
        }
        printf("Case #%d: %d %d\n",cn,ans[0],ans[1]);
        
    }
    return 0;
}
