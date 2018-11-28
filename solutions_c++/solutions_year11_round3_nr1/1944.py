
#include <cstdio>
#include <cstring>
#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
#include <map>
#include <vector>
#include <list>

using namespace std;

char inFileName[64], outFileName[64];
FILE *ifile, *ofile;
int64_t T, R, C;

char tiles[50][50];


void parse_test_case()
{
  fscanf(ifile, "%lld %lld", &R, &C);
  for (int i = 0; i < R; ++i) {
    fscanf(ifile, "%s", &tiles[i][0]);
  }
}

bool redify(int r, int c)
{
  assert(tiles[r][c] == '#');
  if (r == R - 1 || c == C - 1) return false;
  if (tiles[r][c+1] != '#' ||
      tiles [r+1][c] != '#' ||
      tiles [r+1][c+1] != '#') return false;
  tiles[r][c] = tiles[r+1][c+1] = '/';
  tiles[r+1][c] = tiles[r][c+1] = '\\';
  return true;
}

void print_tiles()
{
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      fprintf(ofile, "%c", tiles[r][c]);
    }
    fprintf(ofile, "\n");
  }
}

int64_t exec_tt()
{

  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      if (tiles[r][c] == '#') {
        if (!redify(r, c)) return false;
      }
    }
  }
  return true;
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

  for (int64_t i = 1; i <= T; ++i) {
    parse_test_case();
    bool res = exec_tt();
    fprintf(ofile, "Case #%lld:\n", i);
    if (res) {
      print_tiles();
    } else {
      fprintf(ofile, "Impossible\n");
    }
  }

  fflush(ofile);
  char cmd[64];
  sprintf(cmd, "cat %s", outFileName);
  system(cmd);
  return 0;
}

