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

struct Circle {
    double x, y, r;
    Circle() {}
    Circle(double _x, double _y, double _r): x(_x), y(_y), r(_r) {}
};

inline bool intersect(const Circle &A, const Circle &B) {
    return (A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y) < (A.r + B.r) * (A.r + B.r);
}

int main() {
    srand(time(NULL));

    int t;

    scanf("%d", &t);
    for (int casN = 1; casN <= t; casN++) {
        int N, X, Y;
        int r[1005];
        Circle c[1005];

        scanf("%d%d%d", &N, &X, &Y);
        for (int i = 0; i < N; i++) {
            scanf("%d", &r[i]);
        }
        printf("Case #%d:", casN);
        for (int i = 0; i < N; i++) {
            double x, y;
            bool flag;
            do {
                x = (double)(rand() % (X * 10)) / 10.0;
                y = (double)(rand() % (Y * 10)) / 10.0;
                c[i] = Circle(x, y, (double)r[i]);
                flag = false;
                for (int j = 0; j < i; j++) {
                    if (intersect(c[i], c[j])) flag = true;
                }
            } while (flag);
            printf(" %f %f", x, y);
        }
        putchar('\n');
    }

    return 0;
}

