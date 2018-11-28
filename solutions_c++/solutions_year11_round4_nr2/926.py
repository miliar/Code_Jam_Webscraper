#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <tr1/unordered_map>
#include <tr1/unordered_set>

#define umap    tr1::unordered_map
#define uset    tr1::unordered_set
#define pv(i,n) ((i)>0?(i)-1:(n)-1)
#define nx(i,n) ((i)+1<(n)?(i)+1:0)
#define TT      template<typename T>
#define TAB     template<typename A,typename B>
#define ss(x)   cout<<"DEBUG : "#x" = "<<(x)<<"\n"

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
TT T sqr(const T &x) { return x * x; }
TT T abs(const T &x) { return x < 0 ? -x : x; }
TT void mil(T &a, const T &b) { if (a > b) a = b;}
TT void mal(T &a, const T &b) { if (a < b) a = b;}
TT T gcd(T a, T b) { while (b) { T t = a % b; a = b; b = t; } return a; }
TAB B conv(const A &i) { stringstream s; s << i; B o; s >> o; return o; }
TAB istream& operator >>(istream &i, pair<A, B> &p) { return i >> p.first >> p.second; }
TT void usort(vector<T> &a) { sort(a.begin(), a.end()); a.erase(unique(a.begin(), a.end()), a.end()); }
TT pair<T, T> operator +(const pair<T, T> &a, const pair<T, T> &b) { return pair<T, T>(a.first + b.first, a.second + b.second); }
TT pair<T, T> operator -(const pair<T, T> &a, const pair<T, T> &b) { return pair<T, T>(a.first - b.first, a.second - b.second); }

int n, m, d;
char mat[12][12];

bool check(int len) {
    for (int i = 0; i + len <= n; ++i) {
        for (int j = 0; j + len <= m; ++j) {
            double mx = i + (len - 1) / 2.0;
            double my = j + (len - 1) / 2.0;
            double sx = 0.0;
            double sy = 0.0;
            int c = 0;

            for (int p = 0; p < len; ++p) {
                for (int q = 0; q < len; ++q) {
                    if (p == 0 && q == 0) continue;
                    if (p == 0 && q == len - 1) continue;
                    if (p == len - 1 && q == 0) continue;
                    if (p == len - 1 && q == len - 1) continue;
                    ++c;
                    int x = i + p;
                    int y = j + q;

                    sx += (mx - x) * mat[x][y];
                    sy += (my - y) * mat[x][y];
                }
            }
            //printf("%d : %d %d (%d)\n", len, i, j, c);
            //ss(sx);
            //ss(sy);
            if (fabs(sx) < 0.0001 && fabs(sy) < 0.0001) {
                return true;
            }
        }
    }
    return false;
}

void york() {
    int t;
    scanf("%d", &t);
    for (int xxxxx = 0; xxxxx < t; ++xxxxx) {
        scanf("%d%d%d", &n, &m, &d);
        for (int i = 0; i < n; ++i) {
            scanf("%s", mat[i]);
            for (int j = 0; j < m; ++j) {
                mat[i][j] -= '0';
            }
        }
        int len;
        for (len = min(n, m); len >= 3; --len) {
            if (check(len)) {
                break;
            }
        }
        printf("Case #%d: ", xxxxx + 1);
        if (len < 3) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", len);
        }
    }
}

int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    york();
    return 0;
}
