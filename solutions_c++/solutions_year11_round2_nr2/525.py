#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int MaxN = 205;
const double Inf = 1e50;
const int MaxM = 1000005;
double eps = 1e-8;
int N,n, D;
int pos[MaxN], num[MaxN];

bool check(double t)
{
    double lst = -Inf;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < num[i]; j++)
        {
            if(lst+D > pos[i]+t+eps)return 0;
            lst = max(lst+D, pos[i]-t);
        }
    return 1;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&D);
        for(int i = 0; i < n; i++)
            scanf("%d%d",&pos[i],&num[i]);
        double lo = 0, hi = 1e20;
        while(fabs(lo-hi)>eps)
        {
            double mid = (lo+hi)/2;
            if(check(mid))hi = mid;
            else lo = mid;
        }
        printf("Case #%d: %.7f\n",++cas,(lo+hi)/2);
    }

    return 0;
}
