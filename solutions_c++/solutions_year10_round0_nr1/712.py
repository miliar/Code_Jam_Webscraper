#include <iostream>
using namespace std;

typedef long long ll;

int main () {
  int n; cin >> n;
  for (int i = 0; i < n; ++i) {
    ll a,b; cin >> a >> b;
    ll mask = (1<<a)-1;
    cout << "Case #" << (i+1) << ": "  << ((mask & b) == mask ? "ON" : "OFF") << endl;
  }
}
