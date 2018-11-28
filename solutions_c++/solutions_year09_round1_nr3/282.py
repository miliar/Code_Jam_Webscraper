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
typedef long double ld;

ld binom(int n, int k) {
  if (k > n) return 0;
  if (k > n/2) k = n-k;
  long double sum = 1;
  for (int i = 1; i <= k; ++i) {
    sum *= (n-k+i)/i;
  }
  return sum;
}

ld factorial(int N) {
  ld res = 1.0;
  for (int i = 1; i < N; ++i) res *= i;
  return res;
}

int main(int argc, char** argv) {
  if (argc != 3) {
    cerr << "invalid amount of arguments" << endl;
    return -1;
  }
  
  ifstream in(argv[1]);
  ofstream out(argv[2]);
  
  int T, N, C;
  in >> T;
  
  for (int t = 1; t <= T; ++t) {
    in >> C >> N;
    ld dp[C+1];
    memset(dp, 0, sizeof(dp));
    ld ptable[C+1][N+1];
    memset(ptable, 0, sizeof(ptable));
       
    ptable[0][N] = 1.0;
    
    int permtable[C];
    for (int i = 0; i < C; ++i) {
      permtable[i] = i;
    }
    
    for (int c = 1; c < C; ++c) {
      int hlookup[N+1];
      int total = 0;
      memset(hlookup, 0, sizeof(hlookup));
      do {
        int hits = 0;

        for (int i = 0; i < N; ++i) {
          if (permtable[i] >= c) hits++;
        }
        hlookup[hits]++;
        total++;
      } while (next_permutation(permtable, permtable + C));
      for (int i = 0; i <= N; ++i) {
        ptable[c][i] = (ld)hlookup[i] / total;
      }
    }
    
    /*
    for (int i = 0; i < C; ++i) {
      for (int j = 0; j <= N; ++j) {
        cout << ptable[i][j] << " ";
      }
      cout << endl;
    }*/
    
    
    for (int c = C-1; c >= 0; --c) {
      for (int n = 1; n <= N; ++n) {
        if (c + n >= C) break;
        dp[c] += ptable[c][n]/((ld)1 - ptable[c][0]) * (dp[c + n] + 1);
      }
      
      // compute expected misses
      ld miss = ptable[c][0];
      if (miss >= 1e-9) { // epsilon
        double misses = 0.0;
        for (int i = 0; ; ++i) {
        
          double add = (i) * pow(miss, i) * ((ld)1 - miss);
          misses += add;
          
          if (i != 0 && add < 1e-9) break;
        }
        dp[c] += misses;
      }
    }
    out << "Case #" << t << ": " << dp[0] + 1<< endl;
  }
  
  
  return 0; 
}


