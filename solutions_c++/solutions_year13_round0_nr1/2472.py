
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <vector>
#include <list>
#include <unordered_set>
#include <algorithm>

using namespace std;

#define ITER(_i, _o) for(typeof((_o)->begin()) _i = (_o)->begin(); _i != (_o)->end(); ++_i)
#define FIND(_i, _o, _key) typeof((_o)->begin()) _i = (_o)->find(_key)

enum Status
{
  FAILURE = -1,
  SUCCESS = 0
};


FILE *ifile, *ofile;

long T;                          // num test cases

int read_input(const char *fbase="Sample")
{
  char fname[2048];

  // open input file with extension .in
  strncpy(fname, fbase, sizeof(fname) - 5);
  int fbase_idx = strlen(fname);
  strcpy(&fname[fbase_idx], ".in");
  ifile = fopen(fname, "r");
  assert(ifile);

  // open output file with extension .out
  strcpy(&fname[fbase_idx], ".out");
  ofile = fopen(fname, "w");
  assert(ofile);

  // scan the number of test cases
  fscanf(ifile, "%ld", &T);
  return 0;
} /* read_input */

char input[5][5];

int read_test_case(long tc_id)
{
  for (long i = 0; i < 4; ++i) {
    fscanf(ifile, "%s", &input[i][0]);
  } /* 'i' for loop */

  return 0;
} /* read_test_case */

char *solve(long tc_id)
{
  long strid = 0;
  static char result_str[65535];

  assert(!feof(ifile));
  tc_id++; // increment tc_id so that Case # will start from 1
  read_test_case(tc_id);

  strid += sprintf(&result_str[strid], "Case #%ld: ", tc_id);

  /* SOLVE HERE */
  bool blank = false;
  int h[4] = {0};
  int v[4] = {0};
  char win = '.';
  int ans = 0;
  char exp = input[0][0];
  if (exp == '.') goto skip_diag1;
  if (exp == 'T') exp = input[3][3];
  for (long i = 1; i < 4; ++i, ++ans) {
    if (input[i][i] == 'T') continue;
    if (input[i][i] != exp) break;
  } /* 'i' for loop */

  if (ans == 3) {
    win = exp;
    goto done;
  }

 skip_diag1:
  ans = 0;
  exp = input[0][3];
  if (exp == '.') goto skip_diag2;
  if (exp == 'T') exp = input[3][0];
  for (long i = 1; i < 4; ++i, ++ans) {
    if (input[i][3 - i] == 'T') continue;
    if (input[i][3 - i] != exp) break;
  } /* 'i' for loop */

  if (ans == 3) {
    win = exp;
    goto done;
  }

 skip_diag2:
  for (long i = 0; i < 4; ++i) {
    for (long j = 0; j < 4; ++j) {
      switch (input[i][j]) {
        case '.':
          blank = true;
          h[i] = -1;
          v[j] = -1;
          break;
        case 'X':
          if (h[i] == 0) h[i] = 'X';
          else if (h[i] != 'X') h[i] = -1;
          if (v[j] == 0) v[j] = 'X';
          else if (v[j] != 'X') v[j] = -1;
          break;
        case 'O':
          if (h[i] == 0) h[i] = 'O';
          else if (h[i] != 'O') h[i] = -1;
          if (v[j] == 0) v[j] = 'O';
          else if (v[j] != 'O') v[j] = -1;
          break;
        default:
          break;
      }
    } /* 'j' for loop */
  } /* 'i' for loop */

  for (long i = 0; i < 4; ++i) {
    if (h[i] == 'X' || v[i] == 'X') {
      win = 'X';
      goto done;
    } else if (h[i] == 'O' || v[i] == 'O') {
      win = 'O';
      goto done;
    }
  } /* 'i' for loop */

 done:
  if (win == 'X' || win == 'O') {
    strid += sprintf(&result_str[strid], "%c won", win);
  } else if (blank) {
    strid += sprintf(&result_str[strid], "Game has not completed");
  } else {
    strid += sprintf(&result_str[strid], "Draw");
  }
  strid += sprintf(&result_str[strid], "\n");
  return result_str;
} /* solve */

int main(int argc, char *argv[])
{
  char *str;
  read_input(argc > 1 ? argv[1] : "Sample");
  for (long i = 0; i < T; ++i) {
    str = solve(i);
    fprintf(ofile, "%s", str);
    fprintf(stderr, "%s", str);
  }
  return 0;
}
