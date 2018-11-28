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
#define MOD 100003
#define MAXN 505
int DP[MAXN][MAXN][MAXN];

int solve(int ind,int N,int K)
{
  int &res=DP[ind][N][K];
  
//   cout<<"solving : "<<N<<" "<<K<<endl;

  if (N==1) res=K==0;
  else if (K==0) res=1;
  else if (ind==1)res=0;
  if (res!=-1)
  {
//     cout<<s<<N<<" "<<K<<" = "<<res<<endl;
//     cout<<"result: "<<res<<endl;
    return res;
  }
  res=0;
  
  if (ind==N)
  {//musime ho vziat a posunieme N
    if (ind-1>=K+1)
      res=solve(ind-1,K+1,K-1);
  }else
  {//nemusime ho vziat
    res=solve(ind-1,N,K-1);//vzali sme
    res+=solve(ind-1,N,K);//nevzali sme
    res%=MOD;
  }

/*
  int nas=1;
  int newPos=K+1;
  int slotov=N-newPos-1;
//   cout<<"slotov : "<<slotov<<endl;
  res=0;

  FOR(i,0,slotov)
  if (i+1<=K)
  {//i cisiel bolo medzi newPos a N
    ll cur=solve(newPos,K-i-1,s+"  ");
//     cur*=nas;
    cur%=MOD;
    res=(res+cur)%MOD;
    nas=(nas*2)%MOD;
  }*/
//   cout<<s<<N<<" "<<K<<" = "<<res<<endl;
  return res;
}
void solve_case()
{
  int N;cin>>N;
  int total=0;
//   cout<<"solving : "<<N<<endl;
  FOR(i,0,N-1)
    total=(total+solve(N,N,i))%MOD;
  cout<<total<<endl;
  


}


int cases;
int main( )
{
  mset(DP,-1);
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    printf("Case #%d: ",ii+1);
    solve_case();
    
  }         
  return 0;
}
