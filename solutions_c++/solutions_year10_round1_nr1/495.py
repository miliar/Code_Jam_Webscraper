#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x) {
    return x*x;
}

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int t, n, k;

void rotate(char board[55][55]) {
    for (int i = 0; i < n; i++) {
        int r = n - 1;
        while (r >= 0 && board[i][r] != '.') --r;
        int l = r - 1;
        while (l >= 0) {
            if (board[i][l] == '.') {
                --l;
                continue;
            }
            board[i][r] = board[i][l];
            board[i][l] = '.';
            --r;
            --l;
        }
    }
}

string check(char board[55][55]) {
    int wr = 0, wb = 0;
    int dp[55][55][4] = {0};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
			dp[i][j][0]=dp[i][j][1]=dp[i][j][2]=dp[i][j][3]=1;
            if (j > 0) dp[i][j][0] = (board[i][j] == board[i][j - 1]) ? dp[i][j - 1][0] + 1 : 1;
            if (i > 0) dp[i][j][1] = (board[i][j] == board[i - 1][j]) ? dp[i - 1][j][1] + 1 : 1;
            if (i > 0 && j > 0) dp[i][j][2] = (board[i][j] == board[i - 1][j - 1]) ? dp[i - 1][j - 1][2] + 1 : 1;
            if (i > 0 && j < n - 1) dp[i][j][3] = (board[i][j] == board[i - 1][j + 1]) ? dp[i - 1][j + 1][3] + 1 : 1;
            for (int c = 0; c < 4; c++) {
                if (dp[i][j][c] == k) {
                    if (board[i][j] == 'R') wr = 1;
                    else if(board[i][j]=='B') wb = 1;
                }
            }
        }
    }
    if (wr && wb) return "Both";
    else if (wr) return "Red";
    else if (wb) return "Blue";
    else return "Neither";
}

int main(int argc, char** argv) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int ti = 1; ti <= t; ++ti) {
        scanf("%d%d", &n, &k);
        char board[55][55] = {0};
        for (int i = 0; i < n; i++) {
            scanf("%s", board[i]);
        }
        rotate(board);
        printf("Case #%d: ", ti);
        cout << check(board) << endl;
    }
    return (EXIT_SUCCESS);
}

