#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <iterator>
#include <algorithm>

using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;
typedef unsigned int uint;

int countGroups(const string &s2) {
  int groups = 1;
  for (int i = 1; i < s2.length(); ++i)
    if (s2[i] != s2[i - 1])
      ++groups;
  return groups;
}

int compress(const string &S, vector<int> &v) {
  int k = v.size();
  string s2(S.length(), ' ');
  for (int i = 0; i < S.length() / k; ++i)
    for (int j = 0; j < k; ++j)
      s2[i * k + j] = S[i * k + v[j]];

  return countGroups(s2);
}

int main() {
  int N;
  cin >> N;

	for (int caseNumber = 1; caseNumber <= N; ++caseNumber) {
	  int k;
	  string S;
	  cin >> k >> S;

    vector<int> v(k);
    for (int i = 0; i < k; ++i)
      v[i] = i;

    int lMin = numeric_limits<int>::max();
    do {
      int l = compress(S, v);
      if (l < lMin)
        lMin = l;
    } while (next_permutation(v.begin(), v.end()));

    cout << "Case #" << caseNumber << ": " << lMin << endl;
	}
}
