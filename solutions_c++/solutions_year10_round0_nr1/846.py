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
//#include <ext/hash_set>
//#include <ext/hash_map>

using namespace std;
// using namespace __gnu_cxx;


int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);

  for (int test=0; test<nbTests; test++) {
    
    int n; bool b=true;
    long long int k;
    in >> n >> k;

    for(int i=0; i<n; i++) {
      if (k%2==0) {
	out << "Case #" << test+1 << ": OFF" << endl;
	b=false;
	break;
      }
      k = (k-1)/2;
    }    

    if(b)
      out << "Case #" << test+1 << ": ON" << endl;
  }
}

