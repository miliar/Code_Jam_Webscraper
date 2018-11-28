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

typedef long long ll;

int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);

  for (int test=0; test<nbTests; test++) {
    ll sum=0, mini=1e7+1, xo=0, n, val, i;

    in >> n;
    for(i=0; i<n; i++) {
      in >> val;
      sum += val;
      mini = (val<mini)?val:mini;
      xo ^= val;
    }

    if(xo != 0)
      out << "Case #" << test+1 << ": NO" << endl;
    else
      out << "Case #" << test+1 << ": " << sum-mini << endl;
  }
}

