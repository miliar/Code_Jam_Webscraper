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
#include<cassert>
#include <queue>
#include<cstdlib>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)      REP(i,0,n)
#define pb push_back 
#define mp make_pair
#define ALL(C)   (C).begin(),(C).end()
template<class T> void vp(T &a,int p){rep(i,p)cout << a[i]<<" ";cout << endl;} 
const double eps = 1e-10;
typedef complex<double>P;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;

bool isok(vector<int> &in,double l,int d){
  //vector<double> t;
  double prev=in[0]+l;
  //t.pb(prev);
  REP(i,1,in.size()){
    if (prev-d < in[i]){
      //cout << prev-d <<" " << in[i] <<" ;: " << l << endl;
      if (in[i]-l > prev-d)return false;
      prev=(prev-d);
    }else {//if (prev-d > in[i]){
      prev=min(prev-d,in[i]+l);
    }
    //t.pb(prev);
  }
  //vp(t,t.size());
  //cout << l << endl;
  //  rep(i,t.size()-1)//assert(t[i+1]-t[i] >= d-eps);
    //if (t[i]-t[i+1] < d+eps)return false;
  //    cout << t[i+1]-t[i]<<" ";
  //  cout << endl;
  return true;
}

double solve(vector<int> &in,int d){
  double l=0,r=1e30,ans=-1;
  rep(i,200){
    double mid=(l+r)/2;
    if (isok(in,mid,d))r=mid-eps,ans=mid;
    else l=mid+eps;
  }
  return ans;
}

main(){
  int te;
  cin>>te;
  rep(tc,te){
    int d,c;
    cin>>c>>d;
    vector<int> in;
    rep(i,c){
      int p,num;
      cin>>p>>num;
      rep(j,num)in.push_back(p);
    }
    reverse(in.begin(),in.end());
    printf("Case #%d: %.10lf\n",tc+1,solve(in,d));
  }
  return false;
}
