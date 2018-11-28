#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long double ld;
typedef long long ll;

const int Maxn = 205;
const ld Inf = ld(1000000000000LL);

int t, c, d;
pair <int, int> info[Maxn];
ld ans;

bool Enough(ld x)
{
     ld lst = -Inf;
     for (int i = 0; i < c; i++)
        for (int j = 0; j < info[i].second; j++) {
            if (lst + d > info[i].first)
               if (lst + d > info[i].first + x) return false;
               else lst += d;
            else lst = max(lst + d, info[i].first - x);
        }
     return true;
}

void Search(ld l, ld r)
{
     if (l + 1e-7 >= r) return;
     ld mid = (l + r) / ld(2);
     if (Enough(mid)) {
                      ans = mid;
                      Search(l, mid-1e-7);
     } else Search(mid+1e-7, r);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> c >> d;
        for (int i = 0; i < c; i++) cin >> info[i].first >> info[i].second;
        Search(0, Inf);
        cout << "Case #" << tc << ": " << fixed << setprecision(12) << ans << endl;
    }
    return 0;
}
