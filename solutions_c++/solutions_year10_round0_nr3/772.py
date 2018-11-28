#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int g[2005];
int l[1005];
int c[1005];

int main( int argc, char* argv[] )
{
    FILE *fr = fopen("C-large.in", "r");
    FILE *fw = fopen("C-large.out", "w");

    int T;
    fscanf(fr, "%d", &T);

    for(int t = 1; t <= T; ++t)
    {
        int R, k, N;

        fscanf(fr, "%d %d %d", &R, &k, &N);

        for(int i = 0; i < N; ++i)
        {
            fscanf(fr, "%d", &g[i]);

            g[N + i] = g[i];
        }

        int ib = 0, ie = -1;

        memset(l, 0, sizeof(int) * N);

        while(ib < N && ie < (N << 1))
        {
            if(l[ib] < k && l[ib] + g[ie + 1] <= k && ie - ib + 1 < N)
            {
                l[ib] += g[++ie];
            }
            else
            {
                l[ib + 1] = l[ib] - g[ib];
                c[ib] = l[ib];
                l[ib] = ie - ib + 1;
                ++ib;
            }
        }

        unsigned long long sum = 0;
        int ptr = 0;

        for(int r = 0; r < R; ++r)
        {
            sum += c[ptr];
            ptr = (ptr + l[ptr]) % N;
        }

        fprintf(fw, "Case #%d: %lld\n", t, sum);
    }

    fclose(fr);
    fclose(fw);

    return 0;
}