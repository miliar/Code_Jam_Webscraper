// g++ -Wall -O2

#include <vector>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    srand48(0x9876543CL);
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        fprintf(stderr, "Case #%d\n", testcase);
        int N, W, L;
        scanf("%d%d%d", &N, &W, &L);
        vector<pair<int, int> > r(N);
        for (int i = 0; i < N; ++i)
        {
            scanf("%d", &r[i].first);
            r[i].second = i;
        }
        sort(r.begin(), r.end(), greater<pair<int, int> >());
        vector<int> perm(N);
        for (int i = 0; i < N; ++i)
            perm[r[i].second] = i;
        vector<int> x(N);
        vector<int> y(N);
        for (int i = 0; i < N; ++i)
        {
            while (true)
            {
                int x1 = (int)(drand48() * (W + 1));
                int y1 = (int)(drand48() * (L + 1));
                bool good = true;
                for (int j = 0; j < i; ++j)
                {
                    int rsum = r[i].first + r[j].first;
                    if (x1 - x[j] > -rsum && x1 - x[j] < rsum && y1 - y[j] > -rsum && y1 - y[j] < rsum)
                    {
                        good = false;
                        break;
                    }
                }
                if (good)
                {
                    x[i] = x1;
                    y[i] = y1;
                    break;
                }
            }
        }
        printf("Case #%d:", testcase);
        for (int i = 0; i < N; ++i)
            printf(" %d %d", x[perm[i]], y[perm[i]]);
        putchar('\n');
    }
    return 0;
}
