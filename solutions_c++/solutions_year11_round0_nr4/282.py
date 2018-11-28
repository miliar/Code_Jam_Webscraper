#include <iostream>
#include <vector>
#include <utility>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <iomanip>
#include "../../print.hpp"

using namespace std;

typedef long long ll;

/*
vector<double> memo(1001, -1);
vector<int> f_memo(10001, -1);
vector<vector<double> > h_memo(1001, vector<double> (1001, -1) ) ;


ll frac(int n){
  if(f_memo[n] >= 0) return f_memo[n];
  if(n == 0) return 1;
  return f_memo[n] = n * (frac(n-1));
}

double h(int n, int m){
  if(n == m) return h_memo[n][m] = 1/(double)frac(n);
  if(n - m == 1) return 0;
  if(h_memo[n][m] >= 0) return h_memo[n][m];  
  h_memo[n][m] = ( (n - m - 1)* h(n-1, m) + h(n-2, m))/(double)(n-m);
  return h_memo[n][m] ;
}

double E(int n){
  if(memo[n] >= 0) return memo[n];
  if(n == 0) return 0;
  if(n == 1) return 0;
  double ret = 0;
  for(int m = 0;m < n;m ++){
    ret += E(m) * h(n, n-m);
    //    cout << n << " " << m << " " << E(m) << " " << h(n, m) <<endl;
  }
  ret = (ret + 1)/ (double)(1- h(n,0));
  //  cout << n << " " << ret  <<endl;
  return memo[n] = ret ;
}
*/

double solve(vector<int> & c){
  int mismatch = 0;
  for(int i = 0;i<c.size();i++){
    if(c[i] != i){
      mismatch++;
    }
  }
  return mismatch;
  //return E(mismatch);
}


int main(){
  int t;cin >> t;
  for(int i = 1;i<=t;i++){
    int n;cin >> n;
    vector<int> c(n);
    for(int j = 0;j<n;j++){
      cin >> c[j] ;
      c[j] --;
    }
    double ans = solve(c);
    cout << "Case #" << i << ": " << setprecision(10) << ans << endl;
      
  }
  return 0;

}
