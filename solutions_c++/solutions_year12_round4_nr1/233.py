#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main(void) {
    int testCount;
    cin >> testCount;
    for (int testNo = 1; testNo <= testCount; ++testNo) {
        int n;
        cin >> n;
        vector<int> d(n), l(n);
        for (int i = 0; i < n; ++i) {
            cin >> d[i] >> l[i];
        }
        int D;
        cin >> D;
        set<int> vines;
        typedef pair<int, int> pii;
        set<pii> expi;
        vines.insert(0);
        expi.insert(pii(2*d[0], 0));
        for (int i = 1; i < n; ++i) {
            while (!expi.empty() && d[i] > expi.begin()->first) {
                vines.erase(expi.begin()->second);
                expi.erase(expi.begin());
            }
            if (!vines.empty()) {
                expi.insert(pii(d[i] + min(l[i], d[i] - d[*vines.begin()]), i));
                vines.insert(i);
            }
        }
        while (!expi.empty() && D > expi.begin()->first)
            expi.erase(expi.begin());
        cout << "Case #" << testNo << ": ";
        if (expi.empty())
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
    return 0;
}
