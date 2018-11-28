#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

const int MAXN = 128;

int T;
int N, S, p;
int s[MAXN];

int main() {
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    int ans = 0;
    //printf("CASE %d\n", t);
    scanf("%d %d %d", &N, &S, &p);
    for (int i = 0; i < N; i++) {
      scanf("%d", &s[i]);
      //printf("   --- %d\n", s[i]);
      if (s[i] >= 3 * p - 2) {
        //printf("        yay!\n");
        ans++;
      } else if (s[i] >= 3 * p - 4 && p - 2 >= 0) {
        if (S > 0) {
	  ans++;
	  S--;
	  //printf("          use up one : new S = %d\n", S);
	} else {
	  //printf("         ..booo \n");
	}
      } else {
        //printf("     oh well\n");
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
