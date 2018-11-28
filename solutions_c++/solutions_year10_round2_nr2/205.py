#include <cstdio>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

struct Chicken {
  int speed;
  int x0;
  bool good;
};

vector<Chicken> chickens;
int nChickens, k, xEnd, tMax;

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    cin >> nChickens >> k >> xEnd >> tMax;
    chickens.clear();
    chickens.resize(nChickens);
    for (int i = 0; i < nChickens; i++) {
      cin >> chickens[i].x0;
    }
    for (int i = 0; i < nChickens; i++) {
      cin >> chickens[i].speed;
    }
    
    int nGoodChickens = 0;
    
    for (int i = 0; i < nChickens; i++) {
      Chicken& c = chickens[i];
      c.good = (c.x0 + c.speed * tMax >= xEnd);
      nGoodChickens += c.good;
    }
    
    cout << "Case #" << iCase << ": ";
    if (nGoodChickens >= k) {
      int nSwaps = 0;
      for (int i = nChickens - 1; i >= nChickens - k; i--) {
        int j;
        for (j = i; j >= 0; j--) {
          if (chickens[j].good) break;
        }
        assert(j >= 0);
        swap(chickens[j], chickens[i]);
        nSwaps += i - j;
      }
      cout << nSwaps << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
