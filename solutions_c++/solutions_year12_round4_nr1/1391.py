
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

struct TestCase                 // struct to hold one test case
{
  long tc_id;
} TC;

int comp(const void *v1, const void *v2)
{
  long *l1 = (long *)v1;
  long *l2 = (long *)v2;
  return *l1 - * l2;
}

//  qsort(board, 512, sizeof(board[0]), comp);

long N, D;
long d[10000], l[10000];
map<pair<long, long>, bool> dyn;

int read_test_case(long tc_id)
{
  TC.tc_id = tc_id;
  memset(d, 0, sizeof(d));
  memset(l, 0, sizeof(l));
  dyn.clear();
  fscanf(ifile, "%ld\n", &N);
  for (long i = 0; i < N; ++i) {
    fscanf(ifile, "%ld %ld\n", &d[i], &l[i]);
  } /* 'i' for loop */
  fscanf(ifile, "%ld", &D);

  return 0;
} /* read_test_case */

bool swing(long v, long len)
{
  pair<long, long> key = make_pair(v, len);
  FIND(lkup, &dyn, key);
  if (lkup != dyn.end()) return lkup->second;

  long range = d[v] + len;
  if (range >= D) return true;

  bool rslt = false;
  for (long i = v + 1; d[i] <= range; ++i) {
    rslt = swing(i, min(d[i] - d[v], l[i]));
    if (rslt) break;
  } /* 'i' for loop */
  dyn[key] = rslt;
  return rslt;
}

char *solve(long tc_id)
{
  long strid = 0;
  static char result_str[65535];

  assert(!feof(ifile));
  tc_id++; // increment tc_id so that Case # will start from 1
  read_test_case(tc_id);

  strid += sprintf(&result_str[strid], "Case #%ld: ", tc_id);

  /* SOLVE HERE */
  bool rslt = swing(0, min(d[0], l[0]));

  strid += sprintf(&result_str[strid], "%s\n", rslt ? "YES" : "NO");

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
