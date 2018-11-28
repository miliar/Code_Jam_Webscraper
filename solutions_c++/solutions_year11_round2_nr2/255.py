
//Author Phinfinity
#include<iostream>
#include<cstdio>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<string>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
//#include<climits>
using namespace std;
#define pop_count(n) __builtin_popcount(n)
#define FOR(i,a,b) for(int i= (int)a; i< (int)b; ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;
#define INF 1000000000


int main()
{
   //CODE GOES HERE>>....

   int t,n;
   scanf("%d",&t);
   int tit;
   int i,j;
   LL d;
   LD l,u,p;
   LL inp[500][2];
   for(tit=1;tit<=t;tit++)
   {
      fprintf(stderr,"case %d\n",tit);
      printf("Case #%d: ",tit);
      scanf("%d%lld",&n,&d);
      for(i=0;i<n;i++)
	 scanf("%lld%lld",&inp[i][0],&inp[i][1]);
      bool nochange=true;
      for(i=0;i<n;i++)
	 if(inp[i][1]>1)
	    nochange=false;
      for(i=1;i<n;i++)
	 if(inp[i][0]-inp[i-1][0]<d)
	    nochange=false;
      int it;
      if(nochange)
      {
	 printf("0\n");
      }
      else
      {
	 l=0;
	 u=1e13;
	 LD mind,minpt,maxpt;
	 LD prevpt=-1e13;
	 it=0;
	 while(it<200 && u-l>LD(1e-11))
	 {
	    it++;
	    p=(l+u)/2;
	    prevpt=-1e13;
	    for(i=0;i<n;i++)
	    {
	       // to place minpt at max(prevpt,inp[i][0]-p)
	       // and maxpt at minpt+cnt*d
	       minpt=max(LD(prevpt+d),LD(inp[i][0]-p));
	       maxpt=minpt+(inp[i][1]-1)*d;
	       prevpt=maxpt;
	       if(abs((LD)inp[i][0]-minpt)>p+1e-11 || abs((LD)inp[i][0]-maxpt)>p+1e-11)
		  break;
	    }
	    if(i==n)
	       u=p;
	    else
	       l=p;
	 }
	 printf("%.9Lf\n",p);
      }
   }

   return 0;
}
