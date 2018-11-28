#include <cstdio>
#include <vector>
using namespace std;

vector<vector<int> > ciklicniZapis(vector<int> p) {
  vector<vector<int> > c;
  int n = p.size();
  bool *used = new bool[n];
  
  for (int i=0; i<n; i++) used[i] = false;
  for (int i=0; i<n; i++) {
    if (used[i]) continue;
    vector<int> cikel;
    cikel.push_back(i);
    used[i] = true;
    int j = p[i];
    while (j != cikel[0]) {
      cikel.push_back(j);
      used[j] = true;
      j = p[j];
    }
    c.push_back(cikel);
  }
  
  delete[] used;
  return c;
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  
  for (int t=1; t<=nCases; t++) {
    int n, x;
    vector<int> perm;
    
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
      scanf("%d", &x);
      perm.push_back(x-1);
    }
    
    vector<vector<int> > cikli = ciklicniZapis(perm);
    int goro = 0;
    for (int i=0; i<cikli.size(); i++) {
      if (cikli[i].size() != 1) goro += cikli[i].size();
    }
    printf("Case #%d: %d.000000\n", t, goro);
    
    /*for (int i=0; i<cikli.size(); i++) {
      if (i > 0) printf(" ");
      printf("(");
      for (int j=0; j<cikli[i].size(); j++) {
        if (j > 0) printf(" ");
	printf("%d", cikli[i][j]+1);
      }
      printf(")");
    }
    printf("\n");
    */
  }
  
  return 0;
}
