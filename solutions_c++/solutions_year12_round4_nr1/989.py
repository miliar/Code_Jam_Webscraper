/*
 * Author: code6
 * Created Time:  2012/5/26 21:45:06
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

const int MAX =  10000 + 50;
int n, D;
int p[MAX], l[MAX];
int dp[MAX];

int getR(int i)
{
    if (dp[i] > -1) {
        return p[i] + min(dp[i], l[i]);
    } else {
        return -1;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    int i, j;
    scanf("%d", &t);
    while (t--) {
        cas ++;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d%d", &p[i], &l[i]);
        }
        scanf("%d", &D);
        memset(dp, -1, sizeof(dp));
        dp[0] = p[0];
        int pos = 0;
        for (i = 1; i < n; i++) {
            while (pos < i) {
                if (getR(pos) >= p[i]) {
                    dp[i] = p[i] - p[pos];
                    break;
                } else {
                    pos ++;
                }
            }
        }
        
        string ans = "NO";
        for (i = 0; i < n; i++) {
            if (getR(i) >= D) {
                ans = "YES";
                break;
            }
        }
        printf("Case #%d: %s\n", cas, ans.c_str());
    }
    return 0;
}

