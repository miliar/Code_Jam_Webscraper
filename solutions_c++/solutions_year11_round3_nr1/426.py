//DEDICATED TO EMMA WATSON, THE BRITISH *SUNSHINE*
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <string.h>
//#include <fstream>

#define eps 1e-11
#define INF 1000000000
#define PI 3.141592653589793238462
#define EU 2.71828182845904523536
#define sz(a) (int)a.size()
#define pb(a) push_back(a)
#define mset(a,hodnota) memset(a,hodnota,sizeof(a))
#define wh(a) a.begin(),a.end()
#define REP(i,n) for(__typeof(n) i=0;i<(n);++i)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);--i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SQR(a) ((a)*(a))
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
typedef long long ll;
using namespace std;
int R,C;
int M[55][55];
char S[55][55];
void solve_case()
{
  memset(S,'.',sizeof(S));
  scanf("%d %d",&R,&C);
  REP(i,R)
    REP(j,C)
    {

      char ch;
      cin>>ch;
      M[i][j]=ch=='#';
    }
  int poss=1;
  REP(i,R)
    REP(j,C)
    if (M[i][j])
    {
      REP(r,2)
        REP(c,2)
          if (i+r>=R || j+c>=C || !M[i+r][j+c]){poss=0;goto hell;}

      REP(r,2)
        REP(c,2)
          M[i+r][j+c]=0;
      S[i][j]='/';
      S[i][j+1]='\\';      
      S[i+1][j]='\\';            
      S[i+1][j+1]='/';                        
    }
hell:;
  if (!poss)cout<<"Impossible"<<endl;
  else
  {
    REP(i,R)
    {
      REP(j,C)
        cout<<S[i][j];
      cout<<endl;
    }
  }



}

int main()
{
  int cases;
  scanf("%d",&cases);getchar();
  REP(kk,cases)
  {
    cout<<"Case #"<<kk+1<<":"<<endl;
    solve_case();
  }
  return 0;
}



