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

bool backtrack (vector<vector<int> >& g, vector<int>& colors,
                int curr_vertex, int n, int num_colors, int& count) {
  ++count;
  if (count > 100000) return false;
//   if (count % 10000 == 0) cerr << ".";
  if (curr_vertex >= n) return true;
  vector<char> colors_used (num_colors,0);
  for (size_t i = 0; i < g[curr_vertex].size(); ++i) {
    if (colors[g[curr_vertex][i]] != -1) {
      colors_used[colors[g[curr_vertex][i]]] = true;
    }
  }
  for (int i = 0; i < num_colors; ++i) {
    if (!colors_used[i]) {
      colors[curr_vertex] = i;
      if(backtrack (g,colors,curr_vertex + 1, n, num_colors,count)) {
        colors[curr_vertex] = -1;
        return true;
      } else if (curr_vertex == 0) return false;
      colors[curr_vertex] = -1;
    }
  }
  return false;
}


int main() {
  int num_cases;
  cin >> num_cases;
  cin.ignore();
  
  for (int case_num = 1; case_num <=  num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    int n,k;
    cin >>n >> k;
    vector<vector<int> > stockprices (n, vector<int> (k));
    vector<vector<int> > cg (n);
    for (int i = 0; i < n;++i) {
      for (int j = 0; j < k; ++j) {
        cin >> stockprices[i][j];
      }
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        vector<int>& sti = stockprices[i];
        vector<int>& stj = stockprices[j];
        for (int s = 0; s < k-1; ++s) {
          bool conflicts = false;
          if (sti[s] == stj[s]) conflicts = true;
          if (sti[s+1] == stj[s+1]) conflicts = true;
          if (sti[s] < stj[s] && sti[s+1] > stj[s+1]) conflicts = true;
          if (sti[s] > stj[s] && sti[s+1] < stj[s+1]) conflicts = true;
          if (conflicts) {
            cg[i].push_back (j);
            cg[j].push_back (i);
//             cg[i][j] = true;
//             cg[j][i] = true;
            break;
          }
        }
      }
    }
    int max_deg=0;
    for (int i = 0; i < n; ++i) {
      int deg = 0;
      for (int j = 0; j < n; ++j) {
        if (cg[i][j])++deg;
      }
      max_deg = max (max_deg, deg);
    }

    for (int i = n; i > 0; --i) {
      cerr << "testing: " << i << "\n";
      int count = 0;
      vector<int> colors (n,-1);
      if (!backtrack (cg, colors, 0, n, i,count)) {
        cout << i+1 << "\n";
        break;
      }
      if (i==1) cout << "1\n";
    }
    
    

  }
  
}
