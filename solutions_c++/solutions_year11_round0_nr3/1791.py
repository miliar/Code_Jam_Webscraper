#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

const int MAX_BIT = 20;

int solve(int numbers[], int size) {

  vector<int> capable_bit;
  for (int i = 0; i < MAX_BIT; ++i)
    capable_bit.push_back(0);

  for (int* it = numbers; it != numbers + size; ++it) {
    int num = *it;
    int mask = 1;
    for (int i = 0; i < MAX_BIT; ++i, mask <<= 1) {
      if (num & mask) {
        ++capable_bit[i];
      }
    }
  }

  for (int i = 0; i < MAX_BIT; ++i)
    if (capable_bit[i] % 2 != 0) return -1;

  int sum = 0;
  for (int* it = numbers + 1; it != numbers + size; ++it)
    sum += *it;

  return sum;
}

int main() {
  int t;
  cin >> t;
  for (int s = 1; s <= t; ++s) {
    int n;
    cin >> n;

    int* numbers = new int[n];
    for (int* it = numbers; it != numbers + n; ++it)
      cin >> *it;

    sort(numbers, numbers + n);

    int ret = solve(numbers, n);
    delete[] numbers;

    cout << "Case #" << s << ": ";
    if (ret == -1) cout << "NO";
    else cout << ret;
    cout << endl;
  }
}
