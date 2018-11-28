#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long ll;
// Utilities
#define S(N) scanf("%d", &N)
#define SS(N) scanf("%s", N)
#define FOR(A,B,C) for(int A=B;A<C;++A)
#define RFOR(A,B,C) for(int A=B;A>=C;--A)
#define MEM(A,B) memset(A,B,sizeof(A))
#define MAX(A,B) ((A > B) ? A : B)
#define MIN(A,B) ((A < B) ? A : B)
// Debugging
bool DBG;
#define debug(args...) dbg(),args
struct dbg { template<typename T> dbg& operator , (const T& v) { if(DBG)
cerr << v << " "; return *this; } ~dbg() { if (DBG) cerr << endl; } };

#define MOD 100000007
#define LIM 1000000000

int main (int argc, char *argv[]) {
    DBG = (argc > 1 && *argv[1] != '0'); // Set debug on if required
    int t;
    scanf("%d\n", &t);
    FOR(k, 0, t) {
        int n, s, p, score, num = 0, max;
        S(n); S(s); S(p);
        FOR(i, 0, n) {
            S(score);
            if(score==0) {
                if(p==0) num++;
                continue;
            }
            max = (score/3) + ((score%3) ? 1 : 0);
            if(max >= p || ((score%3) != 1 && max+1 >= p && s-- > 0))
                num++;
        }
        printf("Case #%d: %d\n", k+1, num);
    }
    return 0;
}
