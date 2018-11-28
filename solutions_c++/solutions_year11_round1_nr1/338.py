#include <iostream>
#include <algorithm>
using namespace std;

typedef long long lli;
int main() {
  int T;
  cin >> T;
  for(int tc = 0; tc < T; ++tc) {
    lli N;
    int Pd, Pg;
    cin >> N >> Pd >> Pg;
    cout << "Case #" << tc+1 << ": ";
    if(Pd != 100 && Pg == 100 ||
       Pd != 0 && Pg == 0) {
      cout << "Broken" << endl;
      continue;
    }
    bool flag = false;

    int cnt2 = 0, cnt5 = 0;
    int tmp = Pd;
    while(tmp % 2 == 0) {
      tmp /= 2;
      ++cnt2;
      if(cnt2 >= 2) break;
    }
    while(tmp % 5 == 0) {
      tmp /= 5;
      ++cnt5;
      if(cnt5 >= 2) break;
    }
    lli D = 1;
    for(int i = 0; i < 2-cnt2; ++i) D *= 2;
    for(int i = 0; i < 2-cnt5; ++i) D *= 5;
    if(D <= N) cout << "Possible" << endl;
    else cout << "Broken" << endl;
  }
  return 0;
}
