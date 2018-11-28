#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, m, best, wrongsum, a, menor;
  vector<int> candies;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    best = 0;
    candies.clear();
    cin >> m;
    for (int j = 0; j < m; j++) {
      cin >> a;
      best += a;
      candies.push_back(a);
      if (j == 0) {
        menor = a;
        wrongsum = a;
      }
      else {
        wrongsum ^= a;
      }
      if (a < menor)
        menor = a;
    }
    cout << "Case #" << i << ": ";
    if (wrongsum != 0)
      cout << "NO";
    else 
      cout << best - menor;
    cout << endl;
  }
}
