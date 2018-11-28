#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

typedef long long s64;
typedef unsigned long long u64;

int a[8000];

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        int n; cin >> n;
        memset(a, 0, sizeof(a));
        int curr = 0;
        for (int c = 1; c <= n; c++) {
            for (int i = 0; i < c; i++) {
                while (a[curr] != 0) { curr++; if (curr == n) curr = 0; }
                if (i == c-1) break;
                curr++; if (curr == n) curr = 0;
            }
            a[curr] = c;
        }
        cin >> n;
        cout << "Case #" << t << ":";
        for (int i = 0; i < n; i++) {
            int x; cin >> x; x--;
            cout << " " << a[x];
        }
        cout << endl;
    }
    return 0;
}

