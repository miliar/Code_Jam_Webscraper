#include <iostream>

using namespace std;

int main() {

  unsigned int R, k, N, T;
  unsigned int g[1000], isum[1000], np[1000];
  cin >> T;
  for (int i=0; i < T; ++i) {
     cin >> R;
     cin >> k;
     cin >> N;
     for (int j=0; j < N; ++j) {
	   cin >> g[j]; isum[j] = 0;
      }
     unsigned long long e = 0;
     int p = 0;
     for (int j=0; j < R; ++j) {
	int ip = p;
	int s = isum[ip];
	if (!s) {
	    while (s + g[p] <= k) {
	        s += g[p];
	        p = (p+1)%N;
	        if (p == ip)
	           break;
	    }
	    isum[ip] = s;
	    np[ip] = p;
	} else
	    p = np[p];
        e += s;
     }
     cout << "Case #" << i+1 << ": " << e << "\n";
  }

}
