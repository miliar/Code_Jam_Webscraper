
#include <cstdio>
#include <cstring>
#include <assert.h>
#include <stdint.h>
#include <map>
#include <vector>
#include <list>

using namespace std;

typedef unsigned long long int uulong;

char inFileName[64], outFileName[64];
FILE *ifile, *ofile;
uulong T, N, Pd, Pg;

void parse_test_case()
{
  fscanf(ifile, "%llu %llu %llu", &N, &Pd, &Pg);
}

char *exec_tt()
{
  if (Pg >= 100 and Pd < 100) return (char *)"Broken";
  if (Pg == 0 and Pd > 0) return (char *)"Broken";
  if (N >= 100) return (char *)"Possible";
  for (uulong i = 1; i <= N; ++i) {
    if ((i * Pd) % 100) continue;
    return (char *)"Possible";
  }
  return (char *)"Broken";
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
  fscanf(ifile, "%lld", &T);

  for (uulong i = 1; i <= T; ++i) {
    parse_test_case();
    fprintf(ofile, "Case #%llu: %s\n", i, exec_tt());
    fprintf(stderr, "Case #%lld: %s\n", i, exec_tt());
  }

  fflush(ofile);
  return 0;
}

