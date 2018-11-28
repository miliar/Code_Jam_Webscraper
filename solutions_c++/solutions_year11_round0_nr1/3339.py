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
template <class T> T &max(T &a,T &b) {
  return a>b ? a : b;
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
    char a; int p,n;
    int o=0,b=0,t=0,op=1,bp=1;
    fi >> n;
    for (int i=0; i<n; ++i) {
      fi >> a >> p;
      if (a == 'O') {
        t += max(abs(p-op)-(t-o)+1,1);
        op = p;
	o = t;
      } else {
        t += max(abs(p-bp)-(t-b)+1,1);
	bp = p;
	b = t;
      }
    } 
    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": ";
    fo << t;  // TODO
    fo << endl;
  }

  fi.close();
  fo.close();
  return 0;
}


