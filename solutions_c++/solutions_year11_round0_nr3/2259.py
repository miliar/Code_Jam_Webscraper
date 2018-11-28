/*
 * Author: code6
 * Created Time:  2011/5/7 23:58:04
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <string>

using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
typedef long long ll;
const double PI=acos(-1.0);
const double eps=1e-11;

int n;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int i, j;
    int t, cas = 0;
    cin >> t;
    while ( t-- ) {
        cas ++;
        cin >> n;
        int tot = 0;
        int mi = 100000000;
        int sum = 0;
        for (i = 0; i < n; i++) {
            int v;
            cin >>  v;
            tot ^= v;
            mi = min(mi, v);
            sum += v;
        }
        
        if (tot) {
            printf("Case #%d: NO\n", cas);
            continue;
        }
        
        printf("Case #%d: %d\n", cas, sum - mi);
    }
    return 0;
}

