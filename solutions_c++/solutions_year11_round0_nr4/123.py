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

int T, ca, N, x[1000+5], visted[1000+5];
vector<int> X;


//void init()
//{
//    dp[1] = 0;  dp[2] = 2;
//    for(int i = 3; i <= 10; i++)
//    {
//        double ans = 0, fac = 1.0;
//        for(int k = i-1; k >= 2; k--)
//        {
//            ans += 1.0*dp[k]/k;
//        }
//        ans += 1;
//        dp[i] = ans*i/(i-1);
//        cout << dp[i] << " " << i << endl;
//    }
//}
int main()
{
   // freopen("D-large.in", "r", stdin);
   // freopen("D-large.out", "w", stdout);

   // freopen("D-small-attempt3.in", "r", stdin);
   // freopen("D-small-attempt0.out", "w", stdout);
   // freopen("A.txt", "r", stdin);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
        X.clear();
        for(int i = 1; i <= N; i++)  scanf("%d", &x[i]);
        for(int i = 1; i <= N; i++) X.push_back(x[i]);

        memset(visted, 0, sizeof(visted));
        int ans = 0;
        for(int i = 1; i <= N; i++)
        {
            int cnt = 0;
            if(visted[i] == 0)
            {
                for(int k = i; visted[k] == 0; k = x[k])
                {
                    visted[k] = 1;
                    cnt++;
                }
                if(cnt > 1) ans += cnt;
            }
        }
        printf("Case #%d: %.6lf\n", ++ca, 1.0*ans);
    }
    return 0;
}


