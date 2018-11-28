#include <iostream>
#include <string>
#include <vector>
#include <fstream>

#define LL long long
using namespace std;

int main() {
  ifstream fin("data.in");
  ofstream fout("data.out");
  int T;
  fin >> T;
  int R, k, N, g;
  for (int i = 0; i < T; i++) {
    fin >> R >> k >> N;
    vector<int> vec;
    for (int j = 0; j < N; j++) {
      fin >> g;
      vec.push_back(g);
    }
    int ptr = 0, size = vec.size();
    LL counter = 0;
    int j;
    for (j = 0; j < R;) {
      int cap = 0;
      for (int m = 0; (cap + vec[ptr]) <= k && m < size; m++) {
        cap += vec[ptr];
        ptr = (ptr == (size - 1)) ? 0 : (ptr + 1);
      }
      counter += cap;
      j++;
      if (ptr == 0)
        break;
    }
    if (j < R) {
      int round = R / j;
      counter *= round;
      j *= round;
    }
    for (; j < R; j++) {
      int cap = 0;
      for (int m = 0; (cap + vec[ptr]) <= k && m < size; m++) {
        cap += vec[ptr];
        ptr = (ptr == (size - 1)) ? 0 : (ptr + 1);
      }
      counter += cap;
      if (ptr == 0)
        break;
    }
    fout << "Case #" << i + 1 << ": " << counter << endl;
    cout << "Case #" << i + 1 << ": " << counter << endl;
  }
  fout.close();
  fin.close();
}
