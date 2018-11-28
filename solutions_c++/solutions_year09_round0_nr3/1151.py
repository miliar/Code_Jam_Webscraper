#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

const string welcome = "welcome to code jam";

int main(void)
{
  int N; cin >> N;
  string line; getline(cin, line);
  for (int c = 1; c <= N; c++) {
    getline(cin, line);
    vector <int> freqs(20); freqs[0] = 1;
    for (int i = 0; i < line.length(); i++)
      for (int j = 18; j >= 0; j--)
	if (line[i] == welcome[j]) {
	  freqs[j+1] += freqs[j];
	  freqs[j+1] %= 10000;
	}
    printf("Case #%d: %04d\n", c, freqs[19]);
  }
  return 0;
}
