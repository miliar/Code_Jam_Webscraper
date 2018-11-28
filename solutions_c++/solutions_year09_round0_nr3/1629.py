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

typedef pair<int,int> pii;

int main(int argc, char** argv) {
  if (argc != 3) {
    cerr << "invalid amount of arguments" << endl;
    return -1;
  }
  
  ifstream in(argv[1]);
  ofstream out(argv[2]);
  
  const int MOD = 1000;
  const string target = "welcome to code jam";
  
  int T;
  in >> T;
  
  // flush newline buffer
  string tmp;
  getline(in, tmp);
  for (int t = 1; t <= T; ++t) {
    string s;
    getline(in, s);
    
    int dp[2][s.length()];
    memset(dp, 0, sizeof(dp));
    
    
    for (int i = 0; i < s.length(); ++i) {
      if (s[i] == target[0]) dp[0][i] = 1; 
    }
    
    
    
    
    for (int i = 1; i < target.length(); ++i) {
      for (int j = 0; j < s.length(); ++j) {
        dp[i & 1][j] = 0;
      }
      
      for (int j = s.length() - 1; j >= 0; --j) {
        if (s[j] == target[i]) {
          int counter = 0;
          
          for (int k = 0; k < j; ++k) {
            counter += dp[(i+1)&1][k];
            counter %= MOD;
          }
          
          dp[i & 1][j] = counter;
        }
      }
      
    }
    int i = target.length() - 1;
    int res = 0;
    for (int j = 0; j < s.length(); ++j) {
      res += dp[i&1][j];
      res %= 1000;
    }
    char buf[100];
    sprintf(buf, "Case #%d: %04d\n", t, res);
    out << buf;
  }
}
