#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <sstream>

using namespace std;

#define iter(c) __typeof((c).begin())

#define rep(i,n) for(int i=0; i<(int)(n); i++)
#define repd(i,n) for(int i=(int)(n); i-->0;)
#define repi(i,a,b) for(int i=(int)(a); i<=(int)(b); i++)
#define times(n) for(int __times=(n); __times-->0;)
#define each(i, c) for (iter(c) i = (c).begin(); i != (c).end(); ++i)

#define all(a) (a).begin(),(a).end()
#define elem(e, c) (find(all(c), (e)) != (c).end())
#define pb push_back
#define mp make_pair
#define fst first
#define snd second

#define INF 501001001
#define INFTY (INF<<32LL|INF)
#define EPS 1e-9
#define PI 3.141592653589793

typedef long long ll;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<double> vd;
typedef vector<string> vs;

template <class T>
void debug(vector<T> v){ each(i,v.size()) cout<<*i<<" "; cout<<endl; }

int nextInt(){ int t; scanf("%d", &t); return t; }
string next(){ string t; cin>>t; return t; }

int N,P;
int M[2048];
int cost[2048][16];
int dp[2048][16][16];

int solve(int i,int j,int k){
  if(j==-1){
    if(k+M[i]>=P) return 0;
    else return INF;
  }
  if(dp[i][j][k]>=0) return dp[i][j][k];
  int i1=2*i;
  int i2=2*i+1;
  return dp[i][j][k]=min(INF,min(
	solve(i1,j-1,k)+solve(i2,j-1,k),
	cost[i][j]+solve(i1,j-1,k+1)+solve(i2,j-1,k+1)));

}

int main(){
  int T=nextInt();
  repi(cases,1,T){
    P=nextInt();
    N=1<<P;
    rep(i,N) M[i]=nextInt();
    rep(j,P) rep(i,1<<(P-j-1)){
      cost[i][j]=nextInt();
      rep(k,P) dp[i][j][k]=-1;
    }
    int ans=solve(0,P-1,0);
    cout<<"Case #"<<cases<<": ";
    cout<<ans;
    cout<<endl;
  }
  return 0;
}
