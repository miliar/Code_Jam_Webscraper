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

typedef long long ll;

int main() {
  int num_cases;
  cin >> num_cases;
  cin.ignore();
  
  for (int case_num = 1; case_num <=  num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    int n;
    cin >> n;
    vector<pair<int,int> > rows;
    for (int i = 0; i < n; ++i) {
      int lastOne = 0;
      for (int j = 0; j < n; ++j) {
        char num;
        cin >> num;
        if (num=='1') lastOne = j+1;
      }
      rows.push_back (make_pair (lastOne,i));
//       cerr << lastOne <<  "\n";
    }

    bool allGood = false;
    while (!allGood) {
      allGood = true;
      bool hadWrong = false;
      int hadWrongAt = 0;
      for (int i = 0; i < n; ++i) {
        if (!hadWrong && rows[i].first > i+1) {
          allGood = false;
            hadWrong = true;
            hadWrongAt = i;
        }
        if (hadWrong && rows[i].first < i+1 && rows[i].first<=hadWrongAt+1) {
//           cerr << "hadWrongAt: " << hadWrongAt << "\n";
          swap (rows[i],rows[i-1]);
          break;
        }
      }
//       }
      
      
//       cerr << "--\n";
//       for (int i = 0; i < n; ++i) cerr << rows[i].first << " " << rows[i].second<< "\n";
    }

//     vector<int> perm (n);
//     for (int i = 0; i < n; ++i) perm[i]=i;
    int bestSwaps = numeric_limits<int>::max();
//     do {
//       bool is_good = true;
//       for (int i = 0; i < n; ++i) {
//         if (rows[perm[i]].first > i+1) is_good = false;
//       }
//       if (is_good) {
        vector<int> pc (n);
        for (int i = 0; i < n; ++i) {
          pc[i] = rows[i].second;
        }
        
        bool issorted = false;
        int numSwaps = 0;
        while (!issorted) {
          issorted = true;
          
          for (int i = 0; i < n-1; ++i) {
            if (pc[i]>pc[i+1]) {
              swap (pc[i],pc[i+1]);
              ++numSwaps;
              issorted = false;
            }
          }
        }
        bestSwaps = min (numSwaps, bestSwaps);
//       }
      
//     } while (std::next_permutation (perm.begin(), perm.end()));
    
    cout << bestSwaps << "\n";
  }

  
}
