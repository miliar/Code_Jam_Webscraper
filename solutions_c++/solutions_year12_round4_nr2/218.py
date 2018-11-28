#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

double eps = 1e-5;

double sq(double x) { return x*x; }

int main(void) {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, W, L; cin >> N >> W >> L;
    vector <int> r(N), r_sort(N);
    for (int i = 0; i < N; i++) cin >> r[i];
    vector <int> perm(N);
    vector <bool> used(N);
    for (int i = 0; i < N; i++) {
      int max_r = 0, max_ind = -1;
      for (int j = 0; j < N; j++)
	if (!used[j] && r[j] > max_r) {
	  max_r = r[j];
	  max_ind = j;
	}
      used[max_ind] = true;
      r_sort[i] = max_r;
      perm[max_ind] = i;
    }
    /*
    for (int i = 0; i < N; i++)
      cerr << r_sort[i] << " "; cerr << endl;
    for (int i = 0; i < N; i++)
      cerr << perm[i] << " "; cerr << endl;
    */

    vector <double> x_ans(N), y_ans(N);

    for (int i = 0; i < N; i++) {
      while (true) {
	double x = rand() / (double) RAND_MAX * W;
	double y = rand() / (double) RAND_MAX * L;
	bool ok = true;
	for (int j = 0; j < i; j++)
	  if (min(sq(x-x_ans[j]), sq(fabs(x-x_ans[j])-eps)) +
	      min(sq(y-y_ans[j]), sq(fabs(y-y_ans[j])-eps))
	      < sq(r_sort[i]+r_sort[j]))
	    ok = false;
	if (ok) {
	  x_ans[i] = x; y_ans[i] = y;
	  break;
	}
      }
    }

    printf("Case #%d:", t);
    for (int i = 0; i < N; i++)
      printf(" %.6f %.6f", x_ans[perm[i]], y_ans[perm[i]]);
    printf("\n");
  }
}
