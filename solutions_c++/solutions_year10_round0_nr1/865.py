#include <iostream>
using namespace std;
typedef long long ll;


int main() {
  int nt, C = 1;
  cin >> nt;
  ll n, k;
  while (nt-- && cin >> n >> k) {
    k %= (1LL << n);
    cout << "Case #" << C++ << ": "
	 << (k == (1LL << n)-1 ? "ON" : "OFF")
	 << endl;
  }
}
