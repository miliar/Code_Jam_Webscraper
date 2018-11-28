#include <iostream>
#include <cstdio>
using namespace std;

int n;

bool isPrime (int p)
{
  int i;
  for (i = 2; i*i <= p; i ++)
    if (p%i == 0) return false;
    
  return true;
  
}
void solve ()
{
  scanf ("%d", &n); 
  
  if (n == 1) {printf ("0\n"); return;}
  
  int Min = 0; 
  int Max = 1;
  int i;
  for (i = 2; i <= n; i ++)
  if (isPrime (i))
  {
    Min ++;
    int temp = i;
    Max ++;
    while (temp*i <= n)
    {
      temp *= i;
      Max ++;
    }
  }
  
  printf ("%d\n", Max - Min);
  
  
}
int main ()
{
  
  int T;
  scanf ("%d", &T);
  
  for (int i = 1; i <=T; i++)
  {
    printf ("Case #%d: ", i);
    solve ();
  }
    
  
}
