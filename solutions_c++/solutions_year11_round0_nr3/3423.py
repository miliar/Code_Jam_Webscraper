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
    int n,max;
    fi >> n;
    int *t = new int[n];
    for (int i=0; i<n; ++i) fi >> t[i];
    int sum = t[0];
    for (int i=1; i<n; ++i) sum ^= t[i];
    if (sum != 0) max = 0;
    else {
      int min = t[0];
      max = 0;
      for (int i=0; i<n; ++i) {
        max += t[i];
	if (t[i] < min) min = t[i];
      }
      max -= min;
    }

    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": ";
    if (max == 0) fo << "NO";
    else
    fo << max;  // TODO
    fo << endl;
  }

  fi.close();
  fo.close();
  return 0;
}


