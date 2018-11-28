#include <iostream>

#define MAX 110

using namespace std;

int n,s,p;
int v[MAX];

int main() {
  int tt;
  cin >> tt;
  for (int t = 0; t<tt; t++) {
    cin >> n >> s >> p;
    for (int i = 0; i<n; i++)
      cin >> v[i];

    int ns = 0, ps = 0;
    for (int i = 0; i<n; i++) {
      int k = v[i]/3;
      int r = v[i]%3;
      if (v[i] == 0) {
	if (p == 0) ns++;
	continue;
      }
      if (k >= p || (r > 0 && k+1>=p)) {
	//cout << "ns " << v[i] << endl;
	ns++;
      }
      else {
	if (r < 2 && k+1 >= p) {
	  //cout << "ps " << v[i] << endl;
	  ps++;
	}
	if (r == 2 && k+2 >= p) {
	  //cout << "ps " << v[i] << endl;
	  ps++;
	}
      }
    }
    
    cout << "Case #" << t+1 << ": " << ns+min(ps,s) << endl;
  }
  return 0;
}
