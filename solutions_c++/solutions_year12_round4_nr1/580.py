#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

//by Skyly

typedef long long int64;

#define SIZE(X) ((int)((X).size())) 
#define FOR(IT, X) for (__typeof((X).begin()) IT = (X).begin(); IT != (X).end(); ++IT)

template<typename T> string toStr(const T &x) { ostringstream os; os << x; return os.str(); }
template<typename T> void toMin(T &x, const T &y) { x = min(x, y); }
template<typename T> void toMax(T &x, const T &y) { x = max(x, y); }

const int MAXN = 10005;
const int INF = 1000000005;

int N, D;
int d[MAXN], l[MAXN];
int maxT[MAXN];

bool getAns;

void solve(int id, int y) {
    if (y >= D - d[id]) {
        //cerr << id << ", " << y << endl;
        getAns = true;
    }
    int tmp;
    for (int i = id + 1; i <= N; i++) {
        if (y < d[i] - d[id]) break;
        tmp = min(l[i], d[i] - d[id]);
        if (maxT[i] < tmp) {
            maxT[i] = tmp;
            solve(i, tmp);
            if (getAns) break;
        }
    }
}

int main() {
    int t;

    scanf("%d", &t);
    for (int casN = 1; casN <= t; casN++) {
        scanf("%d", &N);
        for (int i = 1; i <= N; i++) {
            scanf("%d%d", &d[i], &l[i]);
            maxT[i] = -1;
        }
        scanf("%d", &D);
        getAns = false;
        solve(1, d[1]);
        printf("Case #%d: %s\n", casN, getAns ? "YES" : "NO");
    }

    return 0;
}

