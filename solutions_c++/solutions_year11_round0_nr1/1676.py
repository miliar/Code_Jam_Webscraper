
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

   int t,n;
   scanf("%d",&t);
   int tit;
   int i;
   char c;
   int tmp;
   for(tit=1;tit<=t;tit++)
   {
      vector<PI> o,b;
      scanf("%d",&n);
      for(i=0;i<n;i++)
      {
	 scanf(" %c %d",&c,&tmp);
	 if(c=='O')
	    o.PB(make_pair(tmp,i));
	 else
	    b.PB(make_pair(tmp,i));
      }
      int oit=0,bit=0;
      int opos=1,bpos=1;
      int tim=0;
      bool push=false;
      while(oit<o.size() || bit<b.size())
      {
	 push=false;
	 if(oit<o.size())
	 {
	    if(opos!=o[oit].first)
	       opos+=o[oit].first>opos?1:-1;
	    else if(bit>=b.size() || o[oit].second<b[bit].second)
	    {
	       oit++;
	       push=true;
	    }
	 }
	 if(bit<b.size())
	 {
	    if(bpos!=b[bit].first)
	       bpos+=b[bit].first>bpos?1:-1;
	    else if((oit>=o.size() || b[bit].second<o[oit].second) && !push)
	       bit++;
	 }
	 tim++;
      }
      printf("Case #%d: %d\n",tit,tim);
   }

   return 0;
}
