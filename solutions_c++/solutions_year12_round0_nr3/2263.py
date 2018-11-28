#include <cstdio>
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

int update(const int x, const int B) {
    vector<int> curr;
    char s[10] = {};
    int len = 0;

    for (int i = x; i > 0; i /= 10) {
        s[len] = i % 10;
        len++;
    }
    reverse(s, s + len);

    int L[10] = {s[0]}, R[10] = {s[len - 1]};
    bool avi[10] = {(s[len - 1] != 0)};

    for (int i = 1; i < len; i++) {
        L[i] = L[i - 1] * 10 + s[i];
    }
    for (int i = 1, fac = 10; i < len; i++, fac *= 10) {
        R[i] = (s[len - 1 - i]) * fac + R[i - 1];
        if (s[len - 1 - i] != 0) avi[i] = true;
    }
    for (int i = 0, fac = 10; i < len; i++, fac *= 10) {
        if (!avi[len - 1 - i - 1]) continue;
        int val = R[len - 1 - i - 1] * fac + L[i];
        if (x < val && val <= B) curr.push_back(val);
    }
    sort(ALL(curr));

    return unique(ALL(curr)) - curr.begin();
}

int main() {
    int t, casN = 0;
    int A, B;

    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%d%d", &A, &B);
        int64 ans = 0LL;
        for (int i = B; i >= A; i--) {
            ans += update(i, B);
        }
        printf("Case #%d: %lld\n", ++casN, ans);
    }

    return 0;
}

