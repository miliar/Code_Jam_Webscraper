#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define FORALL(a,b) for(typeof((b).begin()) a = (b).begin(); a != (b).end(); ++a)
#define FOR(i,a,b) for(int i = a; i < (int)(b); ++i)

typedef long long LL;

const double EPS = 1e-6;
const int INF = 1<<29;
const int N = 1010;

LL W, L, n;

typedef struct Node{
    LL x, y, w, l;
    LL s;
    bool operator < (const Node &other) const{
        return s < other.s;
    }
}Node;

Node node, a, b;
LL r[N];
LL x[N], y[N];

int main()
{
//    freopen("in.txt","r",stdin);
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T, cas = 0;

    scanf("%d", &T);

    while (T--){
        scanf("%I64d", &n);
        scanf("%I64d %I64d", &W, &L);

        bool visit[N] = {};

        for (int i = 0; i < n; ++i){
            scanf("%I64d", &r[i]);
            x[i] = y[i] = -1;
        }

        priority_queue<Node> Q;
        node.x = 0, node.y = 0;
        node.w = W, node.l = L;
        node.s = node.w*node.l;
        Q.push(node);

        while (1){
            node = Q.top();
            Q.pop();
            int mark = -1;
            for (int i = 0; i < n; ++i){
                if (visit[i]) continue;
                if (mark == -1 || r[i] > r[mark]) mark = i;
            }
            if (mark == -1) break;

            x[mark] = node.x;
            y[mark] = node.y;

            a.x = node.x+r[mark]*2;
            a.y = node.y;
            a.w = node.w-r[mark]*2;
            a.l = r[mark]*2;

            b.x = node.x;
            b.y = node.y+r[mark]*2;
            b.w = r[mark]*2;
            b.l = node.l-r[mark]*2;

            if (W >= L) a.l = node.l;
            else b.w = node.w;

            a.s = a.w*a.l;
            b.s = b.w*b.l;

            if (a.w >= 0 && a.l >= 0) Q.push(a);
            if (b.w >= 0 && b.l >= 0) Q.push(b);

            visit[mark] = 1;
        }
        printf("Case #%d:", ++cas);
        bool flag = 1;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (i != j && (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]) < (r[i]+r[j])*(r[i]+r[j]))
                    flag = 0;
//        printf("%s\n", flag ? "YES" : "NO");
        for (int i = 0; i < n; ++i) printf(" %.1lf %.1lf", x[i]*1.0, y[i]*1.0);
        putchar('\n');
    }

    return 0;
}
