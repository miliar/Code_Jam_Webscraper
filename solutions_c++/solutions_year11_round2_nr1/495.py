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
#include<cstdlib>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)      REP(i,0,n)
#define pb push_back 
#define mp make_pair
#define ALL(C)   (C).begin(),(C).end()
template<class T> void vp(T &a,int p){rep(i,p)cout << a[i]<<" ";cout << endl;} 

typedef complex<double>P;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
ll gcd(ll a,ll b){return b==0?a:gcd(b,a%b);}
const int N = 200;
char in[N][N];
int x[N],y[N];
double wp[N],owp[N],oowp[N];

void solve(int n){
  rep(i,n){
    x[i]=0,y[i]=0;
    rep(j,n){
      if (in[i][j] == '1')y[i]++,x[i]++;
      if (in[i][j] == '0')x[i]++;
    }
    wp[i]=y[i]/(double)x[i];
  }

  rep(i,n){
    owp[i]=0;
    rep(j,n){
      if (in[i][j] == '1'){
	owp[i]+=y[j]/(double)(x[j]-1);
      }else if (in[i][j] == '0'){
	owp[i]+=(y[j]-1)/(double)(x[j]-1);
      }
    }
    owp[i]*=1/(double)x[i];
  }
  
  rep(i,n){
    oowp[i]=0;
    rep(j,n){
      if (in[i][j] != '.')oowp[i]+=owp[j];
    }
    oowp[i]*=1/(double)x[i];
  }
}

main(){
  int te;
  cin>>te;
  rep(tc,te){
    int n;
    cin>>n;
    rep(i,n)cin>>in[i];
    solve(n);
    cout <<"Case #" << tc+1  << ":" << endl;
    rep(i,n){
      printf("%.10lf\n",0.25*wp[i]+
	     0.50*owp[i]+
	     0.25*oowp[i]);
    }
  }
  return false;
}
