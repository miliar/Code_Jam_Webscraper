#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>

FILE* input;
FILE* output;

using namespace std;

void solveone(int tc) {
  int p,q;
  fscanf(input, "%d %d\n", &p, &q);
  typedef vector<int> VI;

  VI qv;

  for (int i = 0; i < q; ++i) {
    int t;
    fscanf(input, "%d", &t);
    qv.push_back(t-1);
  }
  sort(qv.begin(), qv.end());

  long long int minBribe = 0xffffffff;

//  fprintf(stderr, "QQQQQ\n\n");
  do {
/*    for (int i =0; i < qv.size(); ++i) {
      fprintf(stderr, "qv[%d]=%d\n", i, qv[i]);
      }*/

    VI pv(p, 1);
    long long bribe = 0;
    for (int i = 0; i < qv.size(); ++i) {
      pv[qv[i]] = 0;
      for (int j = qv[i] - 1; j >= 0; j--) {
        if (pv[j] == 0) {
          break;
        }
        bribe++;
      }
      for (int j = qv[i] + 1; j < p; ++j) {
        if (pv[j] == 0) {
          break;
        }
        bribe++;
      }
    }
    if (minBribe > bribe) {
      minBribe = bribe;
    }
  } while (next_permutation(qv.begin(), qv.end()));
  fprintf(output, "Case #%d: %lld\n", tc, minBribe);
}


void solve() {
  int n;
  fscanf(input, "%d\n", &n);
  for (int i = 0; i < n; ++i) {
    solveone(i+1);
  }
}

int main(int argc, char** argv) {
  if (argc >= 2 ) {
    input = fopen(argv[1], "r");
    if (input == NULL) {
      fprintf(stderr, "could not open input file\n");
      exit(1);
    }
  }
  else {
    input = stdin;
  }
  
  if (argc >= 3) {
    output = fopen(argv[2], "w");
    if (output == NULL) {
      fprintf(stderr, "could not open output file\n");
      exit(2);
    }
  }
  else {
    output = stdout;
  }

  solve();
}
