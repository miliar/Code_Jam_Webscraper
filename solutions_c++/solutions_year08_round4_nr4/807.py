#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>
using namespace std;

int main() {
  int ncases;
  cin >> ncases;
  for (int casenum=1; casenum<=ncases; casenum++) {
    int k;
    string S;
    cin >> k >> S;
    int N = (int)S.size();

    vector<int> perm(k);
    for (int i=0; i<k; i++) perm[i] = i;

    int Y = INT_MAX;
    do {
      string P = S;
      for (int i=0; i<N; i+=k) {
	for (int j=0; j<k; j++) P[i+j] = S[i+perm[j]];
      }
      //cout << S << " " << P << endl;

      int groups = 1;
      for (int i=1; i<N; i++) {
	if (P[i] != P[i-1]) groups++;
      }
      Y = min(Y, groups);
    } while (next_permutation(perm.begin(), perm.end()));

    cout << "Case #" << casenum << ": " << Y << endl;
  }
  
  return 0;
}
