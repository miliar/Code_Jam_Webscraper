#include <cstdio>
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long double ld;

const int Maxn = 3000;

struct segment {
       int b, e;
       int w;
       public:
              segment(int b, int e, int w): b(b), e(e), w(w) {}
};

int T, x, s, r, n;
ld t;
ld ans;
vector <segment> torun;

bool Less(const segment &a, const segment &b)
{
     return a.w < b.w;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cin >> x >> s >> r >> t >> n;
        int b, e, w, lst = 0;
        torun.clear();
        for (int i = 0; i < n; i++) {
            cin >> b >> e >> w;
            if (lst < b) torun.push_back(segment(lst, b, 0));
            torun.push_back(segment(b, e, w));
            lst = e;
        }
        if (lst < x) torun.push_back(segment(lst, x, 0));
        sort(torun.begin(), torun.end(), Less);
        ans = 0;
        for (int i = 0; i < torun.size(); i++)
           if (t * (torun[i].w + r) >= torun[i].e - torun[i].b) {
                 ld usedtime = ld(torun[i].e - torun[i].b) / ld(torun[i].w + r);
                 ans += usedtime;
                 t -= usedtime;
           } else {
                  ld usedtime = t; t = 0;
                  ld leftdist = torun[i].e - torun[i].b - usedtime * ld(torun[i].w + r);
                  ans += usedtime + leftdist / ld(torun[i].w + s);
           }
        cout << "Case #" << tc << ": " << fixed << setprecision(9) << ans << endl;
    }
    return 0;
}
