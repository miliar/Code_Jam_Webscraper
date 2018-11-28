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

ll solve(int R, int k, const vector<ll>& gs){
  ll result(0);
  vector<pair<int, ll> > history;
  int pos_prev(0);
  int pos(0);

  ll ff(0);
  size_t head(0);
  int r(0);
  for(;r!=R;++r){
    ll f(0);
    while(f + gs[pos] <= k){
      result += gs[pos];
      f += gs[pos];
      ++pos;
      if(pos >= int(gs.size()))pos=0;
      if(pos == pos_prev)break;
    }
    history.push_back(make_pair(pos_prev, f));
    for(size_t i=0;i!=history.size();++i){
      if(history[i].first == pos){
        head = i;
        for(;i!=history.size();++i){
          ff += history[i].second;
        }
        ++r;
        goto found;
      }
    }
    pos_prev = pos;
  }
found:
  if(r < R){
    const size_t ls = history.size() - head;
    result += (R-r)/ls*ff;
    r += (R-r) - ((R-r)%ls);
    for(;r!=R;++r){
      result += history[head + ((r-head)%ls)].second;
    }
  }
  return result;
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int c=0;c!=T;++c){
    int R, k, N;
    cin >> R >> k >> N;
    vector<ll> gs;
    for(int i=0;i!=N;++i){
      int g;
      cin >> g;
      gs.push_back(g);
    }
    cout << "Case #" << (c+1) << ": " << solve(R, k, gs) << endl;
  }
  return 0;
}
