#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int a[1000];

int main()
{
    int i, j, k, tt;
    cin >> tt;
    for (int test = 1; test <= tt; test++) {
        long long t, ct = 0, tot = 0;
        int c, n, l;
        vector<int> lose;

        cin >> l >> t >> n >> c;

        for (i = 0; i < c; i++) cin >> a[i];

        for (i = 0; i < n; i++) {
            if (ct >= t) lose.push_back(a[i % c]);
            else if (ct + 2 * a[i % c] >= t) lose.push_back(a[i % c] - (t - ct) / 2);
            ct += 2 * a[i % c];
        }

        sort(lose.rbegin(), lose.rend());

        l = min(l, (int)lose.size());
        for (i = 0; i < l; i++) ct -= lose[i];

        cout << "Case #" << test << ": " << ct << endl;
    }
    return 0;
}
