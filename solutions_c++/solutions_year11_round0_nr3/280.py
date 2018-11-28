#include <iostream>
#include <vector>
#include <utility>
#include <cstring>
#include <algorithm>
#include <numeric>
#include "../../print.hpp"

using namespace std;

int solve(vector<int> & c){
  int xsum = 0;
  int n = c.size();

  for(int i = 0;i<n;i++){
    xsum ^= c[i]; 
  }
  if(xsum != 0){
    return -1;
  }
  sort(c.begin(), c.end());
  int ans = accumulate(c.begin(), c.end(), 0);
  ans -= c[0];
  return ans;
}


int main(){
  int t;cin >> t;
  for(int i = 1;i<=t;i++){
    int n;cin >> n;
    vector<int> c(n);
    for(int j = 0;j<n;j++){
      cin >> c[j] ;
    }
    int ans = solve(c);
    if(ans == -1){
      cout << "Case #" << i << ": " << "NO" <<endl;
    }else{
      cout << "Case #" << i << ": " << ans <<endl;
    }
  }
  return 0;

}
