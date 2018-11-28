#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

typedef long long int64;

int k;
int len;
char s[50001];

int perm[16];
bool used[16];

int best;

void go()
{
    char prev = '\0';
    int n = 0;

    for (int i = 0; i < len; i += k) {
        for (int j = 0; j < k; j++) {
            char next = s[i + perm[j]];
            if (next != prev)
                n++;
            prev = next;
        }
    }

    best = std::min(best, n);
}

void gen(int pos)
{
    if (pos == k)
        go();
    else
        for (int i = 0; i < k; i++)
            if (used[i])
                continue;
            else {
                used[i] = true;
                perm[pos] = i;
                gen(pos+1);
                used[i] = false;
            }
}

void solve()
{
    scanf("%d%s", &k, s);
    len = strlen(s);

    best = len + 1;
    gen(0);
    printf("%d", best);
}

int main()
{
    int n_cases;
    scanf("%d", &n_cases);

    for (int i = 0; i < n_cases; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}

