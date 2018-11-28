#include <cstdio>
#include <cstring>

using namespace std;

int havea[16384];
int haveb[16384];
int musta[16384];
int mustb[16384];

int convert(int h, int m)
{
  return h * 60 + m;
}

int solve(int *have, int *must)
{
  const int maxim = 24 * 60;

  int added = 0;
  int current = 0;
  for (int i = 0; i < maxim; ++i) {
    current += have[i];
    current -= must[i];
    if (current < 0) { 
      added -= current; 
      current = 0; 
    }
  }
  return added;
}

int main()
{
  FILE *fin = fopen("train.in", "r");
  FILE *fout = fopen("train.out", "w");
  int tests;
  int delay;
  int na, nb;
  int h1, m1, h2, m2;

  fscanf(fin, "%d\n", &tests);
  for (int test = 0; test < tests; ++test) {
    memset(havea, 0, sizeof(havea));
    memset(haveb, 0, sizeof(haveb));
    memset(musta, 0, sizeof(musta));
    memset(mustb, 0, sizeof(mustb));
    fscanf(fin, "%d\n", &delay);
    fscanf(fin, "%d %d\n", &na, &nb);
    for (int i = 0; i < na; ++i) {
      fscanf(fin, "%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
      musta[convert(h1, m1)]++;
      haveb[convert(h2, m2) + delay]++;
    }
    for (int i = 0; i < nb; ++i) {
      fscanf(fin, "%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
      mustb[convert(h1, m1)]++;
      havea[convert(h2, m2) + delay]++;
    }
    fprintf(fout, "Case #%d: %d %d\n", test + 1, solve(havea, musta), solve(haveb, mustb));
  }

  fclose(fin);
  fclose(fout);
}
