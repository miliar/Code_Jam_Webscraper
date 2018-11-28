#include <cstdio>
#include <cstring>
#include <cassert>

typedef long long ll;

ll solve(int rides, int capacity, int num_groups, int groups[]) {
    /* num_fit[i] contains the number of groups who will fit if a ride started
     * here. */
    int num_groups_fit[1024];
    ll money_made[1024];
    for (int i = 0; i < num_groups; i++) {
        int num_people = 0;
        int j;
        for (j = 0; j < num_groups; j++) {
            int new_value = num_people + groups[(i+j)%num_groups];
            if (new_value > capacity)
                break;
            num_people = new_value;
        }
        num_groups_fit[i] = j;
        money_made[i] = num_people;
    }

    /* Now, start from the start until we get back to somewhere we've seen. */
    bool seen[1024];
    ll profit_to[1024];
    ll profit_at[1024];
    int pos = 0;
    int time[1024];
    ll total = 0;
    int num_rides = 0;
    memset(seen, 0, sizeof(seen));
    memset(profit_to, 0, sizeof(profit_at));
    memset(profit_at, 0, sizeof(profit_at));
    while (!seen[pos]) {
        seen[pos] = true;
        time[pos] = num_rides+1;
        fprintf(stderr, "At %d, adding %d\n", pos, money_made[pos]);
        profit_to[pos] = total;
        total += money_made[pos];
        profit_at[pos] = total;
        pos = (pos + num_groups_fit[pos]) % num_groups;
        num_rides++;

        if (num_rides == rides)
            return total;
    }
#if 1
    fprintf(stderr, "\nProfit at: ");
    for (int i = 0; i < num_groups; i++) {
        fprintf(stderr, "%lld ", profit_at[i]);
    }
    fprintf(stderr, "\n");
    for (int i = 0; i < num_groups; i++) {
        fprintf(stderr, "%d(%lld) ", num_groups_fit[i], money_made[i]);
    }
    fprintf(stderr, "\nCycle len: %d\n", num_rides);
    fprintf(stderr, "\nTotal: %lld\n", total);
#endif

    /* Didn't make it. See how many more rides we have to make. */
    total = total + (total - profit_at[pos]) * (rides / (num_rides - time[pos]-1));
    num_rides = rides - pos - (num_rides * (rides / num_rides));
    while (num_rides > 0) {
        total += money_made[pos];
        pos = (pos + num_groups_fit[pos]) % num_groups;
        num_rides--;
    }

    return total;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        unsigned int R, k, N;
        int groups[1024];
        scanf("%u%u%u", &R, &k, &N);
        for (int j = 0; j < N; j++) {
            scanf("%d", &groups[j]);
            assert(groups[j] <= k);
        }
        printf("Case #%d: %lld\n", i, solve(R, k, N, groups));
    }
}
