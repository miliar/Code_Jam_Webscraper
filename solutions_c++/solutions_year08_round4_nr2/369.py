#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long int64;
const int64 MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;} 
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}

int  N, M, A;
int  x1, Y1, x2, y2;
bool Solve()
{
    int S, MAX;
    for(x1 = 0; x1 <= N; ++x1)
    {
        for(y2 = 0; y2 <= M; ++y2)
        {
            S = A + y2 * x1;
            MAX = sqrt(1.0*S);
            for(x2 = 1; x2 <= MAX; ++x2)
			{
                if(S % x2 == 0)
                {
                    Y1 = S / x2;
                    if(Y1 <= M && x2 <= N)
                        return 1;
                    else if(Y1 <= N && x2 <= M)
                    {
                         swap(Y1, x2);
                         return 1;
                    }
                }
			}
        }
    }
    return 0;
}
int main()
{
    int T, ctr;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    for(ctr = 1; ctr <= T; ++ctr)
    {
        scanf("%d%d%d", &N, &M, &A);
        printf("Case #%d:", ctr);
        if(Solve()) printf(" 0 0 %d %d %d %d\n", x1, Y1, x2, y2);
        else printf(" IMPOSSIBLE\n");
    }
}
