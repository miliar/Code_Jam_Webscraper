#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;
#define N 1005
int n, w, l;
pair<int, int> r[N];
struct opt
{
    int a,b;
}num[12312];
pair<int, pair<int, int> > res[N];
int main() {
    freopen("bs.in", "r", stdin);
    freopen("bs.out", "w", stdout);
    int cas, cass = 0;
    scanf("%d",&cas);
    while (cas--)
    {
        scanf("%d%d%d",&n,&w,&l);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d",&r[i].first);
            r[i].second = i;
        }
        sort(r + 1, r + 1 + n);
        int t = -1000000000, last = -r[1].first, nt = t;
        bool lr = 0;
           for(int ddd =0; ddd<n;ddd++)
        {
            num[ddd].a=last+ddd;
            num[ddd].b=nt-ddd;
        }
        for (int i = 1; i <= n; i++)
        {
            if (!lr)
            {
                if (last + r[i].first <= w)
                {
                    res[i].first = r[i].second;
                    res[i].second.first = last + r[i].first;
                    res[i].second.second = max(t + r[i].first, 0);
                    nt = max(nt, res[i].second.second + r[i].first);
                    last += 2 * r[i].first;
                } else {
                    lr = 1;
                    last = w + r[i].first;
                    t = nt;
                    i--;
                }
            } else
            {
                if (last - r[i].first >= 0)
                {
                    res[i].first = r[i].second;
                    res[i].second.first = last - r[i].first;
                    res[i].second.second = t + r[i].first;
                    nt = max(nt, res[i].second.second + r[i].first);
                    last -= 2 * r[i].first;
                } else
                {
                    lr = 0;
                    last = -r[i].first;
                    t = nt;
                    i--;
                }
            }
        }
        if (t > l) puts("wa");
        for(int ddd =0; ddd<n;ddd++)
        {
            num[ddd].a=last+ddd;
            num[ddd].b=nt-ddd;
        }
        sort(res + 1, res + 1 + n);
           for(int ddd =0; ddd<n;ddd++)
        {
            num[ddd].a=last+ddd;
            num[ddd].b=nt-ddd;
        }
        printf("Case #%d:", ++cass);

        for (int i = 1; i <= n; i++)
            printf(" %d.0 %d.0", res[i].second.first, res[i].second.second);
        puts("");
           for(int ddd =0; ddd<n;ddd++)
        {
            num[ddd].a=last+ddd;
            num[ddd].b=nt-ddd;
        }
    }
    return 0;
}