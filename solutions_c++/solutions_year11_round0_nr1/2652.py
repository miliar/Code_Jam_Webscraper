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

int T, N;

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

void RunTCase(int n, uint64 v) {
  printf("Case #%d: %lld\n", n + 1, v); 
}

void GetInputs() {
  fscanf(ifile, "%d", &T);

  REP(t, T) {
    int sum = 0;
    int prev_c = -1;

    fscanf(ifile, "%d", &N);

    vector<int> pos(2, 1);
    vector<int> time_credits(2, 0);
    
    REP(n, N) {
      char s[10];
      int c, b, dt;

      fscanf(ifile, "%s %d", &s, &b);
      c = (s[0] == 'O') ? 0 : 1;
      dt = abs(b - pos[c]) + 1;

      if (prev_c != c) {
	dt -= time_credits[c];
	if (dt < 1)
	  dt = 1;
	time_credits[c] = 0;
      }
      time_credits[!c] += dt;
      
      sum += dt;
      pos[c] = b;
    }

    RunTCase(t, sum);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
