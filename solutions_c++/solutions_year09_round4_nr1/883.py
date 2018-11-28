#include <cmath>
#include <cstdlib>
#include <cassert>
#include <climits>
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

bool satisfy(const matrix& mat){
  const int N = mat.size();
  for(int i=0;i!=N;++i){
    for(int j=i+1;j!=N;++j){
      if(mat[i][j]!=0){
	return false;
      }
    }
  }
  return true;
}

int solve(const matrix& mat){
  const int N = mat.size();
  vector<int> buf(N);
  for(int i=0;i!=N;++i){
    int jmax(-1);
    for(int j=0;j!=N;++j){
      if(mat[i][j]==1 && j > jmax){
	jmax = j;
      }
    }
    buf[i] = jmax;
  }
  int ret(0);
  for(int i=0;i!=N;++i){
    if(buf[i]>i){
      int jj(-1);
      for(int j=i+1;j!=N;++j){
	if(buf[j]<=i){
	  jj = j;
	  break;
	}
      }
      for(int ii=jj;ii!=i;--ii){
	++ret;
	swap(buf[ii-1], buf[ii]);
      }
    }
  }
  return ret;
}

int main(int argc, char* argv[]){
  int T;
  cin >> T;
  for(int icase=1;icase<=T;++icase){
    int N;
    cin >> N;
    matrix mat(N);
    for(int i=0;i!=N;++i){
      string line;
      cin >> line;
      mat[i].resize(N);
      for(int j=0;j!=N;++j){
	mat[i][j] = line[j]-'0';
      }
    }
    cout << "Case #" << icase << ": " << solve(mat) << endl;
  }
  return 0;
}
