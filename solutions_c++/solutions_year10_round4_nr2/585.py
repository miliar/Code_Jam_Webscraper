#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <functional>
#include <complex>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
using namespace std;
#define rep(i,n) for (int i = 0; i < (int)(n); ++i)
#define foreach(i,c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(),(c).end()

const int inf = 987654321;
const double eps = 1e-9;

int calc(vector<vector<int> > &cost, vector<int> &con, int begin, int end, int cur, int depth, int p) {
    if (begin == end) {
        if (con[begin] == 1) return cost[depth][begin];
        else if (con[begin] < 1) return 0;
        else return inf;
    } else {
        int can1, can2;
        can1 = cost[depth][cur];
        for (int i = begin; i <= end; ++i) con[i]--;
        can1 += calc(cost, con, begin, (begin+end)/2, cur*2, depth-1, p) + calc(cost, con, (begin+end)/2+1, end, cur*2+1, depth-1, p);
        for (int i = begin; i <= end; ++i) con[i]++;
        can2 = calc(cost, con, begin, (begin+end)/2, cur*2, depth-1, p) + calc(cost, con, (begin+end)/2+1, end, cur*2+1, depth-1, p);
        //cout << can1 << " " << can2 << endl;
        if (can1 >= inf && can2 >= inf) return inf;
        if (can1 >= inf) return can2;
        if (can2 >= inf) return can1;
        return min(can1,can2);
    }
}


int main() {
    int T;
    cin >> T;
    rep(I,T) {
        int p;
        cin >> p;
        int n = (1 << p), m = (1 << (p-1));
        vector<int> vi(n), v(m);
        rep(i,n) {
            int tmp;
            cin >> tmp;
            vi[i] = p - tmp;
        }
        rep(i,m) v[i] = max(vi[2*i],vi[2*i+1]);
        //rep(i,m) cerr << v[i] << ' '; cerr << endl;
        
        vector<vector<int> > cost(1024, vector<int>(1024));
        int cnt = m, depth = 0;
        while (cnt > 0) {
            rep(i,cnt) {
                cin >> cost[depth][i];
            }
            ++depth;
            cnt /= 2;
        }
        
        
        cout << "Case #" << I+1 << ": " << calc(cost, v, 0, m-1, 0, p-1, p) << endl;
    }
    return 0;
}

