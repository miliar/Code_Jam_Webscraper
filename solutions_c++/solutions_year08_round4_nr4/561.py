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

using namespace std;


int main() {
  int num_cases ;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    int k;
    cin >> k;
    string text;
    cin>> text;
    vector<int> perm (k);
    int best_compression = text.size();
    for (int i = 0; i < k; ++i) perm[i] = i;
    do {
      vector<char> out_text (text.size());
      for (int i = 0; i < (int)text.size(); i+=k) {
        for (int j = 0; j < k; ++j) {
          out_text[i+j] = text[i+perm[j]];
        }
      }
      char last = 0;
      int groups = 0;
      for (int i = 0; i < (int)text.size(); ++i) {
        if (out_text[i] != last){
          ++groups;
          last = out_text[i];
        }
      }
      best_compression = min (groups, best_compression);
    } while (std::next_permutation (perm.begin(), perm.end()));
    cout << best_compression << "\n";
  }
  

}
