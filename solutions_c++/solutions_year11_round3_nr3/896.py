#include<iostream>
#include<vector>
using namespace std;

typedef vector<int> Vi;

int main() {
  int tcas;
  cin >> tcas;
  for(int cas = 0; cas < tcas; ++cas) {
    int n,l,h;
    cin >> n >> l >> h;
    Vi v(n);
    for(int i = 0; i < n; ++i) cin >> v[i];
    bool found = false;
    int res;
    for(int i = l; i <= h and not found;++i) {
      bool salir = false;
      for(int j = 0; j < n and not salir; ++j) {
	if(v[j] > i) {
	  if(v[j] % i != 0) salir = true;
	}
	else if(i % v[j] != 0) salir = true;
      }
      if(not salir) {
	found = true;
	res = i;
      }
    }
    cout << "Case #"<< cas+1 << ": ";
    if(not found) cout << "NO" << endl;
    else cout << res << endl;
  }
}