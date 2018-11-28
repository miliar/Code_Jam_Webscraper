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
//#include <fstream>

#define eps 1e-11
#define INF 1000000000
#define PI 3.141592653589793238462
#define EU 2.71828182845904523536
#define sz(a) (int)a.size()
#define pb(a) push_back(a)
#define mset(a,hodnota) memset(a,hodnota,sizeof(a))
#define wh(a) a.begin(),a.end()
#define REP(i,n) for(int (i)=0;i<(n);++i)
#define REPS(i,n) for(int (i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(int (i)=(a);i<=(b);++i)
#define FORD(i,a,b) for(int (i)=(a);i>=(b);--i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SQR(a) ((a)*(a))
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
typedef long long ll;
using namespace std;
int R,C;
int G[105][105];
int L[105][105];

vector<pair<int,pii> > V;
int dir[4][2]={-1,0, 0,-1, 0,1, 1,0};
int maping[30];
int casecnt=1;
inline void solve_case()
{
  printf("Case #%d:\n",casecnt++);

  scanf("%d %d",&R,&C);
  V.clear();
  REP(i,R)REP(j,C)
  {
    scanf("%d",&G[i][j]);
    V.pb(mp(G[i][j],mp(i,j)));
  }
  sort(wh(V));
  mset(L,-1);
  int label=0;
  REPS(i,V)
  {
    int r=V[i].se.fi;
    int c=V[i].se.se;
//     cout<<r<<" "<<c<<endl;
    int lowest=G[r][c],lab=-1;

    REP(k,4)
    {
      int nr=r+dir[k][0];
      int nc=c+dir[k][1];
      if (nr>=0&&nc>=0&&nr<R&&nc<C&&G[nr][nc]<lowest)
        lowest=G[nr][nc],lab=L[nr][nc];                
    }
    if (lab==-1)lab=label++;
    L[r][c]=lab;
  }
  mset(maping,-1);
  label=0;
  REP(i,R)
  {
    REP(j,C)
    {
      if (j)putchar(' ');
      if (maping[L[i][j]]==-1)maping[L[i][j]]=label++;
      printf("%c",maping[L[i][j]]+'a');
    }
    putchar(10);
  }






}

int cases;
int main( )
{
  scanf("%d\n",&cases);
  while(cases--)
  {
    solve_case();    
  }  
  return 0;
}
