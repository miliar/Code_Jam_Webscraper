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
#define   ALL(x) 	x.begin(),x.end()
#define   mabs(a)     ((a)>0?(a):(-(a)))
#define   inf         1000000001
#define  MAXN     1160100
#define  eps      1e-6
int N;
int a[MAXN];
bool visited[MAXN];
int main()
{
    int T;scanf("%d",&T);
    REP(roud,T)
    {
        printf("Case #%d: ",roud+1);
        scanf("%d",&N);REP(i,N)scanf("%d",a+i);
        int v=0;REP(i,N) v^=a[i];
        if(v==0)
        {
            int t=inf,s=0;REP(i,N) s+=a[i],t=min(a[i],t);
            s-=t;
            printf("%d\n",s);
        }
        else printf("NO\n");
    }
    return 0;
}
