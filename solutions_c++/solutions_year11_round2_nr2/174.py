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
    int C, D;

    fscanf(ifile, "%d %d", &C, &D);

    vector<double> P(C, 0.0);
    vector<double> V(C, 0.0);

    REP(i, C) {
      int p, v;
      fscanf(ifile, "%d %d", &p, &v);
      //      printf("v = %d.\n", v);
      P[i] = p;
      V[i] = v;
    }

    //    REP(i, C) {
    //      printf("V[%d] = %f.\n", i, V[i]);
    //    }

    double maxt = 0.0;
    REP(i, C) {
      REP(j, C) {
	double totnum = 0.0;
	for(int k = i; k <= j; k++)
	  totnum += V[k];
	//	printf("totnum %d %d = %f.\n", i, j, totnum);
	double dist = fabs(P[j] - P[i]);
	double reqd = (totnum - 1) * D;
	double curt = (reqd - dist) / 2;
	if (curt > maxt)
	  maxt = curt;
      }
    }

    printf("Case #%d: %.10f\n", t + 1, maxt); 
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
