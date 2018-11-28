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
#define   PB push_back
#define   FI 		first
#define   SE 		second
#define   MP 		make_pair
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
typedef long long int64;
#define   inf         1000000001
#define  MAXN     1000061
#define  eps      1e-6
FILE *fin;
FILE *fout;
//int64 inf=100000000000000000LL;
int T;
int X,S,R,t,N;
int B[MAXN],E[MAXN],W[MAXN];
int a[MAXN];
int main()
{
   	fin=fopen("A-large.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
    rep(rds,1,T+1)
	{
          printf("Case #%d: ",rds);
          fprintf(fout,"Case #%d: ",rds);
		  fscanf(fin,"%d%d%d%d%d",&X,&S,&R,&t,&N);
		  REP(i,N) fscanf(fin,"%d%d%d",B+i,E+i,W+i);
		  clr(a);
		  REP(i,X) a[i]=S;
		  REP(i,N)
		  {
		      for(int j=B[i];j<E[i];j++) a[j]=max(a[j],W[i]+S);
		  }
		  sort(a,a+X);
		  double tt=t;
		  double ret=0;
		  REP(i,X)
		  {
		      if(tt>0)
		      {
                 double nt=1.0/(a[i]+R-S);
                 if(tt>=nt)
                 {
                     tt-=nt;ret+=nt;
                 }
                 else
                 {
                     double d=1.0-(a[i]+R-S)*tt;
                     ret+=tt;
                     tt=0;
                     ret+=d/(a[i]);
                 }
		      }
		      else ret+=1.0/a[i];
		  }
            printf("%.10lf\n",ret);
            fprintf(fout,"%.10lf\n",ret);

	}
}
