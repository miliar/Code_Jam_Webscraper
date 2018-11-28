#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;


int main() {
  int num_cases;
  cin >> num_cases;
  cin.ignore();
  
  for (int case_num = 1; case_num <=  num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    string number;
    cin >> number;
    while(number[0] == '0') number = number.substr (1);
    if (!next_permutation (number.begin(), number.end())) {
      number += "0";
      sort (number.begin(),number.end());
      string zeros = number.substr (0,number.find_first_not_of ("0"));
      number = number.substr (zeros.size());
      number = number[0] + zeros + number.substr (1);
    }
    cout << number << endl;
    
  }
  
}
