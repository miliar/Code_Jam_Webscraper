#include <iostream>
#include <cstring>

#define MAX 55

using namespace std;

int n, k, b, tempo;

int x[MAX];
int v[MAX];

bool poss[MAX];

int main() {
  int t;
  cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cin >> n >> k >> b >> tempo;
    for (int i = 0;i < n; i++)
      cin >> x[i];
    for (int i = 0;i < n; i++)
      cin >> v[i];

    memset(poss, false, sizeof(poss));

    int cnt = 0;

    for (int i = 0; i < n; i++) {
      //cout << x[i] << " " << v[i] << " " << tempo << " " << b << endl;
      if (x[i] + v[i]*tempo >= b) {
	//cout << "poss " << i << endl;
	poss[i] = true;
	cnt++;
      }
    }

    if (cnt < k) {
      cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
    }
    else {
      cnt = 0;
      int c = 0;
      int needed = 0;
      for (int i = n-1; i>=0 && needed < k; i--) 
	if (poss[i]) {
	  cnt+=c;
	  needed++;
	}
	else
	  c++;
      cout << "Case #" << tt << ": " << cnt << endl;
    }
  }
  return 0;
}
