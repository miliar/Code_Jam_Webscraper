#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

typedef long long ll;
const double eps = 1e-8;

const int N = 500;
char s[N + 5][N + 5];
int x[N][N];

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int R, C, D;
        cin >> R >> C >> D;
        rep(i, R) {
            scanf("%s", s[i]);
            rep(j, C)
                x[i][j] = s[i][j] - '0';
        }

        int res = -1;
        rep(i, R) rep(j, C) {

            for(int k = 2; i + k < R && j + k < C; k++) {

                double mi = i + k / 2.0;
                double mj = j + k / 2.0;

                double sumx = 0, sumy = 0;

                for(int ii = i; ii <= i + k; ii++)
                    for(int jj = j; jj <= j + k; jj++)
                        if((ii != i || jj != j) &&
                           (ii != i + k || jj != j) &&
                           (ii != i + k || jj != j + k) &&
                           (ii != i || jj != j + k)) {

                            sumx += (ii - mi) * (x[ii][jj]);
                            sumy += (jj - mj) * (x[ii][jj]);

                        }

                if(abs(sumx) < eps && abs(sumy) < eps) {
                    res = max(res, k);
                }

            }
        }

        if(res + 1 < 3) printf("IMPOSSIBLE\n");
        else cout << res + 1 << endl;

    }
}
