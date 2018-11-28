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

void RunTCase(int n, string s) {
  printf("Case #%d: [", n + 1); 
  REP(i, s.SZ) {
    printf("%c", s[i]);
    if(i != s.SZ - 1)
      printf(", ");
  }
  printf("]\n");
}

void GetInputs() {
  fscanf(ifile, "%d", &T);

  REP(t, T) {
    int C, D, N;
    vector<string> comb;
    vector<string> opp;
    char c_els[1000];
    string els;
    string cur;

    fscanf(ifile, "%d", &C);
    REP(c, C) {
      char s[10];
      fscanf(ifile, "%s", &s);
      comb.PB(s);
    }

    fscanf(ifile, "%d", &D);
    REP(c, D) {
      char s[10];
      fscanf(ifile, "%s", &s);
      opp.PB(s);
    }

    fscanf(ifile, "%d", &N);
    fscanf(ifile, "%s", &c_els);
    els = c_els;

    /*
    REP(i, comb.SZ)
      printf("comb[%d] = %s.\n", i, comb[i].c_str());
    REP(i, opp.SZ)
      printf("opp[%d] = %s.\n", i, opp[i].c_str());
    printf("els = %s.\n", els);
    */

    cur = "";

    for(int i = 0; i < els.SZ; i++) {
      cur.PB(els[i]);
      //      printf("0 -- cur = %s.\n", cur.c_str());

      if (cur.SZ > 1) {
	bool flag = true;
	REP(j, comb.SZ) {
	  if (flag && 
	    (((cur[cur.SZ - 1] == comb[j][0]) && (cur[cur.SZ - 2] == comb[j][1])) ||
	     ((cur[cur.SZ - 1] == comb[j][1]) && (cur[cur.SZ - 2] == comb[j][0])))) {
	    cur.erase(cur.SZ - 1, 1);
	    cur[cur.SZ - 1] = comb[j][2];
	    //	    printf("1 -- cur = %s.\n", cur.c_str());
	    flag = false;
	  }
	}

	REP(j, opp.SZ) {
	  REP(k, cur.SZ) {
	    if (flag && 
		(((cur[cur.SZ - 1] == opp[j][0]) && (cur[k] == opp[j][1])) ||
		 ((cur[cur.SZ - 1] == opp[j][1]) && (cur[k] == opp[j][0])))) {
	      //	      printf("2 -- cur = %s.\n", cur.c_str());
	      cur = "";
	      flag = false;
	    }
	  }
	}

      }
    }
    //    printf("9 -- cur = %s.\n", cur.c_str());
    RunTCase(t, cur);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();
  
  fclose(ifile);
}
