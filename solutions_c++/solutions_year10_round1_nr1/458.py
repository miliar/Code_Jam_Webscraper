#include <cmath>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cfloat>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <string>
#include <boost/lexical_cast.hpp>
#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>

using namespace std;
using namespace boost;

#define foreach BOOST_FOREACH

typedef vector<vector<int> > matrix;
typedef long long ll;

void rotate(int N, vector<string>& out, const vector<string>& ls){
  out = ls;
  for(int i=0;i!=N;++i){
    string l;
    for(int j=0;j!=N;++j){
      if(ls[i][j] != '.')l += ls[i][j];
    }
    const int nd = (N-l.length());
    for(int j=0;j!=nd;++j){
      out[j][N-1-i] = '.';
    }
    for(int j=nd;j!=N;++j){
      out[j][N-1-i] = l[j-nd];
    }
  }
}

string solve(int N, int K, const vector<string>& ls){
  bool red(false), blue(false);
  vector<string> rt;
  rotate(N, rt, ls);
  for(int i=0;i!=N;++i){cerr<<rt[i]<<endl;}
  for(int i=0;i!=N;++i){
    for(int j=0;j!=N;++j){
      const char c = rt[i][j];
      if(c == '.')continue;
      if(j<=N-K){
        bool cont(true);
        for(int d=0;d!=K;++d){
          if(rt[i][j+d] != c){
            cont=false;
            break;
          }
        }
        if(cont){
          cerr<<c<<", " << i << ", " << j << endl;
          if(c == 'R'){
            red = true;
          }
          else{
            blue = true;
          }
        }
      }
      if(i<=N-K){
        bool cont(true);
        for(int d=0;d!=K;++d){
          if(rt[i+d][j] != c){
            cont=false;
            break;
          }
        }
        if(cont){
          cerr<<c<<", " << i << ", " << j << endl;
          if(c == 'R'){
            red = true;
          }
          else{
            blue = true;
          }
        }
      }
      if(i<=N-K && j<=N-K){
        bool cont(true);
        for(int d=0;d!=K;++d){
          if(rt[i+d][j+d] != c){
            cont=false;
            break;
          }
        }
        if(cont){
          cerr<<c<<", " << i << ", " << j << endl;
          if(c == 'R'){
            red = true;
          }
          else{
            blue = true;
          }
        }
      }
      if(i<=N-K && j>=K-1){
        bool cont(true);
        for(int d=0;d!=K;++d){
          if(rt[i+d][j-d] != c){
            cont=false;
            break;
          }
        }
        if(cont){
          cerr<<c<<", " << i << ", " << j << endl;
          if(c == 'R'){
            red = true;
          }
          else{
            blue = true;
          }
        }
      }
    }
  }
  if(blue && red){
    return "Both";
  }
  if(blue){
    return "Blue";
  }
  if(red){
    return "Red";
  }
  return "Neither";
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int c=0;c!=T;++c){
    int N, K;
    cin >> N >> K;
    vector<string> ls(N);
    for(int i=0;i!=N;++i){
      cin >> ls[i];
    }
    cout << "Case #" << (c+1) << ": " << solve(N, K, ls) << endl;
  }
  return 0;
}
