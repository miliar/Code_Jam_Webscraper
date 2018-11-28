#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include <math.h>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

#define PB push_back
#define SZ size()

#define REP(i, n)       for(int i = 0; i < (int)(n); i++) 
#define FOR(i, a, b)    for(int i = (a); i < (int)(b); i++) 
#define FORD(i, a, b)   for(int i = (a); i >= (b); i--) 
#define FOREACH(it, c)  for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++) 

typedef unsigned long long int uint64;

FILE *ifile;

int T;

void Usage() {
  fprintf(stderr, "usage = -i <file_name>\n");
  exit(1);
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

void GetInputs() {
  fscanf(ifile, "%d", &T);

  REP(t, T) {
    int C;
    int cum_xor = 0;
    int minv = 10000000;
    int sum = 0;

    fscanf(ifile, "%d", &C);
    REP(c, C) {
      int v;
      fscanf(ifile, "%d", &v);
      if (v < minv)
	minv = v;
      cum_xor = cum_xor ^ v;
      sum += v;
    }

    if (cum_xor == 0)
      printf("Case #%d: %d\n", t + 1, sum - minv); 
    else
      printf("Case #%d: NO\n", t + 1); 
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
