#include <iostream>
#include <string>
#include <vector>

using namespace std;

int good(string &x, int q) {
  for (int i = q+1; i < x.size(); ++i)
    if (x[i] == '1') return false;
  return true;
}

int main() {
  int _T;
  cin >> _T;
  for (int T = 1; T <= _T; ++T) {
    int N;
    cin >> N;
    vector<string> A;
    for (int i = 0; i < N; ++i) {
      string s;
      cin >> s;
      A.push_back(s);
    }
    int sw = 0;
    for (int i = 0; i < N; ++i) {
      int j;
      for (j = i; j < N; j++) {
        if (good(A[j],i)) {
          while (j > i) {
            sw++;
            swap(A[j],A[j-1]);
            j--;
          }
          break;
        }
      }
      //cout << i << "," << j << endl;
    }
    printf("Case #%d: %d\n", T,sw);
    
    
  }
  return 0;
}
