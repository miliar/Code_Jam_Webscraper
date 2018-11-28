#include <iostream>

using namespace std;

#define MAX_NO 1000000

int t;

int n;
int vals[MAX_NO];

static inline void reset()
{
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> vals[i];
  }
}

static inline void split(int case_cnt)
{
  if (!n) {
    cout << "Case #" << case_cnt << ": NO" << endl;
    return;
  }
  int min = vals[0];
  int sum = vals[0];
  int xor_sum = vals[0];
  for (int i = 1; i < n; ++i) {
    if (vals[i] < min)
      min = vals[i];
    sum += vals[i];
    xor_sum ^= vals[i];
  }
  if (xor_sum) {
    cout << "Case #" << case_cnt << ": NO" << endl;
    return;
  }
  cout << "Case #" << case_cnt << ": " << (sum - min) << endl;
}

int main()
{
  cin >> t;
  for (int i = 0; i < t; ++i) {
    reset();
    split(i + 1);
  }
  return 0;
}
