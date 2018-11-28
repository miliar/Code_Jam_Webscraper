
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <ctime>
#define REP(i,u) for(__typeof(u) i=0;i<(u);i++)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(a) i=(a);i<=(b);i++)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);i--)
#define FORE(it,c) for(__typeof(c.begin()) it=(c).begin();it!=(c).end();it++)
#define SQR(a) ((a)*(a))
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define mset(a,u) memset(a,u,sizeof(a))
#define sz(a) ((int)a.size())
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
#define PI 3.141592653589793238462

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;


vector<LL> pov,pov1,pov2;
/*int ne[10];
bool comp(int N)
{
   mset(ne,0);
   while(N)
   {
     ne[N%10]++;
     N/=10;
   }
   REP(i,9)
     if(ne[i+1]!=pov[i+1]) return false;
   return true;
}*/

LL N;
void solve_case(int pp)
{
char c;
pov.clear();
do
{

  c=getchar();
  if(c=='\n')break;
  pov.pb(c-'0');
}
while(c!='\n');


   int poc=0,poc1=0,fi=0;
   while(1)
   {
     do
     {
       if(fi)
       {
        printf("Case #%d: ",pp+1);
        REP(i,sz(pov))
          cout<<pov[i];
        putchar(10); 
        return;
       }
       fi=1;
     }while ( next_permutation( pov.begin(), pov.end() ) );
     poc1++;
     sort(pov.begin(),pov.end());
     REP(i,sz(pov))
      if(pov[i]!=0)
      {
        poc=pov[i];
        pov[i]=0;
        pov.insert(pov.begin(),poc);
        break;
      }
      
   } 
}


int cases;
int main( )
{
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    solve_case(ii);
  }         
  return 0;
}

