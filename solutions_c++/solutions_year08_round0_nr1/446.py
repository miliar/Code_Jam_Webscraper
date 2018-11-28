#include <iostream>
#include <string>
using namespace std;

int main() {
  int N;
  cin >> N;
  for (int iii = 0; iii < N; iii++) {
    char c[1024];
    int ns;
    cin >> ns;
    string s[ns];
    cin.getline(c, 1024);
    for (int i = 0; i < ns; i++) {
      cin.getline(c, 1024);
      s[i] = c;
    }
    int nq;
    cin >> nq;
    int match = 0;
    int a[ns];
    for (int i = 0; i < ns; i++) {
      a[i] = 0;
    }
    int ans = 0;
    cin.getline(c, 1024);
    for (int i = 0; i < nq; i++) {
      cin.getline(c, 1024);
      string q = c;
      for (int j = 0; j < ns; j++) {
        if (q == s[j]) {
          if (a[j] == 0 ) {
            match++;
            if (match == ns) {
              ans++;
              match = 1;
              for (int k = 0; k < ns; k++) {
                a[k] = 0;
              }
            }
            a[j] = 1;
          }
          break;
        }
      }
    }
    
    cout << "Case #" << iii + 1 << ": " << ans << endl;
  }
}
