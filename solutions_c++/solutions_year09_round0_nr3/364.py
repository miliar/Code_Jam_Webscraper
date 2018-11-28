#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x)
{
    return x*x;
}

template <class T> T gcd(T a, T b)
{
    if(a < 0) return (gcd(-a, b));
    if(b < 0) return (gcd(a, -b));
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

int main(int argc, char** argv)
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
    int t;
    string str;
    scanf("%d", &t);
    getline(cin, str);
    const string istr = "welcome to code jam";
    const int MOD = 10000;
    for(int ti = 0; ti < t; ti++)
    {
        getline(cin, str);
        int dp[19] = {0};
        for(int i = 0; i < str.size(); i++)
        {
            for(int j = 18; j >= 1; j--)
            {
                if(str[i] == istr[j]) dp[j] = (dp[j] + dp[j - 1]) % MOD;
            }
            if(str[i] == istr[0]) dp[0] = (dp[0] + 1) % MOD;
        }
        printf("Case #%d: ", ti+1);
        printf("%04d\n", dp[18]);
    }
    return (EXIT_SUCCESS);
}

