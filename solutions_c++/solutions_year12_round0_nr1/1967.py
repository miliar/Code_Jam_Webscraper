#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

char A[256];
bool U[256];
char buf[1000];

int main()
{
  string in = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvq";
  string out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upz";
  CLEAR(A, -1);
  CLEAR(U, 0);
  for (int i = 0; i < in.size(); ++i) {
    A[in[i]] = out[i];
    U[out[i]] = 1;
  }
  char c;
  for (c = 'a'; c <= 'z'; ++c)
    if (U[c] == 0)
      break;
  for (char d = 'a'; d <= 'z'; ++d)
    if (A[d] == -1)
      A[d] = c;

  int T;
  scanf("%d", &T);
  gets(buf);
  for (int t = 0; t < T; ++t) {
    gets(buf);
    printf("Case #%d: ", t+1);
    for (int i = 0; buf[i]; ++i)
      printf("%c", A[buf[i]]);
    printf("\n");
  }

  return 0;
};
