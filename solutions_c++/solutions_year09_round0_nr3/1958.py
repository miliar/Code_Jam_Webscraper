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
  string welcome_message = "welcome to code jam";

  int num_cases;
  cin >> num_cases;
  string line;
  getline (cin, line);
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    getline (cin, line);
    vector<int> num_pos (welcome_message.size()+1);
    num_pos[0] = 1;
    for (size_t i = 0; i < line.size(); ++i) {
      vector<int> new_num_pos (num_pos);
      for (size_t j = 0; j < welcome_message.size(); ++j) {
        if (welcome_message[j] == line[i]) {
          new_num_pos[j+1] += num_pos[j];
          new_num_pos[j+1] %= 1000;
        }
      }
      num_pos.swap (new_num_pos);
    }
    ostringstream os;
    os << num_pos.back();
    cout << string (4-os.str().size(), '0') << os.str() << "\n";
  }
    
}
