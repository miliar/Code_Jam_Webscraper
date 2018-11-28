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
    int N;

    fscanf(ifile, "%d", &N);

    vector<vector<int> > r(N, vector<int>(N, 0));

    REP(i, N) {
	char s[1000];
	fscanf(ifile, "%s", &s);
	//	printf("c = %c.", c);
	REP(j, N) {
	  char c = s[j];
	  if (c == '0')
	    r[i][j] = 0;
	  if (c == '1')
	    r[i][j] = 1;
	  if (c == '.')
	    r[i][j] = 2;
	}
    }

    /*
    REP(i, N) 
      REP(j, N) {
      printf("%d %d %d.\n", i, j, r[i][j]);
    }
    */

    vector<double> ng(N, 0);
    vector<double> wp(N, 0);
    vector<double> owp(N, 0);
    vector<double> oowp(N, 0);

    REP(i, N) {
      REP(j, N) {
	if ((r[i][j] == 1) || (r[i][j] == 0))
	  ng[i] += 1.0;
      }
    }

    REP(i, N) {
      REP(j, N) {
	if (r[i][j] == 1)
	  wp[i] += 1.0 / ng[i];
      }
    }

    REP(i, N) {
      REP(j, N) {
	if (r[i][j] == 1)
	  owp[i] += ((wp[j] * ng[j]) / (ng[j] - 1)) / ng[i];
	if (r[i][j] == 0)
	  owp[i] += ((wp[j] * ng[j] - 1) / (ng[j] - 1)) / ng[i];
      }
    }

    REP(i, N) {
      REP(j, N) {
	if ((r[i][j] == 1) || (r[i][j] == 0))
	  oowp[i] += owp[j] / ng[i];
      }
    }

    printf("Case #%d:\n", t + 1); 
    REP(i, N) {
      double result = wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25;
      printf("%0.10f\n", result);
    }
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
