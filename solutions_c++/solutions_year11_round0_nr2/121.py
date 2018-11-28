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

char a[300+5][300+5];
bool x[300+5][300+5];
int C, D, N;
char s[200+5];
char q[200+5];
int sf = 0, T, ca;
int main()
{
   // freopen("B-large.in", "r", stdin);
   // freopen("B-large.out", "w", stdout);
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0.out", "w", stdout);
//    freopen("A.txt", "r", stdin);
    scanf("%d", &T);
    //cout << T << endl;
    while(T--)
    {
        sf = 0;
        scanf("%d", &C);
        memset(a, 0, sizeof(a));
        memset(x, 0, sizeof(x));
        for(int i = 0; i < C; i++)
        {
            scanf("%s", s);
            a[s[0]][s[1]] = a[s[1]][s[0]] = s[2];
        }
        scanf("%d", &D);
        for(int i = 0; i < D; i++)
        {
            scanf("%s", s);
            x[s[0]][s[1]] = x[s[1]][s[0]] = 1;
        }
        scanf("%d", &N);
        scanf("%s", s);
        sf = 0;
        for(int i = 0; i < N; i++)
        {
            q[sf++] = s[i];
            while(sf > 1&&a[q[sf-1]][q[sf-2]] != 0)
            {
                q[sf-2] = a[q[sf-1]][q[sf-2]];
                sf--;
            }
            for(int i = 0; i < sf-1; i++)
            {
                if(x[q[i]][q[sf-1]])
                {
                    sf = 0;
                    break;
                }
            }
        }
        printf("Case #%d: ", ++ca);
        printf("[");
        if(sf > 0)
        {
            for(int i = 0; i + 1 < sf; i++)  printf("%c, ", q[i]);
            printf("%c", q[sf-1]);
        }
        printf("]\n");
    }
    return 0;
}
