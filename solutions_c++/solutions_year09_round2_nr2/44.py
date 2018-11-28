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
string S;
string z(string s)
{
  while(sz(s)<50)s="0"+s;
  return s;
}
void solve_case()
{
  cin>>S;
  string p1=S;
  next_permutation(wh(p1));
  if (z(p1)>z(S))cout<<p1<<endl;
  else
  {
    S="0"+S;
    next_permutation(wh(S));
    cout<<S<<endl;  
  }


/*
  cin>>N;
  stringstream ss;ss<<N;
  string S;ss>>S;
  next_permutation(wh(S));
  stringstream ss2;ss2<<S;
  ll N2;ss2>>N2;
  if (N2>N) cout<<N2<<endl;
  else
  {
    stringstream ss4;ss4<<N;
    ss4>>S;
    S="0"+S;
    next_permutation(wh(S));
    stringstream ss3;ss3<<S;
    ss3>>N2;
    cout<<N2<<endl;  
  }*/
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
