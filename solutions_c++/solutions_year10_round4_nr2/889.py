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

int countbit(int mask){
  int n(0);
  while(mask){
    if(mask&1)++n;
    mask>>=1;
  }
  return n;
}

int solve(int P, vector<int> ms, const vector<vector<int> >& ps){
  int result((1<<P)-1);
  for(int p=0;p!=P;++p){
    vector<int> ms2(ms.size()/2);
    for(int i=0;i!=int(ms2.size());++i){
      int m = min(ms[i*2], ms[i*2+1]);
      if(m>0){
        --m;
        --result;
      }
      ms2[i] = m;
    }
    ms2.swap(ms);
  }
  return result;
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int c=0;c!=T;++c){
    int P;
    cin >> P;
    vector<int> ms(1<<P);
    for(int i=0;i!=int(ms.size());++i){
      cin>>ms[i];
    }
    vector<vector<int> > ps(P);
    for(int i=0;i!=P;++i){
      ps[i].resize(1<<(P-1-i));
      for(int j=0;j!=int(ps[i].size());++j){
        cin>>ps[i][j];
      }
    }
    cout << "Case #" << (c+1) << ": " << solve(P, ms, ps) << endl;
  }
  return 0;
}
