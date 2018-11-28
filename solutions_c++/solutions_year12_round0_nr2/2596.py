#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    int n, s, p;
    cin >> n >> s >> p;
    int sum[n];
    int ok = 0, mid = 0;
    for(int i = 0; i < n; ++i){
      cin >> sum[i];
      if(p == 0)
        ++ok;
      else if(p >= 1 && sum[i] >= p+p-1+p-1)
        ++ok;
      else if(p >= 2 && sum[i] >= p+p-2+p-2)
        ++mid;
    }
    cout << "Case #" << k+1 << ": " << ok + min(mid, s) << endl;
  }

  return 0;
}
