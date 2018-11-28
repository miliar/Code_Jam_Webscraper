
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

string s,w="welcome to code jam";
int t[505][25];
void solve_case(int cases)
{
  getline( cin, s );
  mset(t,0);
  REP(i,sz(w))
  {
    REP(j,sz(s))
    {
      if(i==0)
      {
        if(s[j]==w[i]) t[j+1][i+1]=1;
        t[j+1][i+1]+=t[j][i+1];        
      }
      else
      {
        if(s[j]==w[i])
          t[j+1][i+1]=t[j][i+1]+t[j][i];
        else
          t[j+1][i+1]=t[j][i+1];
      }
      t[j+1][i+1]%=10000;
//      cout<<t[j+1][i+1]<<" ";
    }
  //  cout<<endl;
  }
  printf("Case #%d: %.4d\n",cases+1,t[sz(s)][sz(w)]);
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

