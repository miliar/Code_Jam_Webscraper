
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

#define M 600
#define MOD 100003
long long choose[M+1][M+1];
void InitChoose()
{
  REP(i,M)choose[i][0]=choose[i][i]=1;
	REP(i,M)
	  REP(j,i)
	    choose[i+1][j+1]=(choose[i][j]+choose[i][j+1])%MOD;
}

int DP[600][600];
long long solve(int kde, int co)
{
  if(DP[kde][co]!=-1) return DP[kde][co];
  if(kde==1) return 1;
  long long res=0;
  //cout<<co<<" "<<kde<<endl;
  for(int i=1;i<kde;i++)
  {
    if(co-kde-1<0 || kde-i-1<0) continue;
    int add = (solve(i,kde)*choose[co-kde-1][kde-i-1])%MOD;
//    cout<<"pridavam "<<i<<" "<<kde<<"  = "<<add<<endl;
    res+= add;
    res%=MOD;
  }
  DP[kde][co]=res;
  return res;
}

int N;
void solve_case(int cases)
{
  scanf("%d",&N);
  mset(DP,-1);
  long long res=0;
  for(int i=1;i<=N;i++)
  {
    res+=solve(i,N);
    res%=MOD;
  }
  cout<<"Case #"<<cases+1<<": "<<res<<endl;
}


int cases;
int main( )
{
  InitChoose();
  scanf("%d",&cases);getchar();
  REP(ii,cases)
  {
    solve_case(ii);
  }         
  return 0;
}

