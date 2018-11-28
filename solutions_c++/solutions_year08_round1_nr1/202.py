#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
  vector<long long> x;
  vector<long long> y;
  int test, N;

  cin >> test;
  for (int tnum = 1; tnum <= test; tnum++) {
    cin >> N;
    x.resize(N);
    y.resize(N);
    for (int i = 0; i < N; i++)
      cin >> x[i];
    for (int i = 0; i < N; i++)
      cin >> y[i];

    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    reverse(x.begin(), x.end());

    long long total = 0;
    for (int i = 0; i < N; i++) 
      total += x[i]*y[i];
    cout << "Case #" << tnum << ": " << total << endl;

  }

  return 0;
}
