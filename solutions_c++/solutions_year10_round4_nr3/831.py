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

const int N=500;

int next(vector<vector<bool> >& dst, const vector<vector<bool> >& src){
  dst=src;
  int result(0);
  for(int i=0;i!=N;++i){
    for(int j=0;j!=N;++j){
      const bool s = src[i][j];
      bool ns(s);
      const bool sn = i>0?src[i-1][j]:false;
      const bool sw = j>0?src[i][j-1]:false;
      if(s){
        if(!sn && !sw){
          ns = false;
        }
      }
      else{
        if(sn && sw){
          ns = true;
        }
      }
      dst[i][j] = ns;
      if(ns)++result;
    }
  }
  return result;
}

int solve(int R, const vector<int>& xs1, const vector<int>& ys1, const vector<int>& xs2, const vector<int>& ys2){
  vector<vector<bool> > st(N), st2;
  for(int i=0;i!=N;++i)st[i].resize(N, false);
  for(int r=0;r!=R;++r){
    for(int x=xs1[r];x<=xs2[r];++x){
      for(int y=ys1[r];y<=ys2[r];++y){
        st[y][x] = true;
      }
    }
  }
  int result(0);
  while(1){
    const int nb = next(st2, st);
    ++result;
    st2.swap(st);
    if(nb == 0)break;
  }
  return result;
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int c=0;c!=T;++c){
    int R;
    cin >> R;
    vector<int> xs1(R), ys1(R), xs2(R), ys2(R);
    for(int i=0;i!=R;++i){
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      xs1[i] = x1;
      ys1[i] = y1;
      xs2[i] = x2;
      ys2[i] = y2;
    }
    cout << "Case #" << (c+1) << ": " << solve(R, xs1, ys1, xs2, ys2) << endl;
  }
  return 0;
}
