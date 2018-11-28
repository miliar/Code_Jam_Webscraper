
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
int64_t T, N, M;

int64_t d[101][101];

struct Team
{
  int team;
  int64_t games;
  int64_t wins;
  int64_t loss;

  int64_t wp;
  int64_t owp;
  int64_t oowp;
  int64_t rpi;
};

Team teams[101];

const int64_t W = 1000000000000;
void parse_test_case()
{
  fscanf(ifile, "%lld", &N);
  for (int i = 1; i <= N; ++i) {
    Team *t = &teams[i];
    t->team = i;
    t->games = t->wins = t->loss = t->wp = t->owp = t->oowp = t->rpi = 0;
    char c[101];
    fscanf(ifile, "%s", &c[1]);
    for (int j = 1; j <= N; ++j) {
      switch (c[j]) {
        case '1':
          d[i][j] = W;
          t->wins += W;
          t->games++;
          break;
        case '0':
          d[i][j] = 0;
          t->loss++;
          t->games++;
          break;
        case '.':
          d[i][j] = -1000;
          break;
        default:
          assert(0);
      }
    }
  }
}

void wp(int z)
{
  Team *t = &teams[z];
  t->wp = t->wins/t->games;
}

void owp(int z)
{
  Team *t = &teams[z];
  int64_t owp = 0;
  int oteams = 0;
  
  for (int i = 1; i <= N; ++i) {
    int64_t owin = d[i][z];
    if (owin < 0) continue;
    Team *ot = &teams[i];
    oteams++;
    owp += ((ot->wins - owin) / (ot->games - 1));
  }
  t->owp = owp/oteams;
}

void oowp(int z)
{
  Team *t = &teams[z];
  int64_t oowp = 0;
  int oteams = 0;

  for (int i = 1; i <= N; ++i) {
    int64_t owin = d[i][z];
    if (owin < 0) continue;
    Team *ot = &teams[i];
    oteams++;
    oowp += ot->owp;
  }
  t->oowp = oowp/oteams;
}

void rpi(int z)
{
  Team *t = &teams[z];
  t->rpi = (0.25 * t->wp) + (0.5 * t->owp) + (0.25 * t->oowp);
}

void exec_tt()
{
  for (int i = 1; i <= N; ++i)
    wp(i);
  for (int i = 1; i <= N; ++i)
    owp(i);
  for (int i = 1; i <= N; ++i)
    oowp(i);
  for (int i = 1; i <= N; ++i)
    rpi(i);
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
    exec_tt();
    fprintf(ofile, "Case #%lld:\n", i);
    fprintf(stderr, "Case #%lld:\n", i);
    for (int j = 1; j <= N; ++j) {
      Team *t = &teams[j];
      fprintf(ofile, "%.12f\n", ((double)t->rpi)/W);
      fprintf(stderr, "%.12f\n", ((double)t->rpi)/W);
    }
  }

  fflush(ofile);
  return 0;
}

