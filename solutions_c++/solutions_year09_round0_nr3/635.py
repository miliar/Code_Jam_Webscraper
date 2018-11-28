#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

const string GCJ = "welcome to code jam";

#define MAXL 501
#define MOD 10000

char inp[MAXL];

int DP[MAXL][19];

int solve()
{
 memset(DP, -1, sizeof(DP));
 
 int len = strlen(inp), ret = 0;
 for (int i = 0; i < len; i++)
 {
  for (int pos = 0; pos < 19; pos++)
  {
   if (inp[i] != GCJ[pos]) continue;
   
   if (i == 0 && pos > 0) continue;
   
   if (pos == 0)
   {
    DP[i][0] = 1;
    continue;
   }
   
   int temp = 0; bool good = false;
   for (int back = i - 1; back >= 0; back--)
   {
    if (DP[back][pos - 1] == -1) continue;
    
    good = true;
    temp = (temp + DP[back][pos - 1]) % MOD;
   }
   
   if (good) DP[i][pos] = temp;
  }
  
  if (DP[i][18] != -1)
   ret = (ret + DP[i][18]) % MOD;
 } 
  
 return ret;
}

int main()
{
 int N;
 scanf("%d\n", &N);
 
 for (int t = 1; t <= N; t++)
 {
  gets(inp);
  printf("Case #%d: %04d\n", t, solve());
 }
 
 return 0;
}
