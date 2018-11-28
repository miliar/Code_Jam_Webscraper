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
const long double eps = 1e-10;
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
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    run();
    return pause();
}

double v[1<<10][1<<10];

inline int run(){
    int test;
    scanf("%d",&test);
    for (int Testcase = 1; Testcase <= test;Testcase ++){
        int n,m,d;
        int ans = 0;
        scanf("%d %d %d\n",&n,&m,&d);
        for (int i=1;i<=n;i++) {
            for (int j=1;j<=m;j++)
                v[i][j] = getchar() - '0';
            getchar();
        }
        for (int i = 1;i <= n; i++)
            for (int j = 1;j <= m; j++)
                for (int len=3;len <= min(n,m);len++) {
                    if (i + len - 1 > n||j + len - 1 > m) continue;
                    double mi=(i + i + len - 1)/2.0,mj = (j + j + len - 1)/2.0, si = 0,sj = 0;
                    for (int ti=i;ti<=i+len-1;ti++)
                        for (int tj=j;tj<=j+len-1;tj++) {
                            if (ti==i&&tj==j || ti==i&&tj==j+len-1 || ti==i+len-1&&tj==j 
                                || ti==i+len-1&&tj==j+len-1) continue;
                            si+=(ti-mi)*v[ti][tj];
                            sj+=(tj-mj)*v[ti][tj];
                        }
                    if (abs(si) < eps && abs(sj)< eps) ans = max(ans,len);
                }
        printf("Case #%d: ",Testcase);
        if (ans == 0) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
}
