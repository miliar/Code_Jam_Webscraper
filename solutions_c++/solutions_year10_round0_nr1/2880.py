#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; i++)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; i--)
#define REP(i, n) for (int i(0), _n(n); i < _n; i++)
#define REPD(i, n) for (int i((n)-1); i >= 0; i--)
#define CLR(x, with) memset((x), with, sizeof(x))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline void getMax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline void getMin(T& a, T b) { if (b < a) a = b; }

typedef long long LL;
typedef unsigned long long ULL;

int N, K;

int Recur(int state, int power)
{
}

int gcd(int a, int b)
{
    if (b == 0) return a;
    else
        return gcd(b, a%b);
}

int main() {
    int tcases;
    int res;

    scanf("%d", &tcases);

    FOR(t, 1, tcases)
    {
        scanf("%d %d", &N, &K);

        int num = (1 << N)-1;

        printf("Case #%d: ",t);
        if (K == 0) printf("OFF\n");
        else if (K < num) printf("OFF\n");
        else if (K == num) printf("ON\n");
        else if (K > num)
        {
            K -= num; num += 1;
            if (K % num == 0) printf("ON\n"); else printf("OFF\n");
        }
        //printf("Case #%d: %d\n", t, res);
    }

    return 0;
}
