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
    uint64 R, C, D;

    fscanf(ifile, "%lld %lld %lld", &R, &C, &D);

    vector<vector<int> > ws(R, vector<int>(C, 0));

    REP(r, R) {
      char cs[1000];
      fscanf(ifile, "%s", cs);
      //      printf("cs = %s.\n", cs);
      REP(c, C) {
	ws[r][c] = cs[c] - '0';
	//	printf("%d", ws[r][c]);
      }
      //      printf("\n");
    }

    int biggest = 0;
    for(int s = 3; s < min(R, C) + 1; s++) {
      //      printf("s = %d %lld %lld.\n", s, R, C);
      int off = (s - 1) / 2;
      //      printf("s = %d, off = %d.\n", s, off);
      REP(r, R) {
	REP(c, C) {
	  uint64 sumr = 0;
	  uint64 sumc = 0;
	  if ((s % 2) == 1) {
	    if ((biggest != s) && (r + off < R) && (c + off < C) && (r >= off) && (c >= off)) {
	      REP(i, off + 1) {
		REP(j, off + 1) {
		  if ((i != off) || (j != off)) {
		    if (j == 0)
		      sumr += i * (ws[r + i][c] - ws[r - i][c]);
		    else
		      sumr += i * (ws[r + i][c + j] + ws[r + i][c - j] - ws[r - i][c + j] - ws[r - i][c - j]);
		    
		    if (i == 0)
		      sumc += j * (ws[r][c + j] - ws[r][c - j]);
		    else
		      sumc += j * (ws[r + i][c + j] + ws[r - i][c + j] - ws[r + i][c - j] - ws[r - i][c - j]);
		  }
		}
	      }
	      if ((sumr == 0) && (sumc == 0)) {
		biggest = s;
	      }
	    }
	  } else {
	    off = s / 2;
	    //	    printf("off = %d.\n", off);
	    if ((biggest != s) && (r + off - 1 < R) && (c + off - 1 < C) && (r >= off) && (c >= off)) {
	      REP(i, off + 1) {
		REP(j, off + 1) {
		  if (((i != off) || (j != off)) && (i != 0) && (j != 0)) {
		    sumr += i * (ws[r + i - 1][c + j - 1] + ws[r + i - 1][c - j] - ws[r - i][c + j - 1] - ws[r - i][c - j]);
		    
		    sumc += j * (ws[r + i - 1][c + j - 1] + ws[r - i][c + j - 1] - ws[r + i - 1][c - j] - ws[r - i][c - j]);
		  }
		  //		  printf("i = %d, j = %d, sumr = %d, sumc = %d.\n", i, j, sumr, sumc);
		}
	      }
	      if ((sumr == 0) && (sumc == 0)) {
		biggest = s;
	      }
	    }
	  }
	}
      }
    }
    
    if (biggest == 0)
      printf("Case #%d: IMPOSSIBLE\n", t + 1); 
    else
      printf("Case #%d: %d\n", t + 1, biggest); 
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
