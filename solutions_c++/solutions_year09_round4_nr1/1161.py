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
#define INF 10000
template<class T>vector<T>&operator<<(vector<T>& v,T t){v.push_back(t);return v;}
typedef long double ld;

map<vector<int>, int> x;

int solve(vector<int> arr) {
  map<vector<int>, int>::iterator iter = x.find(arr); 
  if (iter != x.end()) {
    return iter->second;
  }
  
  int n = arr.size();
  

  
  bool val = true;
  rep(i,n) { if (arr[i] > i) val = false; }
  if (val) return 0;
  
  rep(i, n) {
    int mincost = INF;
    if (arr[i] <= i) { // no switch necessary
      vector<int> next;
      F(j, 1, n) next << arr[j];
      rep(j, n-1) if (next[j] > 0) next[j]--;
      mincost=  solve(next);
    }
    F(j, i+1, n) { // look for possibilities
      if (arr[j] <= i) { // valid switch
        int cost = (j-i); // cost of bringing the j'th element up here
        vector<int> next;
        
        next << arr[i];
        F(k, i+1, n) if (k != j) next << arr[k];
        rep(k, next.size()) if (next[k] > 0) next[k]--;
        
        cost += solve(next);
        if (cost < mincost) mincost = cost;
      }
    }
    x[arr] = mincost;
    return mincost;
  /*
    if (arr[i] > i) { // bad element
      int mincost = INF;
      F(j, i+1, n) {
        cout << j << endl;
        vector<int> a,b;
        rep(k, j+1) if (k != i) a << arr[k];
        b << arr[i];
        F(k, j+1, n) b << arr[k];
        rep(k, b.size()) if (b[k] > 0) b[k] -= j; else b[k] = 0;
        
          cout << "solving " << n << " ";
  rep(i, n) cout << arr[i];
  cout << endl;
        cout << "swapping " << (j-i) << " : a = ";
        rep(k, a.size()) cout << a[k];
        cout << "; b = ";
        rep(k, b.size()) cout << b[k];
        cout << endl;
        int cost = (j-i) + solve(a) + solve(b);
        if (cost < mincost) mincost = cost;
      
        if (arr[j] <= i) {
          int next[n-i-1];
          memcpy(next, arr + i + 1, sizeof(next));
          
          next[j-i-1] = arr[i];
          rep(k, n-i-1) {
            next[k] -= 1;
          }
          
          int cost = (j-i) + solve(n-i-1, next);
          if (cost < mincost) {
            mincost = cost;
          }
        }
      }   * /
      
      }
      
      return mincost;
    } */
  }
  x[arr] = 0;
  return 0;
}

int main(int argc, char** argv) {
  if (argc != 3) {
    cerr << "invalid amount of arguments" << endl;
    return -1;
  }
  
  ifstream in(argv[1]);
  ofstream out(argv[2]);
  
  int T;
  in >> T;
  
  for (int t = 1; t <= T; ++t) {
    int N;
    in >> N;
    
    vector<int> arr;
    for (int i = 0; i < N; ++i) {
      int lastone = -1;
      char c;
      for (int j = 0; j < N; ++j) {
        in >> c;
        if (c == '1') {
          lastone = j;
        }
      }
      arr << lastone;
    }
    

    int ans = solve(arr);
    cout << "Case #" << t << ": " << ans << endl;
    out << "Case #" << t << ": " << ans  << endl;
  }
  
  
  return 0; 
}


