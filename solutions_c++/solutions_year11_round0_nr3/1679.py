
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
   int t;
   int n;
   int tit;
   scanf("%d",&t);
   for(tit=1;tit<=t;tit++)
   {
      printf("Case #%d: ",tit);
      int sum=0,xsum=0,minv=INF;
      int i;
      scanf("%d",&n);
      int tmp;
      for(i=0;i<n;i++)
      {
	 scanf("%d",&tmp);
	 sum+=tmp;
	 xsum^=tmp;
	 minv=min(minv,tmp);
      }
      if(xsum)
	 printf("NO\n");
      else
	 printf("%d\n",sum-minv);
   }

   return 0;
}
