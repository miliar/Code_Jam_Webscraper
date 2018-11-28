#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^a=;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
int check(int i, int j){
    string a = i2s(i), b = i2s(j);
    int sa = SZ(a), sb = SZ(b);
    int ans;
    if (sa != sb || sa == 1 || sb == 1) return 0;
    for (int k = 1; k < sa; k ++){
        ans = 1;
        for (int ll = sa - k, mm = 0; ll < sa; ll ++, mm++){
            if (a[ll] != b[mm]){
               ans = 0; break;
            }
        }
        for (int ll = 0, mm = k; ll < sa - k; ll ++, mm ++){
            if (a[ll] != b[mm]){
               ans = 0; break;          
            }
        }
        if (ans) return ans;
    }
    return 0;
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    int T, A, B, ans;
    cin >> T;
    for (int i = 0; i < T; i ++){
        printf("Case #%d: ", i+1);
        ans = 0;
        cin >> A >> B;
        for (int j = A; j < B; j ++){
            for (int k = j+1; k <= B; k ++){
                ans += check(j, k);     
            }
        }
        cout << ans << endl;
    }
    return 0;
}

