#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

int set[1001];
bool seen[1001];

bool is_prime[1001];

void solve()
{
    int P, A, B;
    scanf("%d %d %d", &A, &B, &P);

    for (int i = A; i <= B; i++)
        set[i] = i;

    for (int i = A; i <= B; i++)
    for (int j = i + 1; j <= B; j++) {
        for (int div = P; div <= B; div++) {
            if (is_prime[div] && i % div == 0 && j % div == 0) {
                for (int k = A; k <= B; k++) {
                    if (set[k] == set[j])
                        set[k] = set[i];
                }
                break;
            }
        }
    }

    for (int i = A; i <= B; i++)
        seen[i] = false;

    for (int i = A; i <= B; i++)
        seen[set[i]] = true;

    int ans = 0;
    for (int i = A; i <= B; i++)
        ans += (seen[i]) ? 1 : 0;
    
    printf("%d", ans);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i < 1001; i++)
        is_prime[i] = true;
    for (int i = 2; i < 1001; i++) {
        if (is_prime[i]) {
            for (int j = i + i; j < 1001; j += i)
                is_prime[j] = false;
        }
    }

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

