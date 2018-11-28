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
  int L, D, N;
  cin >> L >> D >> N;
  vector <string> words(D);
  for (int d = 0; d < D; d++)
    cin >> words[d];

  for (int c = 1; c <= N; c++) {
    string pattern; cin >> pattern;
    vector <bool> good(D, true);
    int pos = 0;
    for (int l = 0; l < L; l++) {
      vector <bool> char_ok(26);
      if (pattern[pos] == '(') {
	pos++;
	while (pattern[pos] != ')')
	  char_ok[pattern[pos++]-'a'] = true;
	pos++;
      }
      else
	char_ok[pattern[pos++]-'a'] = true;
      for (int d = 0; d < D; d++)
	if (!char_ok[words[d][l]-'a'])
	  good[d] = false;;
    }
    printf("Case #%d: %d\n", c, count(good.begin(), good.end(), true));
  }
  return 0;
}
