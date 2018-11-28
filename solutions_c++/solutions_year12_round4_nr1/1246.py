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
#define  MAXN     10061
#define  eps      1e-6
#define   PB push_back
#define   FI 		first
#define   SE 		second
#define   MP 		make_pair
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
typedef long long int64;
FILE *fin;
FILE *fout;
//int64 inf=100000000000000000LL;
int T,N;
int64 d[MAXN],l[MAXN];
int64 D;
int64 dp[MAXN];
bool solve()
{
    clr(dp);
    dp[0]=d[0];
   // REP(i,N) if(l[i]>=d[i]) dp[i]=d[i];
    REP(i,N)
    {
        int64 dm=d[i]+dp[i];
        if(dm>=D) return true;
        rep(j,i+1,N)
        {
            if(d[j]>dm) break;
            int64 tmp=min(d[j]-d[i],l[j]);
            checkmax(dp[j],tmp);
        }
    }
    return false;
}
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
    rep(rds,1,T+1)
	{
         	 printf("Case #%d: ",rds);
          	fprintf(fout,"Case #%d: ",rds);
		  fscanf(fin,"%d",&N);
          REP(i,N)
          {
              int a,b;fscanf(fin,"%d%d",&a,&b);
              d[i]=a,l[i]=b;
          }
          int tmpd;fscanf(fin,"%d",&tmpd);
          D=tmpd;
          bool ret=solve();
          if(ret)
          {
             fprintf(fout,"YES\n");
                printf("YES\n");
          }
          else
          {
                fprintf(fout,"NO\n");
                printf("NO\n");
          }

	}
}
