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
  int N;
  cin >> N;
  for (int c = 1; c <= N; c++) {
    int k;
    cin >> k;
    string S;
    cin >> S;
    vector <int> v;
    for (int i = 0; i < k; i++)
      v.push_back(i);
    int ans = S.length();
    do {
      string T = S;
      for (int i = 0; i < S.length(); i++) {
	int ik = i%k;
	T[i-ik+v[ik]] = S[i];
      }
      int tans = 0;
      for (int i = 0; i < T.length(); i++)
	if (i == 0 || T[i] != T[i-1])
	  tans++;
      ans <?= tans;
    } while (next_permutation(v.begin(), v.end()));
    printf("Case #%d: %d\n", c, ans);
  }
}
