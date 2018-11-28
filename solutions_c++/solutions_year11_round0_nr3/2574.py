#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <ctime> 
 
using namespace std; 

int main () { 
  int t, T; 

  cin >> T; 
  for (t = 1; t <= T; t++) {
    int n, N;
    cin >> N;
    vector <int> c (N);
    for (n = 0; n < N; n++)
      cin >> c[n];
    int s = c[0];
    for (n = 1; n < N; n++)
      s ^= c[n];
    cout << "Case #" << t << ": ";
    if (s != 0) {
      cout << "NO" << endl;
      continue;
    }
    sort (c.begin (), c.end ());
    s = 0;
    for (n = 1; n < N; n++)
      s += c[n];
    cout << s << endl;
  }
  return 0; 
}
