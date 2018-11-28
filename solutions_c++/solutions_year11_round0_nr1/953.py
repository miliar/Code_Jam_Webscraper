#include <cstdio>
#include <iostream>
#include <algorithm>

#define rep(i,n) for (int i = 0; i < n; i++)

using namespace std;

char r[110];
int p[110];
int rpos[2];

int main() {
    int T, N;
    cin >> T;
    rep(t,T) {
        cin >> N;
        rep(i,N) {
            cin >> r[i] >> p[i];
        }

        int res = 0;
        int bonus = 0;
        rpos[0] = rpos[1] = 1;

        rep(i,N) {
            int rind = (r[i] == 'O');
            int tim = abs(p[i] - rpos[rind]) + 1;

            if (i && r[i-1] != r[i]) {
                tim = max(tim - bonus, 1);
                bonus = 0;
            }

            bonus += tim;
            res += tim;
            rpos[rind] = p[i];
        }

        cout << "Case #" << t+1 << ": " << res << endl;
    }
}

