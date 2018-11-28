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
 
long long gcd (long long x, long long y)
{
  long long t;
  while (y) {
    t = y;
    y = x % y;
    x = t;
  }
  return x;
}

int main () { 
  int t, T; 

  cin >> T; 
  for (t = 1; t <= T; t++) {
    int N;
    long long L, H;
    cin >> N >> L >> H;
    long long f[N];
    for (int n = 0; n < N; n++) {
      cin >> f[n];
    }
    cout << "Case #" << t << ": ";
    bool flag;
    for (int g = L; g <= H; g++) {
      flag = true;
      for (int n = 0; n < N; n++)
	if ((f[n] >= g) && (f[n] % g != 0)) {
	  flag = false;
	  break;
	}
	else if ((f[n] <= g) && (g % f[n] != 0)) {
	  flag = false;
	  break;
	}
      if (flag) { cout << g << endl; break; }
    }
    if (flag == false) cout << "NO" << endl;
  }
  return 0; 
}
