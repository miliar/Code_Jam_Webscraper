#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define  MAXN     10021
typedef long long  int64;
FILE *fin;
FILE *fout;
int T,N;
int64 inf=100000000000000000LL;
int64 L,H;
int64 gd[MAXN];
int64 lc[MAXN];
int64 a[MAXN];
int64 res;
int64 gcd(int64 a,int64 b)
{
    return b==0?a:gcd(b,a%b);
}
int64 lcm(int64 a,int64 b)
{
    int64 d=gcd(a,b);
    a/=d;
    if(a>inf/b) return H+1;
    a*=b;
    if(a>H) return H+1;
    return a;
}
void docheck(int64 a)
{
    if(a>=L&&a<=H) res=min(res,a);
}
int main()
{
   	fin=fopen("C-small-attempt1.in","r");
	fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
    rep(rds,1,T+1)
	{
          printf("Case #%d: ",rds);
          fprintf(fout,"Case #%d: ",rds);
		  fscanf(fin,"%d%lld%lld",&N,&L,&H);
		  REP(i,N) fscanf(fin,"%lld",a+i);
		  sort(a,a+N);
		  res=inf;
		  rep(i,L,H+1)
		  {
		      bool f=true;
		      REP(j,N) if(i%a[j]==0||a[j]%i==0) continue ;else f=false;
		      if(f) docheck(i);
		  }
		  if(res>H)
		  {
            printf("NO\n");
            fprintf(fout,"NO\n");
		  }
		  else
		  {
            printf("%lld\n",res);
            fprintf(fout,"%lld\n",res);
		  }
	}
}
