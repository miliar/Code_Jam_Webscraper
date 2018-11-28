#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <assert.h>
#include <bitset>
#include <functional>
#include <utility>
#include <iomanip>
#include <cctype>
#include <gmp.h>
#include <gmpxx.h>
//#include <ext/hash_set>
//#include <ext/hash_map>

using namespace std;
//using namespace __gnu_cxx;
typedef unsigned long long int ll;

int TD(char c) {return (int)(c-'A');}


int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);

  for (int test=0; test<nbTests; test++) {
    int c, d, n, i;
    char c1, c2, c3;
    string r;
    vector<vector<char> > tab_comb(26,vector<char>(26,'-'));
    vector<vector<bool> > tab_del(26,vector<bool>(26,false));

    /* Get entry */
    in >> c;
    for(i=0; i<c; i++) {
      in >> c1 >> c2 >> c3;
      tab_comb[TD(c1)][TD(c2)] = c3;
      tab_comb[TD(c2)][TD(c1)] = c3;
    }
    
    in >> d;
    for(i=0; i<d; i++) {
      in >> c1 >> c2;
      tab_del[TD(c1)][TD(c2)] = true;
      tab_del[TD(c2)][TD(c1)] = true;
    }
    
    in >> n;
    in >> r;

    /* Solve */
    int pos=0;
    string sol(102,'-');

    for(i=0; i< n; i++) {
      /* Add letter */
      sol[pos] = r[i];
      pos++;
      
      if(pos<=1) continue;

      /* Combination */
      
      while(1) {
	if(pos<=1) break;
	char comb = tab_comb[TD(sol[pos-1])][TD(sol[pos-2])];
	if(comb != '-') {
	  sol[pos-2] = comb;
	  pos--;
	}
	else
	  break;
      }
      if(pos<=1) continue;
      
      /* Deletion */
      char d = sol[pos-1];
      for(int j=0; j<pos-1; j++) {
	if(tab_del[TD(d)][TD(sol[j])]) {
	  pos = 0;
	  break;
	}
      }
    }

    /* Output */
    out << "Case #" << test+1 << ": [";
    for(i=0; i<pos-1; i++) {
      out << sol[i] << ", ";
    }
    if(pos != 0) out << sol[pos-1];
    out << "]" << endl;
  }
}

