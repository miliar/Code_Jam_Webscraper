
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
int T, C, D, N;
char SEQ[101], OUT[101];
map<char, char> opair_map, cpair_map, cresult_map;

void parse_test_case()
{
  char b1, b2, r;
  cpair_map.clear();
  cresult_map.clear();
  opair_map.clear();
  fscanf(ifile, "%d", &C);
  for (int i = 0; i < C; ++i) {
    fscanf(ifile, " %c%c%c", &b1, &b2, &r);
    cpair_map[b1] = b2;
    cpair_map[b2] = b1;
    cresult_map[b1] = r;
    cresult_map[b2] = r;
  }

  fscanf(ifile, " %d", &D);
  for (int i = 0; i < D; ++i) {
    fscanf(ifile, " %c%c", &b1, &b2);
    opair_map[b1] = b2;
    opair_map[b2] = b1;
  }

  fscanf(ifile, " %d", &N);
  fscanf(ifile, " %s\n", SEQ);
  assert(strlen(SEQ) == (unsigned int)N);
}

void exec_tt()
{
  int idx = 0;
  for (char *c = &SEQ[0]; *c != '\0'; ++c) {

    if (idx == 0) {
      OUT[idx++] = *c;
      continue;
    }

    if (cpair_map.find(*c) != cpair_map.end() and cpair_map[*c] == OUT[idx - 1]) {
      OUT[idx - 1] = cresult_map[*c];
      continue;
    }

    if (opair_map.find(*c) != opair_map.end()) {
      bool found = false;
      char o = opair_map[*c];
      for (int i = 0; i < idx; ++i) {
        if (OUT[i] == o) {
          idx = 0;
          OUT[idx] = '\0';
          found = true;
          break;
        }
      }
      if (found) continue;
    }

    OUT[idx++] = *c;
  }
  OUT[idx] = '\0';
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
    exec_tt();
    char out[4096];
    out[0] = '\0';
    int idx = 0;
    for (char *c = OUT; *c != '\0'; ++c) {
      idx += sprintf(&out[idx], "%c, ", *c);
    }
    out[idx - 2] = '\0';
    fprintf(ofile, "Case #%d: [%s]\n", i, out);
  }
  fflush(ofile);
  fclose(ifile);
  fclose(ofile);
  return 0;
}

