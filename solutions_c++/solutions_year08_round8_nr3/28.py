#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
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
#include <vector>
// gmp library
#include <gmpxx.h>

using namespace std;

typedef long long ll;

const int MF = 1000000009;



vector<vector<int> > children;
int k;

mpz_class mfbig;


mpz_class get_possibilities (int v, int second_level) {
  if (children[v].empty()) return 1;
  mpz_class ret;
  mpz_class factchild;
  mpz_fac_ui (factchild.get_mpz_t(), children[v].size());
  factchild = factchild % mfbig;
  mpz_class kminussec = k-second_level - (v==0?0:1);
  mpz_bin_ui (ret.get_mpz_t(),kminussec.get_mpz_t(), children[v].size());
  ret = ret % mfbig;
  ret = (ret * factchild) % mfbig;
  for (int i = 0; i < (int)children[v].size(); ++i) {
    ret = ret * get_possibilities (children[v][i], children[v].size() - (v == 0? 1:0));
    ret = ret % mfbig;

  }
  return ret % mfbig;
}





int main() {
  mfbig = MF;
  int num_cases ;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    int n;
    cin >> n >> k;
    vector<vector<int> > g (n);
    for (int i = 0; i < n-1; ++i) {
      int v1,v2;
      cin >> v1 >> v2;
      v1--;
      v2--;
      g[v1].push_back (v2);
      g[v2].push_back (v1);
    }
    children = vector<vector<int> > (n);

    vector<char> visited (n,0);
    queue<int> q;
    q.push (0);
    visited[0] = true;
    while (!q.empty()) {
      int curr = q.front();
      q.pop();
      for (int i = 0; i < (int)g[curr].size(); ++i) {
        if (!visited[g[curr][i]]) {
          visited[g[curr][i]]= true;
          children[curr].push_back (g[curr][i]);
          q.push (g[curr][i]);
        }
      }
    }
    if (children[0].size() == 0) {
      cout << "1\n";
      continue;
    }
    
    mpz_class ret = get_possibilities (0,0);
    cout << ret << "\n";
  }
}
  
    
    
