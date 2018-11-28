#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <vector>
#include <list>
#include <deque>
#include <climits>
#include <algorithm>
#include <queue>
#include <functional>
#include <map>
#include <set>
#include <iomanip>
#include <ctime>
#include <stack>

using namespace std;


#if 0
#define d64 "%lld"
#else
#define d64 "%I64d"
#endif
#define mp make_pair
typedef long long LL;
const int INF = INT_MAX;

typedef pair<int, int> pii;
typedef pair<LL, LL> pll;
typedef pair<double, double> pdd;
const double EPS = 1e-10;
inline double SQR(double x){return x * x;}
inline LL SQR(LL x){return x * x;}
inline int SQR(int x){return x * x;}
inline double SQR3(double x) {return x * x * x; }
inline void DEBUG(){puts("jackie");}
inline bool zero(double x) {return abs(x) < EPS;}
inline int inInt()
{
    int x = 0, c;
    while((unsigned)((c = getchar()) - '0') >= 10)
    {
        if('-' == c)
        return -inInt();
//        if(!~c)
//        throw ~0;
    }
    do
    {
        x = (x << 3) + (x << 1) + (c - '0');
    }while((unsigned)((c = getchar()) - '0') < 10);
    return x;
}
inline void outInt(int x)
{
    if(x < 0)
    {
        putchar('-');
        x = -x;
    }
    if(x >= 10) outInt(x / 10);
    putchar((x % 10) + '0');
}

const int MAXN = 110000;

int N;
LL d[MAXN], l[MAXN];
LL D;

bool vis[MAXN];
LL record[MAXN];

bool check(int idx, LL len)
{
    record[idx] = len;
   if(len >= D - d[idx]) return true;

   for(int i = idx + 1; i < N; i++)
   {
       if(len >= d[i] - d[idx])
       {
           if(min(d[i] - d[idx], l[i]) > record[i] && check(i, min(d[i] - d[idx], l[i]))) return true;
       }
       else
       {
           break;
       }
   }
   return false;
}

int main()
{

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;

    for(int n_case = 1; n_case  <= T; n_case++)
    {
        cin >> N;
        for(int i = 0; i < N; i++)
        {
            cin >> d[i] >> l[i];
        }
        cin >> D;
        memset(vis, false, sizeof(vis));
        memset(record, -1, sizeof(record));

        cout << "Case #" << n_case << ": ";

        if(d[0] > l[0])
        {
            cout << "NO" << endl;
            continue;
        }
        if(check(0, d[0]))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }






    }


















    return 0;
}
