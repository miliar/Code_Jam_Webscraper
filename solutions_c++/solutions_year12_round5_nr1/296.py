#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct bar {
    int p, l, i;
};

bool operator<(bar x, bar y) {
    return x.p > y.p || (x.p == y.p && x.i < y.i);
}



int main() {
    int num_cases;
    std::cin >> num_cases;
    for (int casenum = 1; casenum <= num_cases; ++casenum) {
        int n;
        cin >> n;

        vector<bar> pl;
        for (int i = 0; i < n; ++i) {
            bar foo;
            cin >> foo.l;
            pl.push_back(foo);
        }

        for (int i = 0; i < n; ++i) {
            cin >> pl[i].p;
            pl[i].i = i;
        }

        sort(pl.begin(), pl.end());



        cout << "Case #" << casenum << ":";
        for (int i = 0; i < n; ++i) {
            cout << " " << pl[i].i;
        }
        cout << endl;
    }
}
