#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define pb push_back
#define go(x,it) for(typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)
#define x first
#define y second

typedef long long ll;

bool solve(int C) {
  printf("Case #%d: ", C);
  int n, S, p;
  cin>>n>>S>>p;
  vector< pair<int, int> > s(n);
  for (int i = 0; i < n; i++) {
    int x;
    cin>>x;
    s[i].first = x/3;
    s[i].second = x%3;
  }
  sort(s.begin(), s.end(), greater< pair<int, int> >() );
  int res = 0;
  for (int i = 0; i < n; i++) {
    if (s[i].first >= p) {
      res++;
    } else if (s[i].first + 1 >= p && s[i].second > 0) {
      res++;
    } else if (s[i].first + 1 >= p && s[i].second == 0 && S && s[i].first > 0) {
      res++;
      S--;
    } else if (s[i].first + 2 >= p && s[i].second == 2 && S) {
      res++;
      S--;
    }
  }
  printf("%d\n", res);
  return true;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  srand(time(NULL));
  int n = 1;
  cin>>n;
  for (int i = 1; i <= n; i++) {
    if (!solve(i)) {
      break;
    }
  }
  return 0;
}

