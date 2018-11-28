#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;


int main (int argc, char *argv[]) {
  int n;

  scanf ("%d",&n);
  for (int cs = 0; cs < n; cs++) {
    int g, s, threshold, result = 0;
    scanf ("%d %d %d",&g,&s,&threshold);
    for (int i = 0; i < g; i++) {
      int score, base;
      scanf ("%d",&score);
      base = score/3;
      switch (score%3) {
        case 0:
          if (base >= threshold) result++;
          else if (s > 0 && base && base + 1 >= threshold) s--,result++;
          break;
        case 1:
          if (base+1 >= threshold) result++;
          break;
        case 2:
          if (base+1 >= threshold) result++;
          else if (s > 0 && base+2 >= threshold) s--,result++;
          break;
      }
    }
    printf ("Case #%d: %d\n",cs+1,result);
  }

  return 0;
}
