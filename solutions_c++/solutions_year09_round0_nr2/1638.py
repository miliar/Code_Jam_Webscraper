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
  
  int T;
  in >> T;
  for (int t = 1; t <= T; ++t) {
    int H, W;
    in >> H >> W;
    int alt[H][W];
    for (int h = 0; h < H; ++h) {
      for (int w = 0; w < W; ++w) {
        in >> alt[h][w];
      }
    }
    
    char res[H][W];
    memset(res, 0, sizeof(res));
    
    char lexnextsink = 'a';
    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
        vector<pii> visited;
        int h = i, w = j;
        while (true) {
          if (res[h][w] != 0) {
            char basin = res[h][w];
            for (vector<pii>::iterator it = visited.begin();
                 it != visited.end();
                 ++it) {
              res[it->first][it->second] = basin;      
            }
            break;
          }
          visited << pii(h,w);
          // Determine next cell to visit
          int height = alt[h][w];
          pii next(-1,-1);
          if (h > 0 && alt[h-1][w] < height) {
            height = alt[h-1][w];
            next = pii(h-1,w);
          }
          if (w > 0 && alt[h][w-1] < height) {
            height = alt[h][w-1];
            next = pii(h,w-1);
          }
          if (w < W - 1 && alt[h][w+1] < height) {
            height = alt[h][w+1];
            next = pii(h,w+1);
          }
          if (h < H - 1 && alt[h+1][w] < height) {
            height = alt[h+1][w];
            next = pii(h+1,w);
          }
          if (height == alt[h][w]) {
            // Found a basin
            char basin = lexnextsink;
            ++lexnextsink;
            for (vector<pii>::iterator it = visited.begin();
                 it != visited.end();
                 ++it) {
              res[it->first][it->second] = basin;      
            }
            res[h][w] = basin;
            break;
          } else {
            h = next.first;
            w = next.second;
          }
        }
      }
    } 
    out << "Case #" << t << ":" << endl;
    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
        if (j != 0) out << " ";
        out << res[i][j];
      }
      out << endl;
    }
  }
  
}
  