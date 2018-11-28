#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

const int MAX = 1010;

struct NODE
{
    int b;
    int e;
    int w;

    bool operator < (const NODE &a) const
    {
        return w > a.w;
    }
};

priority_queue<NODE> qq;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    int cases = 1;
    scanf("%d", &T);

    int X;
    int S;
    int R;
    int t;
    int N;
    while (T-- > 0)
    {
        scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
        int b, e, w;
        int st = 0;
        double ti;
        double ans;
        NODE node;
        for (int i = 0; i < N; i++)
        {
            scanf("%d %d %d", &b, &e, &w);
            if (b != st)
            {
                node.b = st;
                node.e = b;
                node.w = 0;
                qq.push(node);
            }
            node.b = b;
            node.e = e;
            node.w = w;
            qq.push(node);
            st = e;
        }
        if (st != X)
        {
            node.b = st;
            node.e = X;
            node.w = 0;
            qq.push(node);
        }
        ans = 0;
        double total = t;
        while (!qq.empty())
        {
            node = qq.top();
            qq.pop();
            int len = node.e - node.b;
            if (total > 1e-6)
            {
                ti = (double)len / (node.w + R);
                if (total >= ti)
                {
                    total = (double)total - ti;
                    ans += ti;
                }
                else
                {
                    ans += total;
                    ti = (double)(len - (node.w + R) * total) / (node.w + S);
                    ans += ti;
                    total = 0;
                }
            }
            else
            {
                ans += (double)len / (node.w + S);
            }
        }
        printf("Case #%d: %.8lf\n", cases++, ans);
    }
    return 0;
}
