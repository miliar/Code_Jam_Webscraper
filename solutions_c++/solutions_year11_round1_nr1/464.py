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

long long N;
int D, G;
int gcd(int a, int b)
{
    return b == 0 ?  a : gcd(b, a%b);
}
int T, ca;
int main()
{
  //  freopen("A-large.in", "r", stdin);
    //freopen("A-small-attempt1.in", "r", stdin);
  //  freopen("A.txt", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
        cin >> N;
        scanf("%d %d", &D, &G);
             printf("Case #%d: ", ++ca);
        if(G == 0&&D != 0)   puts("Broken");
        else if(G == 100&&D != 100)  puts("Broken");
        else if(D == 0)
        {
            printf("Possible\n");
        }
        else if(100/gcd(D, 100) > N)
        {
            puts("Broken");
        }
        else
        {
            printf("Possible\n");
        }
    }
    return 0;
}
