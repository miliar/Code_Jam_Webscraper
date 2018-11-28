#include <math.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <deque> 
#include <iostream>

using namespace std;

typedef vector<string>::iterator Vst;
typedef vector<int>::iterator    Vit;
typedef pair<int, int>           Pii;
typedef pair<string, int>        Psi;


struct W{
  int a;
  int b;
};

static int comp(const void* a, const void* b)
{
  W* wa = (W*) a;
  W* wb = (W*) b;
  return wa->a - wb->a;
}


static int solve(W *w, int n)
{
  qsort(w, n ,sizeof(W), comp);

  int count = 0;
  for (int i = 0 ; i < n; i++) {
    for (int j = 0; j < i; j++)
      if (w[i].b < w[j].b) {
        count++;
      }
  }

  return count;
}

int main()
{
  int T;

  //calcC();
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {

    printf("Case #%d: ", i);
    int N;
  
    W window[1000];
    scanf("%d", &N);
    for (int k = 0; k < N; k++)
      scanf("%d%d", &window[k].a, &window[k].b);

    printf("%d", solve(window, N));

    printf("\n");
  }

  return 0;
}
