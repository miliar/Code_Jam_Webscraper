#include <iostream>

using namespace std;

int main() {
  int t, n, k;
  cin >> t;
  for (int i=1;i<=t; i++) {
    cin >> n >> k;
    cout << "Case #" << i << ": " << ((k & ((1<<n)-1))==((1<<n)-1)?"ON":"OFF") << endl;
  }
  return 0;
}
