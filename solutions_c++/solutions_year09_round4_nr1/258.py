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

int main(void)
{
  int T; cin >> T;
  for (int c = 1; c <= T; c++) {
    int N; cin >> N;
    vector <int> earliest;
    for (int i = 0; i < N; i++) {
      string str;
      cin >> str;
      int last = 0;
      for (int j = 0; j < N; j++)
	if (str[j] == '1')
	  last = j;
      earliest.push_back(last);
    }
    int ans = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < earliest.size(); j++) {
	if (earliest[j] <= i) {
	  earliest.erase(earliest.begin() + j);
	  break;
	}
	else
	  ans++;
      }
    }
    printf("Case #%d: %d\n", c, ans);
  }
  return 0;
}
