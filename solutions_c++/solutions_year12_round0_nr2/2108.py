#include <iostream>
#include <cstring>
#include <set>
#include <algorithm>

using namespace std;

pair<int, int> pary[1000];


int main() {
//  int time = clock();  
  int nrTest;
  scanf("%d\n", &nrTest);
  
  int t[1000];
  for (int testcase = 1; testcase <= nrTest; testcase++) {
    int N, S, p;
    int ans = 0;
    scanf("%d%d%d", &N, &S, &p);
    for (int i = 0; i < N; i++) {
      scanf("%d", t + i);
      if (t[i] % 3 == 0) {
        pary[i].first = t[i] / 3;
        pary[i].second = t[i] / 3 + 1;
      } else if (t[i] % 3 == 1) {
        pary[i].first = t[i] / 3 + 1;
        pary[i].second = t[i] / 3 + 1;
      } else {
        pary[i].first = t[i] / 3 + 1;
        pary[i].second = t[i] / 3 + 2;
      }
    }
    sort(pary, pary + N);
    for (int i = 0; i < N; i++) {
      if (pary[i].first == 0 && pary[i].second == 1) {
        if (p == 0) ans++;
      } else if (pary[i].first == 1 && pary[i].second == 1) {
        if (p <= 1) ans++;
      } else if (pary[i].second >= p && pary[i].second <= 10 && S) {
        ans++;
        S--;
      } else if (pary[i].first >= p) {
        ans++;
      }
      //cout << pary[i].first << " " << pary[i].second << endl;
    }

    printf("Case #%d: %d\n", testcase, ans);
    
  }
//  printf("time = %d\n", clock() - time);
    
 
  return 0; 
}
