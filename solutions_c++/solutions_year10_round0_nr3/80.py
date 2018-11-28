#include <cstdio>
#include <numeric>
#include <cstring>
#include <algorithm>

const char input_file[] = "C-large.in";
const char output_file[] = "c.large.out";

typedef long long I64;

const int N = 1000;

int id[N];
I64 group[N];
I64 memo[N][2];
int r, k, n;

void solve() {
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int ti = 1; ti <= t; ++ti) {
        scanf("%d%d%d", &r, &k, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lld", group + i);
        }
        for (int i = 0; i < n; ++i) {
            id[i] = i;
        }
        memset(memo, 0, sizeof(memo));
        I64 money = 0;
        bool use_memo = true;
        for (int i = 0; i < r; ++i) {
            int first = 0;
            I64 sum = 0;
            for (; first < n; ++first) {
                if (sum + group[first] > k) {
                    break;
                }
                sum += group[first];
            }
            money += sum;
            first %= n;
            std::rotate(group, group + first, group + n);
            std::rotate(id, id + first, id + n);
            if (use_memo) {
                if (memo[id[0]][0]) {
                    int cycle = i + 1 - memo[id[0]][0];
                    I64 cycle_money = money - memo[id[0]][1];
                    int left = r - i - 1;
                    money += left / cycle * cycle_money;
                    r = left % cycle;
                    i = -1;
                    use_memo = false;
                } else {
                    memo[id[0]][0] = i + 1;
                    memo[id[0]][1] = money;
                }
            }
        }
        printf("Case #%d: %lld\n", ti, money);
    }
}
int main() {
    solve();
    return 0;
}

