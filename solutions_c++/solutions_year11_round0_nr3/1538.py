#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long ll;

const int N = 1<<20;

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    int n, cs[1000];
    int x = 0, sum = 0;
    cin >> n;
    for(int i = 0; i < n; ++i){
      cin >> cs[i];
      x ^= cs[i];
      sum += cs[i];
    }
    sort(cs, cs+n);
    cout << "Case #" << k+1 << ": ";
    if(x == 0)
      cout << sum - cs[0] << endl;
    else
      cout << "NO" << endl;
  }


  return 0;
}
