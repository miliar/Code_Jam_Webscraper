#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

void solve ()
{
  int n; 
  scanf ("%d", &n);
  int mini; 
  int a, exor = 0, sum = 0;
  scanf ("%d", &a);
  mini = sum = exor = a;
  for (int i = 1; i < n; i ++)
  {
	scanf ("%d", &a);
	mini = min (a, mini);
	exor ^= a;
	sum += a;
  }
  
  if (exor != 0)
	printf ("NO\n");
  else
	printf ("%d\n", sum - mini);
}
int main ()
{
  
  int t;
  scanf ("%d", &t);
  
  for (int i = 1; i <= t; i ++)
  {
	
	printf ("Case #%d: ", i);
	solve ();
	
  }
  
  return 0;
}