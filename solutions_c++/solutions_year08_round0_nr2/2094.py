#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <math.h>
#include <vector>

using namespace std;

#define PB push_back
#define SZ size()

#define DEBUG 0

int N;
int T;
int NA, NB;
vector<int> a_d, a_a;
vector<int> b_d, b_a;

FILE *ifile;

void Usage() {
  fprintf(stderr, "usage = -i <file_name>");
}

void GetOptions(int argc, char **argv) {
  int c;
  int flags = 0;
  char buf[101];

  while ((c = getopt(argc, argv, "i:")) != -1) {
    switch (c) {
    case 'i':
      flags |= 0x1;
      snprintf(buf, 100, "%s", optarg);
      ifile = fopen(buf, "r");
      if (ifile == NULL) {
        fprintf(stderr, "ERROR!!!  Could not open %s.\n", buf);
        exit(1);
      }
    }
  }
  if (~flags & 0x1) {
    fprintf(stderr, "Missing -i.\n");
    Usage();
  }
}

int RunTCaseSub(vector<int> &a, vector<int> &d) {
  vector<int> ts;
  for(int i = 0; i < 25 * 60; i++)
    ts.PB(0);

  for(uint i = 0; i < a.SZ; i++) {
    for(int t = a[i]; t < 25 * 60; t++) {
      ts[t]++;
    }
  }

  for(uint i = 0; i < d.SZ; i++) {
    for(int t = d[i]; t < 25 * 60; t++) {
      ts[t]--;
    }
  }

  int min = 100;
  for (uint i = 0; i < ts.SZ; i++)
    if (ts[i] < min)
      min = ts[i];

  return -min;
}

void RunTCase(int n) {
  int at, bt;
  at = RunTCaseSub(a_a, a_d);
  bt = RunTCaseSub(b_a, b_d);
  printf("Case #%d: %d %d\n", n, at, bt);
}

void GetInputs() {
  fscanf(ifile, "%d", &N);
  for(int i = 0; i < N; i++) {
    a_a = vector<int>();
    a_d = vector<int>();
    b_a = vector<int>();
    b_d = vector<int>();

    fscanf(ifile, "%d", &T);
    fscanf(ifile, "%d %d", &NA, &NB);
    for(int j = 0; j < NA; j++) {
      int ah, am, dh, dm;
      fscanf(ifile, "%d:%d %d:%d", &dh, &dm, &ah, &am);
      a_d.PB(dh * 60 + dm);
      b_a.PB(ah * 60 + am + T);
    }
    for(int j = 0; j < NB; j++) {
      int ah, am, dh, dm;
      fscanf(ifile, "%d:%d %d:%d", &dh, &dm, &ah, &am);
      b_d.PB(dh * 60 + dm);
      a_a.PB(ah * 60 + am + T);
    }
    if (DEBUG) {
      printf("N = %d.\n", N);
      printf("T = %d.\n", T);
      printf("NA, NB = %d, %d.\n", NA, NB);
      printf("A departures:\n");
      for(uint j = 0; j < a_d.SZ; j++)
        printf("  %d.\n", a_d[j]);
      printf("A arrivals:\n");
      for(uint j = 0; j < a_a.SZ; j++)
        printf("  %d.\n", a_a[j]);
    }
    RunTCase(i+1);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();

  fclose(ifile);
}
