#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <cctype>
#include <functional>
#include <iomanip>
#include <complex>

using namespace std;

int n;
int value[2][10000];
int change[10000];
int gate[10000];

int fix(int cur, int val){
  if(value[val][cur] != -1)
    return value[val][cur];

  value[val][cur] = -2;

  if(cur*2+1 >= n)
    return value[val][cur];

  if(gate[cur] == 1 || change[cur] == 1){ // and
    int tmp = -2;

    if(val == 1){
      int a = fix(cur*2+1, 1), b = fix(cur*2+2, 1);

      if(a >= 0 && b >= 0)
        tmp = a + b;
    }
    else{
      int a = fix(cur*2+1, 0), b = fix(cur*2+2, 0);
      if(a >= 0 && b >= 0)
        tmp = min(a, b);
      else if(a >= 0)
        tmp = a;
      else if(b >= 0)
        tmp = b;
    }

    if(tmp >= 0 && gate[cur] != 1) ++tmp;
    if(tmp >= 0)
      value[val][cur] = value[val][cur] >= 0 ? min(value[val][cur], tmp) : tmp;
  }

  if(gate[cur] == 0 || change[cur] == 1){
    int tmp = -2;

    if(val == 1){
      int a = fix(cur*2+1, 1), b = fix(cur*2+2, 1);
      if(a >= 0 && b >= 0)
        tmp = min(a, b);
      else if(a >= 0)
        tmp = a;
      else if(b >= 0)
        tmp = b;
    }
    else{
      int a = fix(cur*2+1, 0), b = fix(cur*2+2, 0);
      if(a >= 0 && b >= 0)
        tmp = a + b;
    }

    if(tmp >= 0 && gate[cur] != 0) ++tmp;
    if(tmp >= 0)
      value[val][cur] = value[val][cur] >= 0 ? min(value[val][cur], tmp) : tmp;
  }

//   if(value[val][cur] == -2 && change[cur] == 1){
//     if(val == 0){
//       if(!(fix(cur*2+1, 1) >= 0 && fix(cur*2+2, 1) >= 0))
//         value[val][cur] = 1;
//     }
//     else{
//       if(fix(cur*2+1, 1) >= 0 || fix(cur*2+2, 1) >= 0)
//         value[val][cur] = 1;
//     }
//   }

  return value[val][cur];
}

int main(void){
  int cc = 0;
  cin >> cc;
  for(int kk = 0; kk < cc; ++kk){
    int v;
    cin >> n >> v;
    int i = 0;
    for(i = 0; i < (n-1)/2; ++i)
      cin >> gate[i] >> change[i];

    fill_n(value[0], n, -1);
    fill_n(value[1], n, -1);

    int x;
    for(int j = 0; j < (n+1)/2; ++i, ++j){
      cin >> x;
      value[x][i] = 0;
    }

    int ans = fix(0, v);
    cout << "Case #" << kk+1 << ": ";
    if(ans == -2)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << ans << endl;
  }

  return 0;
}
