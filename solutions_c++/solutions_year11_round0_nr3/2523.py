#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;

void Solve() {
  int N;
  vector<int> numbers;
  cin >> N;
  int test = 0;
  int sum = 0;
  int min = 1000000;
  for(int i = 0; i < N; ++i) {
    int number;
    cin >> number;
    test ^= number;
    sum += number;
    if (number < min) {
      min = number;
    }
    numbers.push_back(number);
  }
  if (test) {
    cout << "NO" << endl;
    return;
  }
  cout << sum - min << endl;
}

int main() {
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i) {
    cout << "Case #" << i + 1 << ": ";
    Solve();
  }
  return 0;
}
