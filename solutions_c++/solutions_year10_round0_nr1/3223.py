#include <iostream>

using namespace std;

int main() {
  int t,i=0; cin >> t;
  while(i++<t) {
    int n, k; cin >> n >> k;
    int x = (1<<n)-1;
    bool ok = ((k & x) == x) && k;
    cout << "Case #" << i << ": " << (ok?"ON":"OFF") << endl;
  }
}
