#include <iostream>
#include <vector>
using namespace std;

int main () {
  int T; cin >> T;
  for (int C = 0; C < T; ++C) {
    int N; cin >> N;
    vector<int> a(N),b(N);
    for (int i = 0; i < N; ++i) {
      cin >> a[i] >> b[i];
    }
    int sum = 0;
    for (int i = 0; i < N; ++i) {
      for (int j = i+1; j < N; ++j) {
	if ((a[i]-a[j])*(b[i]-b[j]) < 0) ++sum;
      }
    }
    cout << "Case #" << C+1 << ": " << sum << endl;
  }
  
}
