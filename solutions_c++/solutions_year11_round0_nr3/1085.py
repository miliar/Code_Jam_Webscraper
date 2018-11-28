#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int c[1000];
int n;

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    cout << "Case #" << tcase << ": ";

    cin >> n;
    for(int i=0;i<n;i++)
      cin >> c[i];

    sort(&c[0], &c[n]);

    int x = 0, s = 0;
    for(int i=0;i<n;i++){
      x ^= c[i];
      s += c[i];
    }
    if(x)
      cout << "NO\n";
    else
      cout << s - c[0] << "\n";
  }
}
