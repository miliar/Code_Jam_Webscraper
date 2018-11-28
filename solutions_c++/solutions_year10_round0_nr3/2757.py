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

#define eps 10e-10
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
typedef long double ld;
using namespace std;
ll R,k,N;
int G[1005];
int CNT[1005];
int EUR[1005];



void solve_case()
{
  cin>>R>>k>>N;
  long long total_people=0;
  REP(i,N)
    scanf("%d",&G[i]),total_people+=G[i],CNT[i]=-1;
  if (total_people<=k)
  {
    cout<<total_people*R<<endl;
    return ;
  }

  //now we can not take everybody at the same time

  long long cur=0,step=0;
  long long eur=0;
  bool wasJump=0;
//   cout<<"go:"<<endl;
  while(step<R)
  {
//     cout<<step<<" "<<cur<<" "<<CNT[cur]<<endl;
    if (CNT[cur]!=step && CNT[cur]!=-1 && wasJump==false)
    {//cyklime?
//       cout<<"jump"<<endl;
      wasJump=true;
      ll cycle_length=step-CNT[cur];
      ll cycle_eur=eur-EUR[cur];
      ll cycles=(R-step)/cycle_length;
      step+=cycles*cycle_length;
      eur+=cycles*cycle_eur;
    }else
    {//normalny krok
      ll sum=0;
      while(sum+G[cur]<=k)
      {
        sum+=G[cur];        
        cur=(cur+1)%N;      
      }
      step++;
      eur+=sum;
      if (CNT[cur]!=-1)
      {
        CNT[cur]=step;
        EUR[cur]=eur;
      }
    }
  }
  cout<<eur<<endl;
}


int cases;
int main( )
{
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    printf("Case #%d: ",ii+1);
    solve_case();
  }         
  return 0;
}
