
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
   scanf("%d",&t);
   int tit;
   int c,d,n;
   char tmp1,tmp2,tmp3;
   char buf[100000];
   int i,j;
   for(tit=1;tit<=t;tit++)
   {
      map<pair<char,char>,char> m;
      vector<char > offset[256];
      int cnt[256];
      memset(cnt,0,sizeof(cnt));
      scanf("%d",&c);
      vector<char> ans;
      while(c--)
      {
	 scanf(" %c%c%c",&tmp1,&tmp2,&tmp3);
	 m[make_pair(tmp1,tmp2)]=tmp3;
	 m[make_pair(tmp2,tmp1)]=tmp3;
      }
      scanf("%d",&d);
      while(d--)
      {
	 scanf(" %c%c",&tmp1,&tmp2);
	 offset[tmp1].PB(tmp2);
	 offset[tmp2].PB(tmp1);
      }
      scanf("%d",&n);
      scanf("%s",buf);
      for(i=0;buf[i];i++)
      {
	 if(ans.size()>0 && m.count(make_pair(ans.back(),buf[i])))
	 {
	    tmp1=ans.back();
	    ans.pop_back();
	    cnt[tmp1]--;
	    ans.PB(m[make_pair(tmp1,buf[i])]);
	 }
	 else
	    ans.PB(buf[i]);
	 cnt[ans.back()]++;
	 for(j=0;j<offset[ans.back()].size();j++)
	 {
	    if(cnt[offset[ans.back()][j]])
	    {
	       memset(cnt,0,sizeof(cnt));
	       ans.clear();
	       break;
	    }
	 }
      }
      printf("Case #%d: ",tit);
      printf("[");
      for(i=0;i<ans.size();i++)
      {
	 printf("%c",ans[i]);
	 if(i+1!=ans.size())
	    printf(", ");
      }
      printf("]\n");
   }

   return 0;
}
