#include <iostream>
#include <algorithm>

using namespace std;

long solve(int n, unsigned int v[]) {
  unsigned int total = 0;
  unsigned int sum = 0;
  unsigned int min = 1 << 31;
  for (int i = 0; i < n; ++i){
    total ^= v[i];
    sum += v[i];
    if (min > v[i])
      min = v[i];
  }
  if (total != 0)
    return -1;
  return sum - min;
}

int main(char* argv[]) {
  int num_tests, n;
  unsigned int v[1000];
  cin >> num_tests;
  for (int i = 0; i < num_tests; ++i){
    cin >> n;
    for (int j = 0; j < n; ++j){
      cin >> v[j];
    }
    long ret = solve(n, v);
    cout << "Case #" << i + 1 << ": ";
    if (ret < 0)
      cout << "NO" << endl;
    else
      cout << ret << endl;
  }
  return 0;
}
