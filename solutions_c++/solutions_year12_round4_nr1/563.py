#include <iostream>
#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

#define MAX 10000
#define EPS 1E-5

int D[MAX], L[MAX], n, d;

bool search() {
  map<int, int> seen;
  queue<int> q;
  q.push(0);
  seen[0] = min(D[0], L[0]);
  
  while (!q.empty()) {
    int c = q.front();
    q.pop();
    
    if (d - D[c] <= seen[c])
      return true;

    for (int i = c + 1; i < n && D[i] - D[c] <= seen[c]; i++) {
      if (seen.count(i) == 0 || seen[i] < min(D[i] - D[c], L[i])) {
        seen[i] = min(D[i] - D[c], L[i]);
        q.push(i);
      }
    }
  }

  return false;
}

int main() {
  int ncases;
  scanf("%i", &ncases);
  for (int caseno = 1; caseno <= ncases; caseno++) {
    scanf("%i", &n);
    for (int i = 0; i < n; i++)
      scanf("%i%i", D + i, L + i);
    scanf("%i", &d);

    printf("Case #%i: %s\n", caseno, search() ? "YES" : "NO");
  }
}
