#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int t, i;
    cin >> t;
    for(int c = 1; c <= t; c++) {
        int n, s, p;
        vector <int> totals;
        cin >> n >> s >> p;
        for(i = 0; i < n; i++) {
            totals.push_back(0);
            cin >> totals[i];
        }
        sort(totals.begin(), totals.end());
        int lower = 3 * p - 2 * min(p, 2);
        for(i = 0; i < n && totals[i] < lower; i++);
        int ans = 0;
        ans += min(n - i, s);
        i += s;
        lower = 3 * p - 2 * min(p, 1);
        for(; i < n && totals[i] < lower; i++);
        ans += max(n - i, 0);
        cout << "Case #" << c << ": " << ans << endl;
    }
    return 0;
}