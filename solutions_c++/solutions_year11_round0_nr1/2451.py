#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <string>
#include <ctime>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <cstring>

#define pii pair <int, int>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back

const int INF = (1<<31)-1;
const double EPS = 1E-9;
const double PI = acos(-1);

using namespace std;

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t, n, a, orange, blue, timeorange, timeblue, res;
    char c;
    cin >> t;
    for(int q=1; q<=t; ++q) {
        cin >> n;
        res = 0;
        orange = 1;
        blue = 1;
        timeorange = 0; timeblue = 0;
        for(int i=0; i<n; ++i) {
            cin >> c >> a;
            if(c == 'O') {
                res += max(0, abs(a-orange)-timeorange) + 1;
                timeblue += max(0, abs(a-orange)-timeorange) + 1;
                orange = a;
                timeorange = 0;
            }
            else {
                res += max(0, abs(a-blue)-timeblue) + 1;
                timeorange += max(0, abs(a-blue)-timeblue) + 1;
                blue = a;
                timeblue = 0;
            }
        }
        cout << "Case #" << q << ": " << res << endl;
    }

    return 0;
}
