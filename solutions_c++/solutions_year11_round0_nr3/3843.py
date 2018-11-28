
#include <cstdio>
#include <cstring>
#include <assert.h>
#include <stdint.h>
#include <map>
#include <vector>
#include <list>

using namespace std;

char inFileName[64], outFileName[64];
FILE *ifile, *ofile;
int T, N;
int SEQ[101];

void parse_test_case()
{
  fscanf(ifile, "%d\n", &N);
  for (int i = 0; i < N; ++i) {
    fscanf(ifile, "%d", &SEQ[i]);
  }
}

char *exec_tt()
{
  static char buf[32];
  int total = SEQ[0];
  for (int i = 1; i < N; ++i) {
    total ^= SEQ[i];
  }

  if (total) {
    sprintf(buf, "NO");
    return buf;
  }

  int smallest = SEQ[0];
  for (int i = 0; i < N; ++i) {
    if (smallest > SEQ[i]) smallest = SEQ[i];
    total += SEQ[i];
  }
  total -= smallest;

  sprintf(buf, "%d", total);
  return buf;
}

int main(int argc, char *argv[])
{
  printf("Enter the input file: ");
  scanf("%s", inFileName);
  sprintf(outFileName, "%s.out", inFileName);
  sprintf(&inFileName[strlen(inFileName)], ".in");
  printf("Input File: %s\n", inFileName);
  printf("Output File: %s\n", outFileName);
  ifile = fopen(inFileName, "r");
  ofile = fopen(outFileName, "w");
  fscanf(ifile, "%d", &T);

  for (int i = 1; i <= T; ++i) {
    parse_test_case();
    fprintf(ofile, "Case #%d: %s\n", i, exec_tt());
  }
  fflush(ofile);
  fclose(ifile);
  fclose(ofile);
  return 0;
}

