#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int solve()
{
    int n, bpos, opos, bwait, owait, time = 0;
    cin >> n;
    bpos = opos = 1;
    bwait = owait = 0;
    for (int i = 0; i < n; i++) {
        char r;
        int p, t;
        cin >> r >> p;
        if (r == 'B') {
            t = max(0, abs(bpos - p) - bwait);
            time += t + 1;
            owait += t + 1;
            bwait = 0;
            bpos = p;
        }
        else { // r == 'O'
            t = max(0, abs(opos - p) - owait);
            time += t + 1;
            bwait += t + 1;
            owait = 0;
            opos = p;
        }
    }
    return time;
}

int main()
{
    int t; // number of tests
    cin >> t;
    for (int i = 0; i < t; i++) {
        int answer = solve();
        cout << "Case #" << (i + 1) << ": " << answer << endl;
    }
    return 0;
}
