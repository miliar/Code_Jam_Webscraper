#include <iostream>
#include <cstdio>
using namespace std;

int __gcd (int a , int b)
{
  while (a && b)
  {
	if (a > b)
	  a %= b;
	else
	  b %= a;
  }
  
  return a | b;
}
void solve ()
{
  int D, G, Pd, Pg, tw, n;
  
  scanf ("%d%d%d", &n, &Pd, &Pg);
  
  if (Pd != 0 && n == 0) 
  {
	printf ("Broken\n");
	return;
  }
  
  if (100/__gcd(Pd, 100) > n)
  {
	printf ("Broken\n");
	return;
  }
  if (Pg == 100)
  {
	if (Pd == 100)
	  printf ("Possible\n");
	else
	  printf ("Broken\n");
	return;
  }
  
  if (Pg == 0)
  {
	if (Pd == 0)
	  printf ("Possible\n");
	else
	  printf ("Broken\n");
	return;
  }
  
  printf ("Possible\n");
}

int main ()
{
  int t;
   scanf ("%d", &t);
   
   int i ; 
   
   for (i = 1; i <= t; i ++)
   {
	 printf ("Case #%d: ", i);
	 solve ();
   }
  
  
  return 0; 
}