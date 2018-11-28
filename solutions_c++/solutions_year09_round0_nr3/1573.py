#include<algorithm>
#include<cmath>
#include<iostream>
#include<list>
#include<cstring>
#include<cstdio>
#include<climits>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<vector>
using namespace std;

template<class A, class B> void conv_(A& x, B& y) { stringstream s; s << x; s >> y; }

typedef unsigned int uint;
typedef unsigned long long int ullong;
#define for_(i, a, b) for(int i=(a);i<(b);++i)
#define set_(a, n) memset(a, n, sizeof a)

string cj = "welcome to code jam";
int cj_sz = cj.length();

int main(void) {
    int n; cin >> n;cin.get();

    for_(t, 1, n+1) {
        string l; getline(cin, l);
        int l_sz = l.length();

        int dp[l_sz+1][cj_sz+1];
        set_(dp, 0);

        for (int i = l_sz; i >= 0; --i) {
            for (int j = cj_sz; j >= 0; --j) {

                if (i == l_sz || j == cj_sz) {
                    dp[i][j] = (j == cj_sz);
                    continue;
                }

                if (l[i] != cj[j]) {
                    dp[i][j] = dp[i+1][j];
                }
                else {
                    dp[i][j] = (dp[i+1][j+1] + dp[i+1][j]) % 10000;
                }

            }
        }

        cout << "Case #" << t << ": ";
        printf("%04d\n", dp[0][0]);
    }

    return 0;
}
