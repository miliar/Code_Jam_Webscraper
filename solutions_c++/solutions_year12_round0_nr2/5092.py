#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
#include <functional>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

int max_unsurp(int n) {
  return n / 3 + (n % 3 > 0 ? 1 : 0);
}

int max_surp(int n) {
  if (n < 2) return -1;   //impossibe
  return (n - 2) / 3 + 2;
}

void solve(int ind) {
    int N, S, p;
    cin >> N >> S >> p;
    vector<int> totals(N);
    for (int i = 0; i < N; ++i) {
      cin >> totals[i];
    }
    //calc - try all permutations of S surprising and N-S common scores, and for each of them get the number of ponits >= p
    vector<int> surp(N, 1);
    for (int i = 0; i < N - S; ++i) {
      surp[i] = 0;
    }
    int maxp = 0, totalp;
    vector<int> best_perm;
    do {
      totalp = 0;
      for (int i = 0; i < N; ++i) {
        totalp += ((surp[i] == 1 ? max_surp(totals[i]) : max_unsurp(totals[i])) >= p ? 1 : 0);
      }
      if (totalp > maxp) {
        maxp = totalp;
        best_perm = surp;
      }
    } while (next_permutation(surp.begin(), surp.end()));
    //output
    cout << "Case #" << ind << ": " << maxp << endl;
/*    for (int i = 0; i < N; ++i) {
      cout << best_perm[i] << " ";
    }
    cout << endl;*/
}

int main() {
    int i, T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
