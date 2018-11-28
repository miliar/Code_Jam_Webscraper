#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <numeric>
#include <cctype>
#include <list>
#include <functional>
#include <stack>
#include <fstream>
#include <sstream>
#include <cstring>
#include <cstdlib>

#define size(c) (int)c.size()
using namespace std;

typedef pair<int, int> edge;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef map<string, int> msi;
typedef pair<int, int> pii;


int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, A1, A2, B1, B2;
    cin >> T;
    double gold = (sqrt(5.0) + 1) / 2;
    for (int t = 1; t <= T; ++ t) {
        cin >> A1 >> A2 >> B1 >> B2;
        long long ans = (long long) (A2 - A1 + 1) * (B2 - B1 + 1);
        for (int i = A1; i <= A2; i ++) {
            int minX = (int)(i * (gold - 1)) + 1;
            int maxX = (int)(i * gold);
            minX = max(minX, B1);
            maxX = min(maxX, B2);
            if (maxX - minX + 1 > 0) ans -= maxX - minX + 1;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
