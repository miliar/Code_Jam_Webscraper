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
  int n;
  cin>>n;
  vector<int> req1(n);
  vector<int> req2(n);
  for (int i = 0; i < n; i++) {
    cin>>req1[i];
    cin>>req2[i];
  }

  int stars = 0;
  int res = 0;

  vector<int> done(n);
  
  while (true) {
    int thingy = -1;
    for (int i = 0; i < n; i++) {
      if (done[i] == 0) {
        if (req2[i] <= stars) {
          thingy = i;
        }
      }
    }
   
    if (thingy == -1) {
      int x = 0;
      for (int i = 0; i < n; i++) {
        if (done[i] == 1 && req2[i] <= stars) {
          thingy = i;
          x = 2;
        }
      }
      if (thingy == -1) {
        for (int i = 0; i < n; i++) {
          if (done[i] == 0 && req1[i] <= stars && (thingy == -1 || req2[thingy] < req2[i])) {
            thingy = i;
            x = 1;
          }
        }
      }
      if (thingy != -1) {
        res++;
        done[thingy] = x;
        stars += 1;
      }
    } else {
      res++;
      stars += 2;
      done[thingy] = 2;
    }

    if (thingy == -1) {
      break;
    }
  }

  if (stars != 2*n) {
    printf("Too Bad\n");
  } else {
    printf("%d\n", res);
  }

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

