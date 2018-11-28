#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 1005;
const double eps = 1e-9;
struct Node
{
    int l,v;
}q[MaxN];
int X,S,R,t,N;

bool cmp(Node p1,Node p2)
{
    return p1.v<p2.v;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
        int tot = 0;
        for(int i = 0; i < N ;i++)
        {
            int x,y;
            scanf("%d%d%d",&x,&y,&q[i].v);
            tot+=y-x;
            q[i].l = y-x;
        }
        q[N].l = X-tot;
        q[N++].v = 0;
        sort(q,q+N,cmp);
        double ret = 0, left = t;
        for(int i = 0; i < N; i++)
        {
            double l = q[i].l, v = q[i].v;
            if(fabs(left)>eps)
            {
                double tp = min(l/(v+R), left);
                ret += tp;
                l -= tp*(v+R);
                left -= tp;
            }
            ret += l/(v+S);
        }
        printf("Case #%d: %.9f\n",++cas,ret);
    }

    return 0;
}
