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

int main()
{
   // freopen("C-small-attempt0.in.txt","r",stdin);freopen("out.txt","w",stdout);
    int t, test = 0;
    scanf("%d", &t); //cout<<t<<endl;
    while(t--)
    {
        int a[1010], n;
        int sum = 0, ans = -1;
        int sum1 = 0;
        scanf("%d", &n);
        for( int i = 0; i < n; i++)
        {
             scanf("%d", &a[i]);
             sum += a[i];
             sum1 ^= a[i];
        }
        for( int i = 0; i < n; i++)
        {
             int tmp = sum1 ^ a[i];
             if(tmp == a[i])
             {
                 if( sum - a[i] > ans)
                 {
                     ans = sum - a[i];
                 }
             }
        }
        printf("Case #%d: ", ++test);
        if( ans >= 0) printf("%d\n", ans);
        else printf("NO\n");
    }
    return(0);
}
