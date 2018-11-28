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
double min(double a, double b){return (a<b)?a:b;}
int main(){
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    int T, A, B;
    double pp, tmp, ans;
    cin >> T;
    for (int i = 0; i < T; i ++){
        printf("Case #%d: ", i+1);
        ans = 0;
        pp = 1;
        cin >> A >> B;
        ans = (double)B + 2.0;
        for (int j = 0; j < A; j ++){
            scanf("%lf", &tmp);
            pp = pp * tmp;
            ans = min( ans, (1.0 - pp)*(B+1)+(A-j-1)*2+B-A+1);
        }
        printf("%.6f\n", ans);
    }
    return 0;
}

