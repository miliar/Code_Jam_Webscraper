#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <complex>
#include <algorithm>
using namespace std;

char buffer[20];
bool S[20];
int cnt, size, n, a, b;
set< pair<int, int> > mySet;

void solve()
{
  int m;
  for (int i = 1; i < size; i++) {
    m = 0;
    for (int j = i; j < size; j++)
      m = m * 10 + buffer[j] - '0';
    for (int j = 0; j < i; j++)
    m = m * 10 + buffer[j] - '0';

    if (n >= a && m <= b && m > n)
      mySet.insert(make_pair(n, m));
  }
}

int main(int argc, char *argv[])
{
  int t, i, j, ans;

  scanf("%d", &t);

  for (i = 1; i <= t; i++) {
    mySet.clear();
    ans = 0;
    scanf("%d %d", &a, &b);
    for (n = a; n < b; n++) {
      sprintf(buffer, "%d", n);
      size = strlen(buffer);
      solve();
    }

    printf("Case #%d: %d\n", i, mySet.size());
  }

  return EXIT_SUCCESS;
}

