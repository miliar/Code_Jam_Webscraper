#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

int n;
vi nextH;
vvi highestFrom;
vi ans;

bool solve(int l, int r, int h) {
    ans[r] = h;
    if (l == r)
        return (highestFrom[r].size() == 0);
    int cl = l;
    for each (int f in highestFrom[r]) {
        if (f < cl)
            return false;
        if (!solve(cl, f, h - 1))
            return false;
        for (int i = cl; i < f; i++)
            ans[i] -= (f - i);
        cl = f + 1;
    }
    return true;
}

int main(void) {
    int testCount;
    cin >> testCount;
    for (int testNo = 1; testNo <= testCount; ++testNo) {
        cin >> n;
        nextH.assign(n, 0);
        highestFrom.assign(n, vi());
        ans.assign(n, -1);
        for (int i =0; i < n-1; ++i) {
            cin >> nextH[i];
            --nextH[i];
            highestFrom[nextH[i]].push_back(i);
        }
        cout << "Case #" << testNo << ":";
        if (!solve(0, n-1, 0)) {
            cout << " Impossible";
        } else {
            int minel = *min_element(ans.begin(), ans.end());
            for (int i = 0; i < n; ++i)
                cout << " " << ans[i] - minel;
        }
        cout << endl;
    }
    return 0;
}
