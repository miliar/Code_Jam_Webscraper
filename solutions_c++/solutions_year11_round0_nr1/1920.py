#include <iostream>

using namespace std;

char    cs[105];
int     is[105];

#define ABS(x) (((x) >= 0) ? x : -(x)) 

int
solve(int n) {
    int     pos[2];
    int     pinc[2];
    int     who, other, i, diff, ans = 0;

    pos[0] = pos[1] = 1;
    pinc[0] = pinc[1] = 0;
    for (i=0;i<n;++i) {
        who = (cs[i] == 'O' ? 0 : 1);
        other = 1 - who;
        diff = ABS(is[i] - pos[who]);
        pinc[who] = min(pinc[who], diff);
        ans += diff - pinc[who] + 1;
        pinc[other] += diff - pinc[who] + 1;
        pinc[who] = 0;
        pos[who] = is[i];
    }

    return ans;
}

int main(void) {
    int     t, n, i, j;

    cin >> t;

    for (i=0;i<t;++i) {
        cin >> n;
        for (j=0;j<n;++j) {
            cin >> cs[j] >> is[j];
        }
        cout << "Case #" << (i+1) << ": " << solve(n) << endl;
    }

    return 0;
}
