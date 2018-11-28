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
const int Max = 1010;

int X, S, R, t, N;
typedef struct node{
    int len;
    int w;
    int sv;
    double mt;
    double m1t;
    double cha;
};

node a[Max];

bool cmp( node a, node b)
{
    if( a.cha - b.cha > EPS) return 1;
    return 0;
}

int main()
{
   //freopen("A-large.in","r",stdin);freopen("E:/out.txt","w",stdout);
    int T, test = 0;
    scanf("%d", &T);
    while(T--)
    {
        printf("Case #%d: ", ++test);
        memset( a, 0, sizeof(a));
        scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
        int sum = X;
        int num = 0;
        for(int i = 0; i < N; i++)
        {
            int t1, t2, w1;
            scanf("%d %d %d", &t1, &t2, &w1);
            num++;
            a[num].len = t2 - t1;
            a[num].w = w1;
            sum -= t2 - t1;
        }
        if( sum > 0)
        {
            a[++num].len = sum;
            a[num].w = 0;
        }
        for(int i = 1; i <= num; i++)
        {
            a[i].sv = a[i].w + S + R;
            a[i].mt = 1000000.0 / ( a[i].sv - S);
            a[i].m1t = 1000000.0 / ( a[i].sv - R);
            a[i].cha = a[i].m1t - a[i].mt;
        }
        sort( a+1, a+1+num, cmp);
        double t1 = t;
        double ans = 0;
        for(int i = 1; i <= num; i++)
        {
            double tmp = a[i].len / ( 1.0 * ( a[i].sv - S));
            if( t1 > EPS){
                if( t1 - tmp >= EPS)
                {
                    ans += tmp;
                    t1 -= tmp;
                }
                else
                {
                    ans += t1; 
                    ans += (1.0 * a[i].len - t1 * ( a[i].sv - S)) / ( a[i].sv - R);
                    t1 = -1;
                }
            }
            else
            {
                ans += ( 1.0 * a[i].len) / ( a[i].sv - R);
            }       
        }
        printf("%.8f\n", ans);
    }
    return(0);
}
