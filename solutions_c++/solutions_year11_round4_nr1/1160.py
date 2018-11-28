
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
#define INF 1000000000


int main()
{
   //CODE GOES HERE>>....

   int kases,tcnt;
   scanf("%d",&tcnt);
   kases=0;
   while(kases++<tcnt)
   {
      printf("Case #%d: ",kases);
      int n;
      double x,s,r,t;
      scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
      int i;
      double b[1009],e[1009],w[1009];
      r-=s;
      vector<pair<double,double> > a;
      for(i=0;i<n;i++)
	 scanf("%lf%lf%lf",&b[i],&e[i],&w[i]);
      double ppos=0;
      for(i=0;i<n;i++)
      {
	 if(b[i]-ppos>1e-3)
	    a.PB(make_pair(s,b[i]-ppos));

	 a.PB(make_pair(s+w[i],e[i]-b[i]));
	 ppos=e[i];
      }
      if(ppos<x)
	 a.PB(make_pair(s,x-ppos));
      sort(a.begin(),a.end());
      double ans=0,tmp;
      for(i=0;i<a.size();i++)
      {
	 tmp=a[i].second/(a[i].first+r);
	 if(tmp<=t)
	 {
	    t-=tmp;
	    ans+=tmp;
	 }
	 else
	 {
	    a[i].second-=(a[i].first+r)*t;
	    ans+=t;
	    t=0;
	    ans+=a[i].second/a[i].first;
	 }
      }
      printf("%.9lf\n",ans);

   }

   return 0;
}
