#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args);

typedef long long lint;
typedef pair<int,int> pii;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXN = 10010;

struct vine {
    int d,l;
    void read() {
        scanf("%d%d",&d,&l);
    }
};

vine v[MAXN];
int n;
int height[MAXN];
bool foi[MAXN];

void dijkstra() {
    int now,h;
    while(1) {
        h=-1;
        for(int a=0;a<n;++a) {
            if(!foi[a] && height[a] > h) {
                h = height[a];
                now = a;
            }
        }
        if(h==-1) break;
        foi[now] = 1;
        for(int a=0;a<=n;++a) {
            if(abs(v[a].d-v[now].d)<=h) {
                height[a] = max(height[a],min(abs(v[a].d-v[now].d),v[a].l));
            }
        }
    }
}        

int main() {
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        debug("Running test case %d...\n",t);
        scanf("%d",&n);
        for(int a=0;a<n;++a) v[a].read();
        scanf("%d",&v[n].d);
        v[n].l = 0;
        memset(height,-1,sizeof(height));
        memset(foi,0,sizeof(foi));
        height[0] = v[0].d;        
        dijkstra();
        printf("Case #%d: %s\n",t,height[n]==0?"YES":"NO");
    }
    return 0;
}
