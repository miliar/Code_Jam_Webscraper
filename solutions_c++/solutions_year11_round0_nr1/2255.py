/*
 * Author: code6
 * Created Time:  2011/5/7 21:37:28
 * File Name: A.cpp
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

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-small-out0.in", "w", stdout);
    int t, cas = 0;
    cin>>t;
    while (t--) {
        cas ++;
        int x, y, lx, ly;
        x = 1, y = 1; lx = ly = 0;
        int n;
        int ret = 0, use;
        cin>>n;
        for (int i = 0; i < n; i++)  {
            char ty;
            int at;
            cin>>ty>>at;
            if (ty == 'B') {
                use = max(0, abs(at - x) - lx) + 1;
                ret += use;
                ly += use;
                lx = 0;
                x = at;
            } else {
                use = max(0, abs(at - y) - ly) + 1;
                ret += use;
                lx += use;
                ly = 0;
                y = at;
            }
        }
        
        printf("Case #%d: %d\n", cas, ret);
    }
    return 0;
}

