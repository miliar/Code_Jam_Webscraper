#include<stdlib.h>
#include<iostream>
#include<ext/hash_set>
#include<ext/hash_map>
#include<string>
#include<vector>
#include<set>

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
    int N;
    cin >> N;
    vector<int> int_list;
    for (int n = 0; n < N; n++) {
      int max_1 = 0;
        for (int n2  = 0; n2  < N; n2 ++) {
	  char b;
	  cin >> b;
	  if (b == '1') {
	    max_1 = n2+1;
	    //	    cout << max_1 << endl;
	  }
        }
	//	cout << max_1 << endl;
	int_list.push_back(max_1);
    }
    int total_swaps = 0;
    for (int i = 0; i < N; i++) {
      int curr = int_list[i];
      //      cout << curr << ":" << i+1 << endl;
      if (curr <= i+1) 
	continue;
      for (int j = i+1; j < N; j++) {
	if (int_list[j] <= i+1) {
	  int tmp = int_list[j];
	  for (int k = j-1; k >=i; k--) {
	    int_list[k+1] = int_list[k];
	  }
	  int_list[i] = tmp;
	  total_swaps += (j-i);
	  //  cout << total_swaps << endl;
	  break;
	}
      }
    }
    cout << "Case #" << t+1 << ": " << total_swaps << endl; 
  }
  return 0;    
}
