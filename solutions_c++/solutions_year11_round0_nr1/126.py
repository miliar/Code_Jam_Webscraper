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
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <typeinfo>
#include <fstream>

using namespace std;

#define eps 1e-9
#define SZ(X)   (int)(X).size()
#define FOR(i, n)   for(int (i) = 0; (i) < (n); (i)++)
#define inf (1LL<<30)
#define PI acos(-1.0)
#define SQR(v)  (1LL*(v)*(v))
//#define X first
//#define Y second
#define MP(x, y)  make_pair((x), (y))
#define degug(c)  cout << "i am here !!" << " " << ++c << endl;
#define sgn(x)   (x > eps) - (x < -eps)

int dp[100+5][100+5];

int N;
char s[10+5];
int x[100+5], y[100+5], n, m, t[100+5];
int solve(int N)
{
    int ll = 0, rr = 0;
    t[0] = 0;
    for(int i = 1; i <= N; i++)
    {
        if(y[i] == 0)
        {
            t[i] = max(t[i-1] + 1, t[ll] + abs(x[i] - x[ll]) + 1);
            ll = i;
        }
        else
        {
            t[i] = max(t[i-1] + 1, t[rr] + abs(x[rr] - x[i]) + 1);
            rr = i;
        }
    }
    return t[N];
}
int T, ca;
int main()
{
    freopen("A-large.in", "r", stdin);
  //  freopen("A-small-attempt1.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
        n = 0, m = 0;
        x[0] = 1;
        for(int i = 0, xx; i < N; i++)
        {
            scanf("%s", s);
            scanf("%d", &xx);
            x[i+1] = xx;
            if(s[0] == 'O') y[i+1] = 0;
            else  y[i+1] = 1;
        }
        printf("Case #%d: %d\n", ++ca, solve(N));
    }
    return 0;
}
