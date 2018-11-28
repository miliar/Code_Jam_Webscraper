#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
//#define ONLINE_JUDGE
#define PB push_back
#define MP make_pair
#define CLR(x,y) memset((x),y,sizeof(x))
#define rep(i,n) for(int i=0; i<(n); i++)
#define forr(i,a,b) for(int i=(a);i<=(b);i++)

const int N = 105;

struct Node{
    int col;
    int loc;
} node[N];

struct Edge{
    int v,w,next;   
} e[N*N];

int sz, st[N], deg[N], ti[N];

inline void addEdge(int u,int v, int w) {
    e[sz].v = v;
    e[sz].w = w;
    e[sz].next = st[u];
    st[u] = sz;
    ++sz;
    deg[v]++;   
}

int ans;

void topsort(int v0, int n) {
    queue<int> que;
    
    que.push(v0);
    rep(i,n) {
        ti[i] = 0;   
    }
    ti[v0] = 0;
    ans = 1;
    while(!que.empty()) {
        int cur = que.front();
        que.pop();
        
        if(ans<ti[cur]) ans=ti[cur];
        
        for(int j=st[cur]; j!=-1; j=e[j].next) {
            int v = e[j].v, w = e[j].w;
            deg[v]--;
            ti[v] = max(ti[v], ti[cur]+w);
            if(deg[v] == 0) {
                que.push(v);   
            }
        }   
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    #endif

    int tt, cas = 1;
    scanf("%d", &tt);
    for(cas=1; cas<=tt; cas++) {
        //To-Do
        int n;
        char str[5];
        scanf("%d",&n);
        
        for(int i=0; i<n; i++) {
            scanf("%s%d", str, &node[i].loc);   
            if(str[0]=='O') node[i].col = 0;
            else node[i].col = 1;
        }
        
        sz = 0;
        forr(i,0,n) {
            st[i] = -1;
            deg[i] = 0;
        }
        
        int pre[2] = {-1,-1};
        
        for(int i=0; i<n; i++) {
            addEdge(n, i, abs(1-node[i].loc)+1);
            if(i+1<n) {
                if(node[i].col != node[i+1].col) {
                    addEdge(i,i+1,1);   
                }
                else {
                    addEdge(i,i+1, abs(node[i].loc-node[i+1].loc)+1);
                }
            }
            int col = node[i].col;
            if(pre[col] != -1) {
                addEdge(pre[col], i, abs(node[pre[col]].loc-node[i].loc)+1);
            }
            pre[col] = i;
        }
        
        topsort(n, n+1);
        
        printf("Case #%d: %d\n", cas, ans);
    }
    //system("pause");
    return 0;
}
