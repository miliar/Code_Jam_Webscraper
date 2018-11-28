#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

//#define __debug__
//#define __filename__

#ifdef __debug__
    template<class T> inline void __ptr(T x) { cout << x << endl; }
#else
    #define __ptr
#endif

typedef long long LL;
typedef pair<int, int> PII;
typedef complex<int> CPI;
typedef priority_queue<int> iPQ;
const long double PI = acos(-1);
const long double eps = 1e-12;
template<class T> inline int hasBit(T x){ return __builtin_popcountll(x);}
template<class T> inline int testBit(T x,int a){ return x & (1 << a);}
template<class T> inline int isPrime(T x){for(T i=2;i*i<=x;i++)if((x%i)==0) return 0;return 1;}
template<class T> inline T sgn(T x){return abs(x) <= eps ? 0 : x > eps ? 1 : -1;}
template<class T> inline T euclide(T a,T b,T &x,T &y){
    if(b == 0){ x = 1; y = 0; return a;}
    T d = euclide(b, a % b, x, y);T t = x;x = y;y = t - (a / b) * y; return d;
}
template<class T> void getint(T &ret){
    char x;
    while (!isdigit(x=getchar()));
    do {ret = ret * 10 + x - 48;}while (isdigit(x=getchar()));
}

int run();

inline int pause(){
    #ifdef __debug__
        cerr << clock() * 1.0 / CLOCKS_PER_SEC << endl;
        system("pause");
    #endif
    return 0;
}

int main(char args[]){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    run();
    return pause();
}

inline int run(){
    vector<int> v;
    for (int i = 2;i <= 1000000;i++)
        if (isPrime(i)) v.push_back(i);
    int sz = v.size();
    int Test;
    cin >> Test;
    for (int Testcase = 1;Testcase <= Test;Testcase ++){
        LL N;
        int tot = 1;
        cin >> N;
        for (int i = 0;i < sz; i++){
            int x = v[i];
            if ((LL)x * x > N) break;
            LL w = x;
            while (w <= N){
                w *= x;
                if (w > N) break;
                ++tot;
            }
        }
        if (N == 1) tot = 0;
        cout << "Case #" << Testcase << ": " << tot << endl;
    }
}
