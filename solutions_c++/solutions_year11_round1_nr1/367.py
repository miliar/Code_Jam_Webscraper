#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   per(i,a,b)  for(int i=((a)-1);i>=(int)(b);i--)
#define   PER(i,n)     per(i,n,0)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   CLEAR(a, v)    memset((a), (v), sizeof(a))
#define   ALL(v)          (v).begin(), (v).end()
#define   mabs(a)       ((a)>0?(a):(-(a)))
#define   inf         1000000001
#define  MAXN     100061
#define  eps      1e-6
#define   PB push_back
#define   FI 		first
#define   SE 		second
#define   MP 		make_pair
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
typedef long long int64;
int64 N;
int64 pd;
int64 pg;
int64 gcd(int64 a,int64 b)
{
    return b==0?a:gcd(b,a%b);
}
int main()
{
    int T;scanf("%d",&T);
    REP(roud,T)
    {
        printf("Case #%d: ",roud+1);
        scanf("%lld%lld%lld",&N,&pd,&pg);
        if(pg==100&&pd!=100||pg==0&&pd!=0)
        {
            printf("Broken\n");continue;
        }
        if(pd==0)
        {
            printf("Possible\n");continue;
        }
        int64 a=gcd(100,pd);
        a=100/a;
        if(N>=a)
        {
            printf("Possible\n");
        }
        else
         printf("Broken\n");
    }
    return 0;
}
