#include <cstdio>
#include <map>

using namespace std;

int A1, A2;
int B1, B2;

map<pair<int, int>, int> chk;

int solve(int a, int b) {  
  if (chk.count(make_pair(a, b)) != 0) return chk[make_pair(a, b)];
  if (a == b) return chk[make_pair(a, b)] = 0;
  
  int j = a / b;
  for (int i = j; i > 0; --i) {
    if (a - b * i != 0 && solve(a - b * i, b) == 0)
      return chk[make_pair(a, b)] = 1;
  }
  
  j = b / a;
  for (int i = j; i > 0; --i) {
    if (b - a * i != 0 && solve(a, b - a * i) == 0)
      return chk[make_pair(a, b)] = 1;
  }
  return chk[make_pair(a, b)] = 0;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int cs;
  scanf("%d", &cs);
  for (int r = 1; r <= cs; ++r) {
    scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
    int sol = 0;
    for (int i = A1; i <= A2; ++i)
      for (int j = B1; j <= B2; ++j) {
        chk.clear();
        sol += solve(i, j);
      }
      
    printf("Case #%d: %d\n", r, sol);
  }
  return 0;
}