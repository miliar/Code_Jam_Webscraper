#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<functional>
#include<iterator>
#include<locale>
#include<memory>
#include<stdexcept>
#include<utility>
#include<string>
#include<fstream>
#include<ios>
#include<iostream>
#include<iosfwd>
#include<iomanip>
#include<istream>
#include<ostream>
#include<sstream>
#include<streambuf>
#include<complex>
#include<numeric>
#include<valarray>
#include<exception>
#include<limits>
#include<new>
#include<typeinfo>
#include<cassert>
#include<cctype>
#include<cerrno>
#include<cfloat>
#include<climits>
#include<cmath>
#include<csetjmp>
#include<csignal>
#include<cstdlib>
#include<cstddef>
#include<cstdarg>
#include<cstdio>
#include<cstring>
#include<ctime>
#define vi vector<int>
#define vvi vector<vi>
#define all(c) c.begin(),c.end()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)
#define MAX(x) numeric_limits<x>::max()
#define FOR(i,a,b) for(int i=(int)(a) ; i < (int)(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) FOR(i,0,n)
#define SZ size()
#define INF MAX(int)
#define getint() ({int e=0;for(gets(q=s);*q;)e=(e<<3)+(e<<1)+*q++-48;e;})
#define putint(a) ({int tmp=a,tmp2;*(q=s+10)='\0';for(;;){tmp2=tmp/10;*--q=tmp-(tmp2<<3)-(tmp2<<1)+48;tmp=tmp2;if(!tmp)break;}puts(q);})
#define LL long long
#define ii pair<int,int>
#define ONLINE_JUDGE 0
using namespace std;
int L,D,N,len;
char str[5001][17];
char inp[1000];
inline bool matches(int i)
{
 int x=0,f;
 for(int j=0;j<len;)
  {
   if(inp[j]=='(')
    {
     ++j;
     f=0;
     while(j<len && inp[j]!=')')
      {
       if(inp[j]==str[i][x])
        {
         f=1;
         
        } 
       ++j;
      } 
     if(f==0)
      return false;
    }
   else
    {
     if(str[i][x]!=inp[j])
      return false;
    }   
   ++j;
   ++x;
  }
 return true; 
}
int main()
 {
    scanf("%d%d%d",&L,&D,&N);
    getchar();
    FOR(i,0,D)
     gets(str[i]);
    int ans;
    FOR(i,0,N)
     {
      ans = 0;
      gets(inp);
      len = strlen(inp);
      FOR(j,0,D)
       if(matches(j))
        ++ans;
      printf("Case #%d: %d\n",i+1,ans);  
     } 
 }   
