#include <string>
#include <map>
#include <iostream>

using namespace std;

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t = 0; 
  cin >> t;
  for(int i = 0; i < t; ++i) {
    int n, s, p;
    cin >> n >> s >>p;
    int ans = 0;
    for(int j = 0; j < n; ++j) {
      int a = 0;
      cin >> a;
      if(a%3 == 0) {
        if(a/3 >= p) {
          ++ans;
        } else {
          if(a/3 > 0 && s > 0 && a/3+1 >= p) {
            ++ans;
            --s;
          }
        }
      }
      if(a%3 == 1) {
        if(a/3 + 1 >= p) {
          ++ans;
        }
      } if(a%3 == 2) {
        if(a/3 + 1 >= p) {
          ++ans;
        } else {
          if(a/3+1 > 0 && s > 0 && a/3+2 >= p) {
            ++ans;
            --s;
          }
        }          
      }
    }
    
    cout << "Case #" << i+1 << ": " << ans << endl;
  }

  return 0;
}
