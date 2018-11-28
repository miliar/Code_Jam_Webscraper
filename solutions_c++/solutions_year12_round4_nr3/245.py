#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <sstream>
#include <algorithm>
#include <ctime>
using namespace std;

//by Skyly

typedef long long int64;

#define SIZE(X) ((int)((X).size())) 
#define FOR(IT, X) for (__typeof((X).begin()) IT = (X).begin(); IT != (X).end(); ++IT)

template<typename T> string toStr(const T &x) { ostringstream os; os << x; return os.str(); }
template<typename T> void toMin(T &x, const T &y) { x = min(x, y); }
template<typename T> void toMax(T &x, const T &y) { x = max(x, y); }

int N;
int s[2005];
int h[2005];

int main() {
    int t;

    srand(time(NULL));

    scanf("%d", &t);
    for (int casN = 1; casN <= t; casN++) {
        scanf("%d", &N);
        for (int i = 1; i < N; i++) {
            scanf("%d", &s[i]);
        }
        for (int i = 1; i <= N; i++) {
            h[i] = 100000000;
        }
        bool flag;
        int cnt = 1;
        do {
            flag = false;
            for (int i = 1; i < N; i++) {
                for (int j = i + 1; j < s[i]; j++) {
                    int tmp = h[i] * (s[i] - j) + h[s[i]] * (j - i);
                    if (h[j] * (s[i] - i) >= tmp) {
                        h[j]--;
                        h[i]++;
                        h[s[i]]++;
                        flag = true;
                        break;
                    }
                }
                if (flag) break;
                for (int j = s[i] + 1; j <= N; j++) {
                    int tmp = h[i] * (j - s[i]) + h[j] * (s[i] - i);
                    if (h[s[i]] * (j - i) < tmp) {
                        h[j]--;
                        h[s[i]]++;
                        flag = true;
                    }
                }
                if (flag) break;
            }
            cnt++;
            if (cnt == 1000000) break;
        } while (flag);
        printf("Case #%d:", casN);
        if (cnt == 1000000) puts(" Impossible");
        else {
            for (int i = 1; i <= N; i++) {
                printf(" %d", h[i]);
            }
            putchar('\n');
        }
    }

    return 0;
}

