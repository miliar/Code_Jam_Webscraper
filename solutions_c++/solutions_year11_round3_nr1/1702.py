/*
 * Tibor Mezei (zemei)
 * Google Code Jam
 * Standard: C++0x with GCC-4.4
*/

#include <deque>
#include <list>
#include <map>
#include <tuple>
#include <vector>
#include <queue>

#include <algorithm>
#include <complex>
#include <iostream>
#include <fstream>
#include <regex>
#include <string>

#include <cctype>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


// Prime number tester
bool isPrime(uint64_t x) {
  if (x<2) return false;
  for (uint64_t i=2; i*i<=x; ++i)
    if (x%i==0) return false;
  return true;
}

    char table[50][50];

int main(int argc,char **argv) {

  ifstream fi;		// input file
  ofstream fo;		// output file
  int numCases,cases;	// number of cases

  if (argc!=2) { 
    printf("No input!\n"); 
    return -1; 
  }

  fi.open(argv[1]);
  fo.open("output.txt");


  fi >> numCases;

  for (cases=1; cases<=numCases; ++cases) {
    // -----------------------------------------------------------------------------
    int sx, sy;
    bool impossible = false;
    for (int i=0; i<50; ++i) {
      for (int j=0; j<50; ++j) {
        table[i][j] = 0;
      }
    }

    fi >> sx >> sy;
    for (int i=0; i<sx; ++i) {
      for (int j=0; j<sy; ++j) {
        char c;
	fi >> c;
	if (c=='#' && table[i][j]==0) { // New tile
	  if (j+1 == sy || i+1 == sx) {
	    impossible=true;
	  } else {
	    table[i][j] = '/';
	    table[i+1][j+1] = '/';
	    table[i][j+1] = '\\';
            table[i+1][j] = '\\';
	  }
	} else
	if (c!='#') {
	 if (table[i][j]=='/' || table[i][j]=='\\') {
	    impossible = true;
	  } else {
	    table[i][j] = c;
	  }
	}
      }
    }
    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": " << endl;
    if (impossible) fo << "Impossible"  << endl;  // TODO
    else {
      for (int i=0; i<sx; ++i) {
        for (int j=0; j<sy; ++j) {
	  fo << table[i][j];
	}
	fo << endl;
      }
    }
  }

  fi.close();
  fo.close();
  return 0;
}


