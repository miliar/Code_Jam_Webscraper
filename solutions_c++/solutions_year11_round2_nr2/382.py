#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<string> vstr;
typedef pair<int, int> pint;

#define TWO(k)  (1<<k)
#define TWOL(k) (((LL)(1)<<(k)))
#define MP make_pair
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int oo = 210000000;
const int Max = 210;

typedef struct node{
    int v, p;
};
node a[Max];
int n, d;

double solve()
{
    double ans = 0.0;
    for(int i = 1; i <= n; i++)
    {
        for(int j = n; j >= i; j--)
        {
            double l = a[j].p - a[i].p;
            double sumv = 0;
            for(int k = i; k <= j; k++)
            {
                sumv += a[k].v;
            }
            double l1 = 1.0 * d * (1.0*( sumv - 1));
            if( l1 - l >= EPS)
            {
                double tmp = ( l1 - l) / 2.0;
                if( tmp - ans >= EPS) ans = tmp;
            }
        }
    }
    return(ans);
}

int main()
{
    //freopen("B-large.in","r",stdin);freopen("E:/out.txt","w",stdout);
    int t, test = 0;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ++test);
        scanf("%d %d", &n, &d);
        for(int i = 1; i <= n; i++)
        {
            scanf("%d %d", &a[i].p, &a[i].v);
        }      
        printf("%.7f\n", solve());
    }
    return(0);
}

