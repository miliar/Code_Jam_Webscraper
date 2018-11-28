#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

using namespace std;

typedef long long li;
typedef long double ld;
//typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-6;

struct pt{
      ld X, Y, Z;
};

pt getCenter(vector<pt>& p){
    pt ans = {0.0, 0.0, 0.0};
    forn(i, sz(p)){
        ans.X += p[i].X;
        ans.Y += p[i].Y;
        ans.Z += p[i].Z;
    }
    ans.X /= sz(p);
    ans.Y /= sz(p);
    ans.Z /= sz(p);
    return ans;
}

inline ld dist(pt& a, pt& b){
    return sqrtl(sqr(a.X - b.X) + sqr(a.Y - b.Y) + sqr(a.Z - b.Z));
}
pt uni = {0.0, 0.0, 0.0};
ld getMin(ld lf, ld rg, vector<pt>& a, vector<pt>& v){
    vector<pt> tmp(sz(a));
    
    forn(Q, 300){
        ld d = (rg - lf) / 3.0;
        ld mlf = lf + d;
        ld mrg = rg - d;
        
        forn(i, sz(a)){
            tmp[i].X = a[i].X + v[i].X * mlf;
            tmp[i].Y = a[i].Y + v[i].Y * mlf;
            tmp[i].Z = a[i].Z + v[i].Z * mlf;
        }

        ld flf = dist(uni, getCenter(tmp));

        forn(i, sz(a)){
            tmp[i].X = a[i].X + v[i].X * mrg;
            tmp[i].Y = a[i].Y + v[i].Y * mrg;
            tmp[i].Z = a[i].Z + v[i].Z * mrg;
        }

        ld frg = dist(uni, getCenter(tmp));

        if(flf < frg) 
            rg = mrg;
        else
            lf = mlf;
    }
    return lf;
}

ld getDis(ld ans, vector<pt>& a, vector<pt>& v){
    vector<pt> tmp(sz(a));
    forn(i, sz(a)){
        tmp[i].X = a[i].X + ans * v[i].X;
        tmp[i].Y = a[i].Y + ans * v[i].Y;
        tmp[i].Z = a[i].Z + ans * v[i].Z;
    }
    return dist(uni, getCenter(tmp));
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T;
    cin >> T;
    cout.precision(10);
    for1(Q, T){
        printf("Case #%d: ", Q);
        int n;
        scanf("%d", &n);
        vector<pt> a(n);
        vector<pt> v(n);
        forn(i, n){
            cin >> a[i].X >> a[i].Y >> a[i].Z;
            cin >> v[i].X >> v[i].Y >> v[i].Z;
        }

        ld lf = 0.0;
        ld D = 1000.0;
        ld rg = 0.0;

        ld ans = getMin(lf, rg, a, v);
        ld d = getDis(ans, a, v);
        
        rg = D;
        forn(i, 100){
            ld pans = getMin(lf, rg, a, v);
            ld pd = getDis(pans, a, v);

            if(fabs(d - pd) < EPS){
                if(pans < ans){
                    d = pd;
                    ans = pans;
                }
            }else
                if(pd < d){
                    d = pd;
                    ans = pans;
                }

            lf = rg;
            rg += D;
        }

        
        cout << fixed << d << " " << fixed << ans <<  endl;
    }
    return 0;
}
