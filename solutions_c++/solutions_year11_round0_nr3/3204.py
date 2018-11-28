#include <algorithm>
#include <cstring>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

int main() {
  int l_test_cases;
  
  cin >> l_test_cases;
  
  for(int i = 0; i < l_test_cases; ++i) {
    int l_possible = 0;
    int l_ncandies, l_candy;
    int l_min = 2000000;
    unsigned long long int l_sum = 0;
    
    cin >> l_ncandies;
    
    for(int j = 0; j < l_ncandies; ++j) {
      cin >> l_candy, l_possible ^= l_candy;
      
      l_min = min(l_min, l_candy);
      l_sum += l_candy;
    }
    
    cout << "Case #" << (i+1) << ": ";
    
    // if it is not possible
    if(l_possible != 0)
      cout << "NO" << endl;
    else
      cout << (l_sum - l_min) << endl;    
  }
  
  return 0;
}
