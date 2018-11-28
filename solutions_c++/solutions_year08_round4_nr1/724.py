#include<iostream>
#include<algorithm>
using namespace std;

#define infi 1000000

int main() {
  int q, cases, i, n, n1, le;
  bool b[10005], anding[10005], c[10005], v;
  int ma[10005];

  cin >> cases;
  for (q = 1; q <= cases; q++) {
    printf("Case #%d: ", q);
    cin >> n >> v;
    n1 = (n-1)/2;
    for (i = 0; i < n1; i++) {
      cin >> anding[i] >> c[i];
    }
    for (i = n1; i < n; i++) {
      cin >> b[i];
    }
    if (! v) {
      for (i = 0; i < n1; i++) anding[i] = ! anding[i];
      for (i = n1; i < n; i++) b[i] = ! b[i];
    }
    for (i = n1; i < n; i++) {
      if (b[i]) ma[i] = 0;
      else ma[i] = infi;
    }
    for (i = n1-1; i >= 0; i--) {
      le = 2*i+1;
      if (! anding[i]) {// or
	ma[i] = min(ma[le], ma[le+1]);
      }
      else { // and
	ma[i] = ma[le] + ma[le+1];
	if (c[i]) {
	  ma[i] = min(ma[i], min(ma[le], ma[le+1]) + 1);
	}
      }
    }
    if (ma[0] >= infi) cout << "IMPOSSIBLE\n";
    else cout << ma[0] << endl;;
  }
}

    /*
    for (i = n1; i < n; i++) {
      if (b[i]) {
	mi[i] = infi;
	ma[i] = 0;
      }
      else {
	mi[i] = 0;
	ma[i] = infi;
      }
    }
    for (i = n1-1; i >= 0; i--) {
      le = 2*i+1;
      rig = le+1;
      if (b[i] ==
      }*/
