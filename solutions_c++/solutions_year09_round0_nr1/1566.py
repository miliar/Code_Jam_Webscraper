#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <ext/algorithm>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/numeric>
using namespace std;
using namespace __gnu_cxx;
 
#define F(i,a,b)for(int i=a;i<b;++i)
#define rep(i,n)F(i,0,n)
#define all(a)a.begin(),a.end()
template<class T>vector<T>&operator<<(vector<T>& v,T t){v.push_back(t);return v;}

int main(int argc, char** argv) {
  if (argc != 3) {
    cerr << "invalid amount of arguments" << endl;
    return -1;
  }
  
  ifstream in(argv[1]);
  ofstream out(argv[2]);
  
  int L, D, N;
  in >> L >> D >> N;
  char db[D][L];
  char tmp;
  
  for (int i = 0; i < D; ++i) {
    for (int j = 0; j < L; ++j) {
      do {
        in.get(db[i][j]);
      } while (db[i][j] == '\r' || db[i][j] == '\n');
    }
  }
  
  for (int n = 1; n <= N; ++n) {
    bool pattern[L][26];
    memset(pattern, 0, sizeof(pattern));
    
    for (int pos = 0; pos < L; pos++) {
      do { in.get(tmp); } while (tmp == '\r' || tmp == '\n'); 
      if (tmp == '(') {
        in.get(tmp);
        while (tmp != ')') {
          pattern[pos][tmp - 'a'] = true;
          in.get(tmp);
        }
      } else {
        pattern[pos][tmp - 'a'] = true;
      }
    }
    
    int res = 0;
    for (int i = 0; i < D; ++i) {
      for (int j = 0; j < L; ++j) {
        if (!pattern[j][db[i][j] - 'a']) goto out;
      }
      res++;
      out:;
    }
    
    out << "Case #" << n << ": " << res << endl;
  }
  
  return 0; 
}
