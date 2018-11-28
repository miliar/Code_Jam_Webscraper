#include<iostream>
#include<ext/hash_set>
#include<ext/hash_map>
#include<string>
#include<vector>

namespace __gnu_cxx
{
        template<> struct hash< std::string >
        {
                size_t operator()( const std::string& x ) const
                {
                        return hash< const char* >()( x.c_str() );
                }
        };
}

using __gnu_cxx::hash_set;
using __gnu_cxx::hash_map;
using namespace std;


int main(int argc, char * argv[])
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    string N;
    cin >> N;
    int temp = -1;
    int smallest = 10;
    int small_pos = -1;
    int i = 0;
    for (i = N.length()-1 ; i >=0 ; i--) {
      int dig = N[i] - '0';
      if (dig >= temp) {
	temp = dig;
      } else {
	int j = 0;
        for (j = i+1; j < N.length(); j++) {
	  int dig_c = N[j] - '0';
	  if (dig_c <= dig) {
	    N[i] = N[j-1];
	    N[j-1] = dig + '0';
	    break;
	  }
        }
	// Last number
	if (j  == N.length()) {
	  N[i] = N[j-1];
	  N[j-1] = dig + '0';
	}
	// REverse
	reverse(N.begin() + i + 1, N.end());
	//	for (int k = i+1; k < N.length(); k++) {
	break;
	//	}
      }
    }
    if (i == -1) {
      for (int m = N.length()-1 ; m >=0 ; m--) {
	int dig = N[m] - '0';
	if (dig != 0) {
	  N[m] = '0';
	  N.push_back(dig + '0');
	  reverse(N.begin(), N.end());
	  break;
	}
      }
    }
    cout << "Case #" << t+1 << ": " << N << endl; 
  }
  return 0;
}
