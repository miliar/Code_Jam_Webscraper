#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int n, l, h;
long long a[10100];

long long gcd (long long p1, long long p2)
{
  while (p1 && p2)
  {
    if (p1 > p2)
      p1 %= p2;
    else
      p2 %= p1;
  }
  if (p1 > p2) 
    return p1;
  else
    return p2;
}

void solve ()
{
  
  scanf ("%d%d%d\n", &n, &l, &h);
 
  long long ggg;
  scanf ("%lld", &a[0]);
  ggg = a[0];
   
  int i, j;
  
  for (i =1; i < n; i ++)
  {
    scanf ("%lld", &a[i]);
    ggg = gcd (ggg, a[i]);   
  }

  for (i = l; i <= h; i ++)
  {
    int ok = 1; 
    
    for (j = 0; j < n; j ++)
    {
      if ( a[j] % i != 0 && i % a[j] != 0 )
      {
	ok = 0;
	break;
      }
      
    }
    if (ok)
      {
	printf ("%d\n", i);
	return;
      }
  }
  printf ("NO\n");
}

int main ()
{
  int t; 
  scanf ("%d", &t);
  
  for (int i = 1; i <=t; i ++)
  {
    printf ("Case #%d: ", i);
    solve ();
  }
  
  
  return 0;
}