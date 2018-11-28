#include <iostream>
#include <cstdio>
using namespace std;

const int MAXQ = 1000;
const int MAXS = 100;

int T;

int DP[MAXQ][MAXS];

char eng[MAXS][110];
char order[MAXQ][110];

int main()
{
 FILE *fin = fopen("universe.in", "r"); 
 FILE *fout = fopen("universe.out", "w");
 
 fscanf(fin, "%d\n", &T);
 for (int u = 0; u < T; u++)
 {
  int S; fscanf(fin, "%d\n", &S);
  for (int i = 0; i < S; i++)
  {
   fgets(eng[i], 109, fin);
   eng[i][strlen(eng[i]) - 1] = '\0';
  } 
  int Q; fscanf(fin, "%d\n", &Q);
  for (int i = 0; i < Q; i++)
  {
   fgets(order[i], 109, fin);
   order[i][strlen(order[i]) - 1] = '\0';
  } 
  for (int i = 0; i < Q; i++)
   for (int j = 0; j < S; j++)
    DP[i][j] = 1000000;
  for (int i = 0; i < S; i++)  
   if (strcmp(order[0], eng[i]) != 0)
    DP[0][i] = 0;
  for (int i = 1; i < Q; i++)
   for (int j = 0; j < S; j++)
   {
    if (strcmp(order[i], eng[j]) == 0) continue;
    for (int k = 0; k < S; k++)
     if (k == j)
     {
      DP[i][j] <?= DP[i - 1][k];
     }
     else
     {
      DP[i][j] <?= DP[i - 1][k] + 1;
     }
   }
  int ans = 1000000;
  for (int i = 0; i < S; i++)
   ans <?= DP[Q - 1][i];
  fprintf(fout, "Case #%d: %d\n", u + 1, ans);
 }
 
 fclose(fin);
 fclose(fout);
 
 return 0;
}
