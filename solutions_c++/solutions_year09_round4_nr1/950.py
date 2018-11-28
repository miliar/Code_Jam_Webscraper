#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
// Templates
template <typename T>
inline T square(T x) { return x * x;}
template <typename T>
void convert(const string& s, T& t) { istringstream iss(s); s >> t; }

// Macros
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FORN(i,n) FOR(i,0,n)
#define FORV(i,v) FORN(i,static_cast<int>((v).size()))

// Input/output file
FILE *fin;
FILE *fout;

// line -> vector of ints
int getInts(vector<int>& v) {
  static char line[2048];
  fgets(line, sizeof(line)/sizeof(line[0]), fin);
  char *tok = strtok(line, " \t");
  while (tok) {
    int t; sscanf(tok, "%d", &t); v.push_back(t);
    tok = strtok(NULL, " ");
  }
  return static_cast<int>(v.size());
}


// BEGIN HERE ************

int main(int argc, const char **argv) {
  if (argc < 3 || !strcmp(argv[1], argv[2])) std::exit(1);
  fin = fopen(argv[1], "r");
  fout = fopen(argv[2], "w");
  if (!fin || !fout) std::exit(2);
  int c_ = 0;
  fscanf(fin, "%d\n", &c_);
  FOR(ci_,1,c_+1) {
    int n;
    fscanf(fin, "%d\n", &n);
    vector<int> lines;
    FORN(i,n) {
      char line[64];
      fscanf(fin, "%s\n", line);
      int max = 0;
      FORN(j,64) {
        if (line[j] == '1') max = j;
        else if (line[j] != '0') break;
      }
      lines.push_back(max);
    }
    //FORV(i,lines) fprintf(fout, "%d ", lines[i]);
    int swaps = 0;
    int size = static_cast<int>(lines.size());
    FORN(i,size) {
      if (lines[i] <= i) continue;
      FOR(j,i,size) {
        if (lines[j] <= i) {
          swaps += j-i;
          int old = lines[j];
          for (int k = j; k > i; --k) lines[k]=lines[k-1];
          lines[i]=old;
          break;
        }
      }
    }
    
    fprintf(fout, "Case #%d: %d\n", ci_, swaps);
  }
  
  return 0;
}
