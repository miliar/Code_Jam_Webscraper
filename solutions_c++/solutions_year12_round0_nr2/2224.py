#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

//by Skyly

typedef long long int64;
typedef vector<int> vint;

#define SIZE(X) ((int)((X).size())) 
#define ALL(X) (X).begin(), (X).end()
#define FOR(IT, X) for (__typeof((X).begin()) IT = (X).begin(); IT != (X).end(); ++IT)

template<typename T> string toStr(const T &x) { ostringstream os; os << x; return os.str(); }
template<typename T> void toMin(T &x, const T &y) { x = min(x, y); }
template<typename T> void toMax(T &x, const T &y) { x = max(x, y); }

int N, S, P;
int s[105];
int dp[105][105];

int main() {
    int t, casN = 0;
    int x;

    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%d%d%d", &N, &S, &P);
        for (int i = 1; i <= N; i++) {
            scanf("%d", &s[i]);
        }
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= i; j++) {
                if (s[i] % 3 == 0) {
                    x = s[i] / 3;
                    toMax(dp[i][j], dp[i - 1][j] + (x >= P ? 1 : 0));//(0, 0, 0)
                    x--;
                    if (x >= 0 && j > 0) toMax(dp[i][j], dp[i - 1][j - 1] + (x + 2 >= P ? 1 : 0));//(0, 1, 2)
                } else if (s[i] % 3 == 1) {
                    x = s[i] / 3;
                    toMax(dp[i][j], dp[i - 1][j] + (x + 1 >= P ? 1 : 0));//(0, 0, 1)
                    x--;
                    if (x >= 0 && j > 0) toMax(dp[i][j], dp[i - 1][j - 1] + (x + 2 >= P ? 1 : 0));//(0, 2, 2)
                } else if (s[i] % 3 == 2) {
                    x = s[i] / 3;
                    toMax(dp[i][j], dp[i - 1][j] + (x + 1 >= P ? 1 : 0));//(0, 1, 1)
                    if (j > 0) toMax(dp[i][j], dp[i - 1][j - 1] + (x + 2 >= P ? 1 : 0));//(0, 0, 2)
                }
            }
        }
        printf("Case #%d: %d\n", ++casN, dp[N][S]);
    }

    return 0;
}

