#include <cstdio>
#include <cstring>
#include <cctype>
#include <iostream>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int di[10000], li[10000];
int mx[10000];
int N, D;

int main() {
  int ca;
  cin >> ca;
  for (int i = 0; i < ca; ++i) {
    cin >> N;
    for (int j = 0; j < N; ++j) {
      cin >> di[j] >> li[j];
    }
    cin >> D;

    memset(mx, 0, sizeof(mx));

    mx[0] = di[0];
    bool ans = false;
    for (int j = 0; j < N; ++j) {
      if (di[j] + mx[j] >= D) {
	ans = true;
	break;
      }
      for (int k = j + 1; k < N; ++k) {
	if (di[j] + mx[j] < di[k]) break;
	int mn = min(di[k] - di[j], li[k]);
	mx[k] = max(mx[k], mn);
      }
    }
    cout << "Case #" << i+1 << ": ";
    if (ans) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
      
  }
}
