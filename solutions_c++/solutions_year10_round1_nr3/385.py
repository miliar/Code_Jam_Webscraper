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

bool winning(int A, int B){
  //cerr << "A = " << A << ", B = " << B << endl;
  if(B > A)swap(A, B);
  vector<int> hs;
  while(B != 0){
    //cerr << "A = " << A << ", B = " << B << ": " << A/B << endl;
    hs.push_back(A/B);
    assert(hs.back() > 0);
    A = A%B;
    swap(A, B);
  }
  assert(!hs.empty());
  bool t(true);
  for(int i=0;i!=hs.size();++i){
    if(hs[i] > 1){
      return t;
    }
    t = !t;
  }
  return t;
}

ll solve(int A1, int A2, int B1, int B2){
  ll result(0);
  for(int a=A1; a<=A2; ++a){
    for(int b=B1; b<=B2; ++b){
      const bool w = winning(a, b);
      if(w)result++;
    }
  }
  assert((A2-A1+1)*(B2-B1+1) >= result);
  return result;
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int c=0;c!=T;++c){
    int A1, A2, B1, B2;
    cin >> A1 >> A2 >> B1 >> B2;
    cout << "Case #" << (c+1) << ": " << solve(A1, A2, B1, B2) << endl;
  }
  return 0;
}
