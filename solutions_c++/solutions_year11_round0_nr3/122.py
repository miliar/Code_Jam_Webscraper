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

int T, ca, N, sum, x;
int main()
{
     freopen("C-large.in", "r", stdin);
     freopen("C-large.out", "w", stdout);
 //   freopen("C-small-attempt0.in", "r", stdin);
 //   freopen("C-small-attempt0.out", "w", stdout);
   // freopen("A.txt", "r", stdin);
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &N);
        int sg = 0;
        x = 1000000+5;
        sum = 0;
      //  cout << (5^3) << endl;
        for(int i = 0, xx; i < N; i++)
        {
            scanf("%d", &xx);
           // cout << xx << endl;
            x = min(xx, x);
            sum += xx;
            sg ^= xx;
        }
        printf("Case #%d: ", ++ca);
        if(sg != 0) printf("NO\n");
        else
        {
            printf("%d\n", sum - x);
        }
    }
    return 0;
}
