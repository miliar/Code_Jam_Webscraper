#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <assert.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define debug2(x)  cerr << #x << " = [";REP(__ind,(x).size()){cerr << (x)[__ind] << ", ";}cerr << "] (L" << __LINE__ << ")" << endl;



#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizeof(a))
#define pb push_back

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;


//x^y%d
int powmod(int x,int n,int d){
  if(n==0)return 1;
  int s=x%d,t=x%d,u=n-1;
  while(u){
    if(u%2) s=(s*t)%d;
    t=(t*t)%d;
    u/=2;
  }
  return s;
}

ll getl(){
  ll ret;
  scanf("%I64d", &ret);
  return ret;
}

vl primes;

bool isPrime(int p){
  FOR(k,2,p){
    if(k*k>p)return true;
    if(p%k==0)return false;
  }
  return true;
}

void mp(){
  FOR(p,2,1000000){
      if(isPrime(p)){
        primes.push_back(p);
      }
    if(p>1000010)break;
  }
}

ll solve(ll n){
  ll ret=0;
  if(n==1)return 0;
  REP(i,primes.size()){
    ll p=primes[i];
    ll nn=n/p/p;
    while(nn>0){
      ret++;
      nn/=p;
    }
  }
  return ret+1; 
}

int main(){
  ll T=getl();
  mp();
  //debug(primes.size());
  REP(i,20){
    //debug(primes[i]);
  }
  REP(test,T){
    ll n=solve(getl());
    printf("Case #%d: %d\n", test+1, n);
  }
  return 0;
}


