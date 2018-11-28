#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;

int nc, na, nb, tt, a, b, c, d;
vector<pair<int, int> > va, vb;

int main () {

  cin >> nc;
  
  for (int ac = 1; ac <= nc; ac++) {
  
    va.clear();
    vb.clear();
  
    cin >> tt >> na >> nb;
    for (int i = 0; i < na; i++) {
      scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
      va.push_back(pair<int, int> (60*a + b, 1));
      vb.push_back(pair<int, int> (60*c + d + tt, 0));
    }
    for (int i = 0; i < nb; i++) {
      scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
      vb.push_back(pair<int, int> (60*a + b, 1));
      va.push_back(pair<int, int> (60*c + d + tt, 0));
    }
    
    sort(va.begin(), va.end());
    sort(vb.begin(), vb.end());
    
    int ta = 0, ra = 0;
    for (int i = 0; i < na+nb; i++) {
      if (va[i].second == 0) {
        ta++;
      } else {
        if (ta == 0)
          ra++;
        else 
          ta--;
      }
    }
    
    int tb = 0, rb = 0;
    for (int i = 0; i < na+nb; i++) {
      if (vb[i].second == 0) {
        tb++;
      } else {
        if (tb == 0)
          rb++;
        else 
          tb--;
      }
    }
  
    cout << "Case #" << ac << ": " << ra << " " << rb << endl;
  }
  return 0;
  
}
