#include <iostream>
#include <vector>
using namespace std;

/*bool stored[31][2] = {0};
int store[31][2] = {0};
int best(int total, bool surprising) {
    if (stored[total][int(surprising)]) return store[total][int(surprising)];
    for (int i = 10; i >= 0; --i)
        for (int j = i; j >= i-(surprising?1:2) && j >= 0; --j) {
            int k = total - i - j;
            if (k >= 0 && k <= 10 &&
                    max(abs(k-j),abs(k-i)) <= (surprising ? 1:2)) {
                stored[total][surprising]
                return i;
            }
        }
}
*/

int best_val[31][2];
void precalc() {
    for (int i = 0; i < 31; ++i)
        for (int j = 0; j < 2; ++j)
            best_val[i][j] = -1;
    for (int i = 0; i <= 10; ++i)
        for (int j = max(0,i-2); j <= i; ++j)
            for (int k = max(0,i-2); k <= j; ++k) {
                if (k == i-2) // surprising
                    best_val[i+j+k][1] = i;
                else
                    best_val[i+j+k][0] = i;
            }
}


void solve(int t) {
    int ans = 0;

    int N,S,P;
    cin >> N >> S >> P;
    for (int i = 0; i < N; ++i) {
        int val;
        cin >> val;
        if (best_val[val][0] >= P) {
            ++ans;
        } else if (best_val[val][1] >= P && S > 0) {
            ++ans;
            --S;
        }
    }

    cout << "Case #" << t << ": " << ans << "\n";
}


int main() {
    precalc();

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
        solve(t+1);

    return 0;
}
