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

const int kInf = 1000000000;

int S[5];
int isSurprise;
int atLeast;

void backtrack(int index, int p, int sum)
{
  if (index == 3) {
    if (abs(S[0] - S[1]) > 2 ||
        abs(S[0] - S[2]) > 2 ||
        abs(S[1] - S[2]) > 2)
      return;
    
    if (S[0] + S[1] + S[2] != sum)
      return;


    if (S[0] >= p || S[1] >= p || S[2] >= p) {
      atLeast++;
      if (abs(S[0] - S[1]) == 2 || abs(S[0] - S[2]) == 2 || abs(S[1] - S[2]) == 2) {
        isSurprise++;
      }

    }

  } else {
    for (int i = 0; i <= 10; i++) {
      S[index] = i;
      backtrack(index + 1, p, sum);
    }
  }
}

int main(int argc, char *argv[])
{
  int t, n, s, p, i, j, countAtLeast, countSurprise, ans;
  int  T[105];
  int P[105];
  
  scanf("%d", &t);

  for (i = 1; i <= t; i++) {
    scanf("%d %d %d", &n, &s, &p);

    countAtLeast = 0;
    countSurprise = 0;
    ans = 0;

    for (j = 0; j < n; j++) {
      scanf("%d", &T[j]);
      isSurprise = 0;
      atLeast = 0;

      backtrack(0, p, T[j]);
      if (atLeast) {
        if (isSurprise == 0) P[j] = -1;
        else if (isSurprise == atLeast) P[j] = 1;
        else P[j] = 0;
      } else {
        P[j] = kInf;
      }
    }

    for (j = 0; j < n; j++) {
      if (P[j] != kInf && s > 0 && P[j] == 1) {
        s--;
        P[j] = kInf;
        ans++;
      }
    }

    for (j = 0; j < n; j++) {
      if (P[j] != kInf) {
        if (s > 0 && P[j] >= 0) {
          s--;
          ans++;
        } else {
          if (P[j] != 1)
            ans++;
        }

      }
    }

    printf("Case #%d: %d\n", i, ans);
  }


  return EXIT_SUCCESS;
}

