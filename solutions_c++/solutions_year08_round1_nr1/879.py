#pragma warning (disable:4786)
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime> //clock()
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
using namespace std;

#ifdef __GNUC__
typedef long long int64;
#else //MS Visual Studio
typedef __int64 int64;
#endif

const long double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const long double PI = 2 * acos(.0);


#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define REPD(i,n) for (int i((n)-1); i >= 0; --i)
#define FILL(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }


int main(int argc, char * argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a-test.out", "w", stdout);
    int N, casei = 1;
    scanf("%d", &N);
/*
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1
*/
    while (N-- > 0)
    {
        int len;
        scanf("%d", &len); 
        vector<long> vx;
        vector<long> vy;
        int temp = len;
        while(temp --)
        {
            long q;
            scanf("%d", &q);
            vx.push_back(q);
        }
        temp = len;
        while(temp --)
        {
            long q;
            scanf("%d", &q);
            vy.push_back(q);
        }

        sort(vx.begin(), vx.end());
        sort(vy.begin(), vy.end());
// printf(" %d %d %d %d %d\n",vy[0],vy[1],vy[2], vy[3],vy[4]);
        reverse(vy.begin(), vy.end());
// printf(" %d %d %d %d %d\n",vy[0],vy[1],vy[2] , vy[3],vy[4]);

        long ret = 0;

        int start = 0;
        int end = len-1;
        while(start <= end)
        {
            if (start == end)
            {
                ret += vx[start]*vy[end];
                break;
            }
            int t = vx[start]*vy[start] + vx[end]*vy[end];
            ret += t;
            start++;
            end--;
        }
        for (int i = 0; i < len; i++)
        {
// printf(" %d %d ",vx[i],vy[i]);
            // ret += vx[i]*vy[i]; 
        }

        // ...
        printf("Case #%d: %d\n", casei++, ret );
    }
    return 0;
}

