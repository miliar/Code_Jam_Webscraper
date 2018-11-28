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
#include<string.h>
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
int N;
int P[1005];
int T[1005];
int DP[1<<21];
int solve_case()
{
  mset(T,0);
  mset(DP,0x3f);

  cin>>N;
  int sum=0;
  REP(i,N)
    cin>>P[i],sum+=P[i];
  sort(P,P+N);

  REP(i,25)
  {
    int cnt=0;
    REP(j,N)
      if (P[j]&(1<<i))cnt++;
    if (cnt%2)return 0;
  }
  return sum-P[0];
}

int main()
{
  int cases;
  scanf("%d",&cases);getchar();
  REP(kk,cases)
  {
    int res=solve_case();
    cout<<"Case #"<<kk+1<<": ";
    if (res==0)cout<<"NO"<<endl;
    else cout<<res<<endl;
  }
  return 0;
}


