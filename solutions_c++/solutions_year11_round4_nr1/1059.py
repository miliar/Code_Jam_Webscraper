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

void RunTCase(int n, int r) {
  printf("Case #%d: %d\n", n + 1, r); 
}

void GetInputs() {
  fscanf(ifile, "%d", &T);

  REP(t, T) {
    uint64 X, S, R, etmp, N;
    double e;

    fscanf(ifile, "%lld %lld %lld %lld %lld", &X, &S, &R, &etmp, &N);

    e = etmp;

    double result = 0.0;
    
    vector<pair<uint64, uint64> > ws;

    uint64 totwd = 0;
    REP(i, N) {
      uint64 wb, we, wv;
      fscanf(ifile, "%lld %lld %lld", &wb, &we, &wv);

      ws.PB(pair<uint64, uint64>(wv, we - wb));
      totwd += we - wb;
    }

    sort(ws.begin(), ws.end());
    //    REP(i, N)
    //      printf("ws[%d] first = %lld, sec = %lld.\n", i, ws[i].first, ws[i].second);

    uint64 totnwd = X - totwd;
    //    printf("totnwd = %lld.\n", totnwd);

    if (e * R >= totnwd) {
      result += totnwd * 1.0 / R;
      e -= totnwd * 1.0 / R;
    } else {
      result += e + (totnwd - e * R) * 1.0 / S;
      e = 0;
    }

    REP(i, N) {
      if (e * (R + ws[i].first) >= ws[i].second) {
	result += ws[i].second * 1.0 / (R + ws[i].first);
	e -= ws[i].second * 1.0 / (R + ws[i].first);
      } else {
	result += e + (ws[i].second - e * (R + ws[i].first)) * 1.0 / (S + ws[i].first);
	e = 0;
      }
    }

    printf("Case #%d: %.12f\n", t + 1, result); 
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
