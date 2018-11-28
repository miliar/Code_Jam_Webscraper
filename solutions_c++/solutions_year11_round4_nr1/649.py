#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define pb push_back
#define mp make_pair

int L, S, R;
int T;
int n;

vector<pair<int, int>> a;

bool Cmp1(pair<int, int> &p1, pair<int, int> &p2) {
    return p1.first < p2.first;
}

bool Cmp2(pair<int, int> &p1, pair<int, int> &p2) {
    return p2.first < p1.first;
}

bool Cmp3(pair<int, int> &p1, pair<int, int> &p2) {
    return (double)p1.first/p1.second < (double)p2.first/p2.second;
}

bool Cmp4(pair<int, int> &p1, pair<int, int> &p2) {
    return (double)p1.second/p1.first < (double)p2.second/p2.first;
}

double go(vector<pair<int, int>> &a) {
    double boost = R - S;
    double ans = 0;
    double rem = T;
    for(int i = 0; i < a.size(); ++i) {
        double v = a[i].first;
        double dst = a[i].second;

        double boostTime = min(dst / (v + boost), rem);

        ans += boostTime + (dst - (v + boost) * boostTime) / v;
        rem -= boostTime;
    }
    return ans;
}


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
        
        cin >> L >> S >> R >> T >> n;
        a.clear();
        int last = 0;
        for(int i = 0; i < n; ++i) {
            int l, r, w;
            cin >> l >> r >> w;
            if (l > last) a.pb(mp(S, l - last));
            a.pb(mp(S + w, r - l));
            last = r;
        }
        if (last < L) a.pb(mp(S, L - last));

        sort(a.begin(), a.end(), Cmp1);

        double res = go(a);

        sort(a.begin(), a.end(), Cmp2);
        res = min(res, go(a));

        sort(a.begin(), a.end(), Cmp3);
        res = min(res, go(a));

        sort(a.begin(), a.end(), Cmp4);
        res = min(res, go(a));

        printf("Case #%d: %.12lf\n", tc, res);
    }

    


    
    return 0;
}