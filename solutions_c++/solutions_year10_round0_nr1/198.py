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

bool LightState(int N, int K){
  return (K&((1<<N)-1)) == ((1<<N)-1);
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int i=0;i!=T;++i){
    int N, K;
    cin >> N >> K;
    cout << "Case #" << (i+1) << ": " << (LightState(N, K)?"ON":"OFF") << endl;
  }
  return 0;
}
