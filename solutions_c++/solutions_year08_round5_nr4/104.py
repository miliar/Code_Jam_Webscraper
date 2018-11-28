#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <map>
#include <bitset>
#include <cmath> 

#define FOR(i, a, b) for (int i=(int)(a); i<(int)(b); i++)
#define REP(i, n) for (int i=0; i<(int)(n); i++)
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pb push_back

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
typedef long long ll; 

bool bd[100][100];
int dp[100][100];

int main () {
    int T, cs=0;
    int i, j;
    cin >> T;
    while (T--) {
        int H, W, R;
        cin >> H >> W >> R;
        for (i=0; i<100; i++) {
            for (j=0; j<100; j++) {
                bd[i][j] = 0;
                dp[i][j] = 0;
            }
        }
        int r, c;
        for (i=0; i<R; i++) {
            cin >> r >> c;
            bd[r-1][c-1] = 1;
        }
        dp[0][0] = 1;
        for (i=0; i<H; i++) {
            for (j=0; j<W; j++) {
                if (bd[i][j]) continue;
                if (i-2 >= 0 && j-1 >= 0) {
                    dp[i][j] += dp[i-2][j-1];
                }
                if (i-1 >= 0 && j-2 >= 0) {
                    dp[i][j] += dp[i-1][j-2];
                }
                dp[i][j] %= 10007;
            }
        }

        cout << "Case #" << ++cs << ": " << dp[H-1][W-1] << endl;
    }
    return 0;
}
