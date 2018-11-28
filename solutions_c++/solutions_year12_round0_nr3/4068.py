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
FILE *fin;
FILE *fout;
//int64 inf=100000000000000000LL;
int T,A,B;
int zu[10];
int tmp[10];
int suan(int a)
{
    int b=a;
    vector<int> t;
    while(b!=0) t.PB(b%10),b/=10;
    reverse(ALL(t));
    REP(i,SZ(t)) zu[i]=t[i],t[i]=(i+1)%SZ(t);
    int ret=0;
    while(true)
    {
        REP(i,SZ(t)) tmp[i]=zu[t[i]];
        REP(i,SZ(t)) zu[i]=tmp[i];
        int v=0;
        REP(i,SZ(t)) v=v*10+zu[i];
        if(v==a) break;
        if(v>a&&v>=A&&v<=B) ret++;
    }
    return ret;
}
int main()
{
   	fin=fopen("C-large.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
    	rep(rds,1,T+1)
	{
         	 printf("Case #%d: ",rds);
          	fprintf(fout,"Case #%d: ",rds);
		  fscanf(fin,"%d%d",&A,&B);
          int64 cnt=0;
          rep(i,A,B)
          {
              cnt+=suan(i);
          }
		  fprintf(fout,"%lld\n",cnt);
		  printf("%lld\n",cnt);
	}
}
