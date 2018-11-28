#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main(void){
  int c;
  int cnt[1000];
  cin >> c;
  for(int m = 0; m < c; ++m){
    int p, k, l;
    cin >> p >> k >> l ;

    for(int i = 0; i < l; ++i)
      cin >> cnt[i];

    sort(cnt, cnt+l, greater<int>());
    unsigned long long res = 0;
    int cur = 0, depth = 0;
    bool no = false;

    for(int i = 0; i < l; ++i){

      if(depth == p){
        no= true;
        break;
      }

      res += cnt[i] * (depth + 1);

      ++cur;
      if(cur == k){
        cur = 0;
        ++depth;
      }
    }

    cout << "Case #" << m+1 << ": ";
    if(no)
      cout << "Impossible" << endl;
    else
      cout << res << endl;
  }

  return 0;
}
