#include <iostream>
#include <cstdio>
using namespace std;

int L, D, N;

char words[5000][16];

char inp[500];

bool good[16][26];

int solve()
{
 memset(good, 0, sizeof(good));
 
 int cur = 0; bool op = false;
 for (int i = 0; i < strlen(inp); i++)
 {
  if (isalpha(inp[i]))
  {
   good[cur][inp[i] - 'a'] = true;
   if (!op) cur++;
  }
  else
  if (inp[i] == '(')
   op = true;
  else
  if (inp[i] == ')')
  {
   cur++;
   op = false;
  }
 }
 
 int ret = 0;
 
 for (int w = 0; w < D; w++)
 {
  bool ok = true;
  
  for (int i = 0; i < L; i++)
   if (!good[i][words[w][i] - 'a'])
   {
    ok = false;
    break;
   }
  
  ret += ok;
 }
 
 return ret;
}

int main()
{
 scanf("%d%d%d\n", &L, &D, &N);
 
 for (int i = 0; i < D; i++)
  gets(words[i]);
  
 for (int t = 1; t <= N; t++)
 {  
  gets(inp);  
  printf("Case #%d: %d\n", t, solve());
 }
 
 return 0;
}
