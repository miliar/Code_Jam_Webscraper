#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main()
{
  int T, N, S, p, t[100];

  FILE *f = fopen("input", "r");
  FILE *out = fopen("output", "w");
  fscanf(f, "%d\n", &T);

  for(int i = 0; i < T; i++)
  {
    int count = 0;
    fprintf(out, "Case #%d: ", i+1);
    fscanf(f, "%d%d%d", &N, &S, &p);
    for(int j = 0; j < N; j++)
    {
      fscanf(f, "%d", &t[j]);
      if(t[j] < 3 * p - 4) continue;
      if(t[j] >= 3 * p - 2) count++;
      if((t[j] < 3 * p - 2) && (S > 0) && (t[j] != 0)) { count++; S--; }
    }
    fprintf(out, "%d\n", count);
  }
  fclose(out);
  return 0;
}
