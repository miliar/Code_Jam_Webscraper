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
    int m,v;
    cin >> m >> v;
    int internal_nodes = (m-1)/2;
    vector<int> tree (m+1);
    vector<int> changeable (m+1);
    for (int i = 1; i <= internal_nodes; ++i) {
      cin >> tree[i] >> changeable[i];
    }
    vector<vector<int> > min_cost (2, vector<int> (m+1, 100000) );
    for (int i = internal_nodes+1; i<= m; ++i) {
      cin >> tree[i];
      min_cost[tree[i]][i] = 0;
    }
    // for (int i = 1; i <= m; ++i) cerr << tree[i] << " ";
    // cerr << "\n";
    
    for (int i = internal_nodes; i > 0; --i) {
      if (tree[i] == 1) {//and
        int c1 = 2*i;
        int c2 = 2*i+1;
        // no change
        min_cost[1][i] = min (min_cost[1][i], min_cost[1][c1] + min_cost[1][c2]);
        min_cost[0][i] = min (min_cost[0][i], min_cost[0][c1] + min_cost[1][c2]);
        min_cost[0][i] = min (min_cost[0][i], min_cost[1][c1] + min_cost[0][c2]);
        min_cost[0][i] = min (min_cost[0][i], min_cost[0][c1] + min_cost[0][c2]);
        // change
        if (changeable[i]) {
          min_cost[1][i] = min (min_cost[1][i], 1 + min_cost[0][c1] + min_cost[1][c2]);
          min_cost[1][i] = min (min_cost[1][i], 1 + min_cost[1][c1] + min_cost[0][c2]);
        }
      } else { // or
        int c1 = 2*i;
        int c2 = 2*i+1;
        // no change
        min_cost[1][i] = min (min_cost[1][i], min_cost[1][c1] + min_cost[1][c2]);
        min_cost[1][i] = min (min_cost[1][i], min_cost[0][c1] + min_cost[1][c2]);
        min_cost[1][i] = min (min_cost[1][i], min_cost[1][c1] + min_cost[0][c2]);
        min_cost[0][i] = min (min_cost[0][i], min_cost[0][c1] + min_cost[0][c2]);
        
        // change
        if (changeable[i]) {
          min_cost[0][i] = min (min_cost[0][i], 1 + min_cost[0][c1] + min_cost[1][c2]);
          min_cost[0][i] = min (min_cost[0][i], 1 + min_cost[1][c1] + min_cost[0][c2]);
        }
      }
    }
    
    if (min_cost[v][1] > m) cout << "IMPOSSIBLE\n";
    else cout << min_cost[v][1] << "\n";
  }
  
      

  
}
