#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

const int MAX_P = 1000005;

int d, k;
int v[16];
bool isPrime[MAX_P];
int limit, p;

int pow(int base, int exp) {
    if (exp == 0) return 1;

    long long sol = pow(base, exp / 2);
    sol = (sol * sol) % p;
    if (exp & 1) sol = (sol * base) % p;

    return (int)sol;
}

int getSol() {
    for (int i = 1; i <= k; ++i)
        if (v[i] >= p) return -1;

    if (v[1] == v[2]) {
        bool ok = true;
        for (int i = 3; i <= k; ++i)
            ok &= v[i] == v[1];
        if (!ok) return -1;
        else return v[1];
    }

    if (k == 2) return -1;

    long long a = ((v[2] - v[3] + p) % p) * pow((v[1] - v[2] + p) % p, p - 2);
    long long b = (v[2] - a * v[1] % p + p) % p;

    for (int i = 2; i <= k; ++i)
        if (((a * v[i - 1] + b) % p) != v[i])
            return -1;
    return (a * v[k] + b) % p;
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    memset(isPrime, true, sizeof(isPrime));
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i * i < MAX_P; ++i)
        if (isPrime[i])
            for (int j = i * i; j < MAX_P; j += i)
                isPrime[j] = false;

    int t; scanf("%d", &t);
    for (int test_no = 1; test_no <= t; ++test_no) {
        scanf("%d %d", &d, &k);
        for (int i = 1; i <= k; ++i)
            scanf("%d", &v[i]);

        limit = 10;
        for (int i = 2; i <= d; ++i)
            limit *= 10;

        if (k == 1) {
            printf("Case #%d: I don't know.\n", test_no);
            continue;
        }

        set<int> sol;
        for (p = 2; p <= limit; ++p)
            if (isPrime[p]) {
                int val = getSol();

                //printf("%d %d\n", p, val);

                if (val != -1)
                    sol.insert(val);
            }

        if (sol.size() != 1) {
            printf("Case #%d: I don't know.\n", test_no);
        } else {
            printf("Case #%d: %d\n", test_no, *(sol.begin()));
        }
    }
}
