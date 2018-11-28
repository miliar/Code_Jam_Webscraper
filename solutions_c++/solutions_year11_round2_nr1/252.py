
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
   char buf[109][109];
   LD wp[109],owp[109],oowp[109];
   int gcnt[109],wcnt[109],lcnt[109];
   for(tit=1;tit<=t;tit++)
   {
      printf("Case #%d:\n",tit);
      scanf("%d",&n);
      for(i=0;i<n;i++)
	 scanf("%s",buf[i]);
      for(i=0;i<n;i++)
	 gcnt[i]=wcnt[i]=lcnt[i]=0;
      for(i=0;i<n;i++)
	 for(j=0;j<n;j++)
	 {
	    if(buf[i][j]!='.')
	       gcnt[i]++;
	    if(buf[i][j]=='1')
	       wcnt[i]++;
	    else
	       lcnt[i]++;
	 }
      for(i=0;i<n;i++)
	 wp[i]=LD(wcnt[i])/LD(gcnt[i]);
      for(i=0;i<n;i++)
      {
	 owp[i]=0;
	 for(j=0;j<n;j++)
	    if(buf[i][j]!='.')
	       owp[i]+=LD(wcnt[j]-(buf[j][i]=='1'?1:0))/LD(gcnt[j]-(buf[j][i]!='.'?1:0));
	 owp[i]/=gcnt[i];
      }
      for(i=0;i<n;i++)
      {
	 oowp[i]=0;
	 for(j=0;j<n;j++)
	    if(buf[i][j]!='.')
	       oowp[i]+=owp[j];
	 oowp[i]/=gcnt[i];
      }
      /*
      printf("wp:\n");
      for(i=0;i<n;i++)
	 printf("%Lf\n",wp[i]);
      printf("owp:\n");
      for(i=0;i<n;i++)
	 printf("%Lf\n",owp[i]);
      printf("oowp:\n");
      for(i=0;i<n;i++)
	 printf("%Lf\n",oowp[i]);
      */
      for(i=0;i<n;i++)
	 printf("%.12Lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
   }

   return 0;
}
