/*! if g++ -g c.cpp -o c.out; then ./c.out < c.test; fi
 */

#include <iostream>
#include <string>
#include <algorithm>


#include <boost/lexical_cast.hpp>


using namespace std;
using namespace boost;



void doit(int t){
  int a, b;
  cin >> a >> b;
  int ret = 0;
  for(int i = a; i <= b; ++i){
    for(int j = a; j < i; ++j){
      string ii, jj;
      ii = lexical_cast<string>(i);
      jj = lexical_cast<string>(j);
      for(int k = 0; k < ii.size(); ++k){
	rotate(ii.begin(), ii.begin()+1, ii.end());
	if(ii == jj){
	  ret++;
	  break;
	}
      }
    }
  }
  cout << "Case #" << t << ": " << ret << endl;
}


int main(int argc, char *argv[]){
  int t;
  cin >> t;

  for(size_t i = 0; i < t; ++i){
    doit(i+1);
  }
  return 0;
}
