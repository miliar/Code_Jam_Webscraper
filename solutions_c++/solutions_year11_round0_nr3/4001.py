#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

int rec(const int& N, int pos, int sum_val_1, int sum_val_2, bitset<20> sum_bit_1, bitset<20> sum_bit_2, const vector<int>& vi, const vector<bitset<20> >& vbit) {
  int res;
  if (pos == N) {
    if (sum_val_1 == 0 || sum_val_2 == 0) res = -1;
    else if (sum_bit_1 == sum_bit_2) {
      res = max(sum_val_1, sum_val_2);
    } else {
      res = -1;
    }
  } else {
    res = max(rec(N, pos+1, sum_val_1+vi[pos], sum_val_2, sum_bit_1^vbit[pos], sum_bit_2, vi, vbit),
	      rec(N, pos+1, sum_val_1, sum_val_2+vi[pos], sum_bit_1, sum_bit_2^vbit[pos], vi, vbit));
  }
  return res;
}

int main() {
  int T; cin >> T;
  for (int test_case_num = 1; test_case_num <= T; ++test_case_num) {
    int N; cin >> N;
    vector<int> vi;
    vector<bitset<20> > vbit;
    for (int i = 0; i < N; ++i) {
      int t; cin >> t;
      vi.push_back(t);
      vbit.push_back( bitset<20>((long)t) );
    }
    int res = rec(N, 0, 0, 0, bitset<20>(0l), bitset<20>(0l), vi, vbit);
    if (res > 0) {
      cout << "Case #" << test_case_num << ": " << res << endl;
    } else {
      cout << "Case #" << test_case_num << ": " << "NO" << endl;
    }
  }
  return 0;
}
