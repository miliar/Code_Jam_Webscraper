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
    int num_offers;
    cin >> num_offers;
    map<string,int> colormap;
    int num_colors=0;
    vector<pair<pair<int,int>, int> > offers;
    for (int i = 0; i < num_offers; ++i) {
      string col;
      int start;
      int end;
      cin >> col >> start >> end;
      if (colormap.find (col) == colormap.end()) {
        colormap[col] = num_colors++;
      }
      offers.push_back (make_pair (make_pair (start, end), colormap[col]));
    }
    sort (offers.begin(), offers.end());

    int best_possible = numeric_limits<int>::max();
    
    for (int c1 = 0; c1 < num_colors; ++c1) {
      for (int c2 = c1; c2 < num_colors; ++c2) {
        for (int c3 = c2; c3 < num_colors; ++c3) {
          // try to paint with c1,c2,c3
          int pos = 0;
          int num_used = 0;
          int next_pos = 0;
          for (int i = 0; i < num_offers; ++i) {
            if (num_used > best_possible) break;
//             cerr << offers[i].first.first << " " << offers[i].first.second << " " << offers[i].second << "\n";
            
            if (offers[i].second != c1 &&
                offers[i].second != c2 && offers[i].second != c3) {
//               cerr << ".";
              continue;
            }
            
            
            if (offers[i].first.first > pos + 1) {
              if (next_pos == pos) {
                break;
              }
              ++num_used;
              pos = next_pos;
            }
            if (offers[i].first.first <= pos + 1) {
              next_pos = max (next_pos, offers[i].first.second);
//               cerr << "w" << next_pos;
            } 
          }
//           cerr << next_pos << "\n";
          if (pos == 10000)
            best_possible = min (best_possible, num_used);
          if (next_pos == 10000) {
            ++num_used;
            best_possible = min (best_possible, num_used);
          }
        }
      }
    }
    if (best_possible == numeric_limits<int>::max()) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << best_possible << "\n";
    }
  }
}
  
    
    
