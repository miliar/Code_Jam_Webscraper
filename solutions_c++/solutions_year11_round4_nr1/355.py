#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <iomanip>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;
double EPS = 1e-9;

template<typename T>
ostream& operator<<(ostream& os, vector<T> v) {
    os << "[";
    for(int i = 0; i < v.size(); ++i) {
        cout << v[i];
        if(i != (v.size() - 1)) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

long double compTime(long double &t, long double x, long double w, long double s, long double r) {
    if(x < EPS)
        return 0;
    if(x / (r + w) <= t) {
        t -= x / (r + w);
        return x / (r + w);
    }
    x -= t * (r + w);
    long double k = t;
    t = 0;
    return (x / (w + s)) + k;
}

int main()
{
    int t;
    cin >> t;
    for(int testCase = 1; testCase <= t; ++testCase)
    {
        long double ans = 0;
        long double x, s, r, t;
        int n;
        cin >> x >> s >> r >> t >> n;
        long double old = 0;
        long double b, e;
        vector<pair<long double, long double> > v;
        for(int i = 0; i < n; ++i) {
            long double w;
            cin >> b >> e >> w;
            v.push_back(make_pair(0, b - old));
            v.push_back(make_pair(w, e - b));
            old = e;
        }
        v.push_back(make_pair(0, x - old));
        sort(v.begin(), v.end());
        for(int i = 0; i < v.size(); ++i) {
            ans += compTime(t, v[i].second, v[i].first, s, r);
        }
        cout << "Case #" << testCase << ": " << fixed << setprecision(9) << ans << endl;
    }
}
