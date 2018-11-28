#include <iostream>
#include <cstdio>
#include <utility>
#include <algorithm>


using namespace std;
const int maxn = 20009;

struct piece{
    long long b, e, w;
};

piece a [ maxn ];
long long sz;
pair<long double, long long> ben [ maxn ];
bool cmp ( pair<long double, long long> a1, pair<long double, long long> a2 ){
    return a1.first < a2.first;
}

int main()
{
    long long k, x, y, z, nt, s, n, i, r,xx;
    freopen ( "input.txt", "rt", stdin );
    freopen ( "output.txt", "wt", stdout );
    long double t;
    cin >> nt;
    for ( k = 1; k <= nt; ++ k ){
        cin >> x >> s >> r >> t >> n;
        a [ 0 ].b = 0;a [ 0 ].e = 0;a [ 0 ].w = 0;
        sz = 0;
        long double ans = 0.0;
        for ( i = 0; i < n; ++ i ){
            cin >> xx >> y >> z;
            if ( xx > a [ sz ].e ){
                a [ ++ sz ].b = a [ sz - 1 ].e;
                a [ sz ].e = xx;
                a [ sz ].w = s;
            }
            a [ ++ sz ].b = xx;
            a [ sz ].e = y;
            a [ sz ].w = z+s;
        }
        if ( a[sz].e < x ){
            a [ ++ sz ].b = a[sz-1].e;
            a [ sz ].e = x;
            a [ sz ].w = s;
        }
        r -= s;
        for ( i = 1; i <= sz; ++ i ){
            long double aux = ((long double)a [ i ].e - a [ i ].b)/((long double)a[i].w+r);
            long double aux2 = ((long double)a [ i ].e - a [ i ].b)/((long double)a[i].w);
            ben [ i ].first = aux/(aux2-aux);
            ben[i].second = i;
        }
        sort ( ben + 1, ben + sz + 1, cmp );
        for ( i = 1; i <= sz; ++ i ){
            long long ind = ben [ i ].second;
            long double timp = ((long double)a [ ind ].e-a[ind].b)/((long double)a[ind].w+r);
            if ( t >= timp ){
                t -= timp;
                ans += timp;
            }
            else if (t>0){
                long double dist = ((long double)a [ind].w+r)*t;
                ans += t;
                t = 0;
                dist = ((long double)a[ind].e-a[ind].b)-dist;
                timp = (dist)/((long double)a[ind].w);
                ans += timp;
            }
            else{
                timp = ((long double)a [ ind ].e-a[ind].b)/((long double)a[ind].w);
                ans+=timp;
            }
        }
        double ras = ans;
        printf ( "Case #%lld: %.9lf\n", k, ras );
    }
    return 0;
}
