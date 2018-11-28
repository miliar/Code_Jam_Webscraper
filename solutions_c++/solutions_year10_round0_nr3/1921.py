#include <cstdio>
#include <utility>
#include <cassert>
#include <cstring>
using namespace std;

int g[1001];
long long g_sum[1001];
pair<long long, long long> runs[1001];
int next_run[1001];

inline long long g_sum_range(int lo, int len, int n) __attribute__((always_inline));
inline void init_run(int i, int k, int n) __attribute__((always_inline));

// [i, i + len % n)
inline long long g_sum_range(int lo, int len, int n)
{
    int hi = (len + lo);
    if (hi >= n) hi -= n;

    if (lo < hi)
        return g_sum[hi] - g_sum[lo];
    return (g_sum[n] - g_sum[lo]) + g_sum[hi];
}

inline void init_run(int i, int k, int n)
{
    int high = n;
    int low = 1, mid;
    long long s;

    // p(s) = s <= k
    // ~p(s) = ~(s <= k) = s > k // using this
    //find the last s such that ~(~p(s))

    while(low < high) {
        mid = low + (high - low + 1) / 2;
        s = g_sum_range(i, mid, n);

        if (s > k)
            high = mid - 1;
        else
            low = mid;
    }
    long long low_s = g_sum_range(i, low, n);
    assert(!(low_s > k)); // ~p(s) won't be true for every s

    runs[i].first = low;
    runs[i].second = low_s;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int caso = 1; caso <= t; caso++) {
        int r, k, n;
        scanf("%d %d %d", &r, &k, &n);
        for(int i = 0; i < n; i++)
            scanf("%d", &g[i]);

        g_sum[0] = 0;
        for(int i = 0; i < n; i++)
            g_sum[i + 1] = g_sum[i] + g[i];

        for(int i = 0; i < n; i++)
            init_run(i, k, n);

        /*for(int i = 0; i < n; i++)
            printf("[%d, %d], ", runs[i].first, runs[i].second);
        puts("");*/

        long long money = 0;
        int run = 0, R = r;
        // simulating! If it finds a cycle it know what to do ;)
        memset(next_run, -1, (n + 1) * sizeof(next_run[0]));
        money = 0, run = 0;
        while(r > 0) {
            if (next_run[run] != -1) {
                int cycle_len = 1;
                long long cycle_total_people = runs[run].second;
                int parent_run = next_run[run];
                while(parent_run != run) {
                    ++cycle_len;
                    cycle_total_people += runs[parent_run].second;
                    parent_run = next_run[parent_run];
                }
                //printf("cur_money = %d, cycle  %d, len %d => (*%d) = %d / %d\n", money,
                //        cycle_total_people, cycle_len, (int) (r / cycle_len), r, cycle_len);
                int cycles = r / cycle_len;
                r -= cycles * cycle_len;
                //printf("r -= cycles * cycle_len -= %d * %d = %d\n", r, cycles, cycle_len, r - cycles * cycle_len);
                money += (long long) cycles * cycle_total_people;
                break;
            }
            money += runs[run].second;

            int the_next_run = run + runs[run].first; // % n
            if (the_next_run >= n) the_next_run -= n;

            next_run[run] = the_next_run;
            run = the_next_run;

            r--;
        }

        // continuing simulations (without cycle detection)
        while(r > 0) {
            money += runs[run].second;
            run += runs[run].first;
            if (run >= n) run -= n;
            r--;
        }

#ifdef TEST
        // testing
        long long result_for_sure = 0;
        run = 0;
        while(R > 0) {
            result_for_sure += runs[run].second;
            run += runs[run].first;
            if (run >= n) run -= n;
            R--;
        }
        //printf("%d %d\n", result_for_sure, money);
        assert(result_for_sure == money);
#endif
        printf("Case #%d: %lld\n", caso, money);
    }
    return 0;
}

