/*
 * Author: code6
 * Created Time:  2011/6/4 21:55:57
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

int X, S, R, T, N;

struct Walk
{
    int b,e,s;
    bool operator<(const Walk &rhs) const
    {
        return s < rhs.s;
    }
};

int pw;
Walk w[2000];

int ct[500];

int main() {
    
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int t, cas = 0;
    cin>>t;
    while (t--) {
        cas++;
        cin>>X>>S>>R>>T>>N;
        int i, j;
        pw = 0;
        int pre = 0;
        for (i = 0; i < N; i++) {
            int b, e, s;
            cin>>b>>e>>s;
            if (pre < b) {
                w[pw].b = pre;
                w[pw].e = b;
                w[pw].s = 0;
                pw++;
            }
            
            w[pw].b = b;
            w[pw].e = e;
            w[pw].s = s;
            pw++;
            
            pre = e;
        }
        
        if (w[pw - 1].e != X) {
            w[pw].b = w[pw - 1].e;
            w[pw].e = X;
            w[pw].s = 0;
            pw++;
        }
        
        memset(ct, 0, sizeof(ct));
        
        for (i = 0; i < pw; i++) {
            ct[w[i].s] += w[i].e - w[i].b;
        }
        
        double lt = T;
        double ans = 0.0, tmp;
        
        for (i = 0; i < 500; i++) {
            if (ct[i] != 0) {
                //printf("i = %d, ct[i] = %d\n", i, ct[i]);
                if (lt * (i + R) > ct[i] + 0.00001) {
                    tmp = 1.0 * ct[i] / (i + R);
                    ans += tmp;
                    lt -= tmp;
                } else {
                    ans += lt;
                    tmp = 1.0 * (ct[i] - (i + R) * lt) / (i + S);
                    lt = 0;
                    ans += tmp;
                }
            }
        }
        
        printf("Case #%d: %.9lf\n", cas, ans);
        
    }
    
    return 0;
}

