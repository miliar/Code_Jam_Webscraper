#include <cstdio>
using namespace std;

#define forn(i, n) for (int i=0; i<(n); ++i)

const int maxn = 1024;

int a[maxn];
long long sum[maxn], id[maxn];
int n, k, r;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tc;
    scanf("%d", &tc);

    for (int tt=1; tt<=tc; ++tt)
    {
        scanf("%d %d %d", &r, &k, &n);
        forn (i, n) sum[i] = 0, id[i] = -1;
        forn (i, n) scanf("%d", a+i);

        long long res = 0;

        int x = 0, j;
        id[x] = 0;
        int period = -1;
        long long psum = 0;
        for (j=1; r>0; --r, ++j)
        {
            int load = 0;
            forn (i, n)
            {               
                if (load+a[x] > k) break;
                load += a[x++];
                x %= n;
            }           
            res += load;
            if (id[x]!=-1)
            {
                psum = load;
                period = j-id[x];
                forn (q, n) if (id[q] > id[x]) psum += sum[q];
                --r;
                break;
            }
            id[x] = j;
            sum[x] = load;
        }
        if (period != -1)
        {
            res += psum*(r/period);
            r %= period;
            for (; r>0; --r)
            {
                int load = 0;
                forn (i, n)
                {                   
                    if (load+a[x] > k) break;
                    load += a[x++];
                    x %= n;
                }
                res += load;
            }
        }

        printf("Case #%d: %I64d\n", tt, res);


    }

    return 0;
}
