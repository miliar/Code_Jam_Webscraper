#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <string>

using namespace std;

FILE* input;
FILE* output;

int n;

void solveone(int casee) {
  char tmp[100];
  string s;
  bool found[256];
  int digit[256];
  
  fscanf(input, "%s\n", &tmp[0]);
  s = tmp;

  for (int i=0; i < 255; ++i) {
    found[i] = false;
    digit[i] = -1;
  }
  
  int base = 0;
  for(int i = 0; i < s.size(); ++i) {
    if (!found[s[i]]) {
      found[s[i]] = true;
      ++base;
    }
  }
  if (base < 2) {
    base = 2;
  }

  digit[s[0]] = 1;
  int curdigit = 0;
  long long result = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (digit[s[i]] == -1) {
      digit[s[i]] = curdigit;
      curdigit++;
      if (curdigit == 1) {
        curdigit++;
      }
    }
    result*=base;
    result+=digit[s[i]];
  }
  fprintf(output, "Case #%d: %lld\n", casee, result);  
}

void solve() {
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
