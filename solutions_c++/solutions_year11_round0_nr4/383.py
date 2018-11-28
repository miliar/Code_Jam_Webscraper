#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <math.h>

using namespace std;

#define MAX 1024
int C[MAX];

int main(void)
{
  int T,caso,N;

  for(scanf("%d",&T), caso = 1; caso <= T; caso++)
  {
    scanf("%d", &N);
    vector<int> v;
    for(int i = 0; i < N; i++)
    {
      scanf("%d", C+i);
      v.push_back(C[i]);
    }
    sort(v.begin(), v.end());

    int n = N;
    for(int i = 0; i < N; i++)
      if (C[i] == v[i])
        n--;

    printf("Case #%d: %.6lf\n", caso, (n < 2) ? 0.0 : (double)n);
  }

  return(0);
}

