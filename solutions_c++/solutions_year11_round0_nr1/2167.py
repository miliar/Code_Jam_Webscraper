#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int t, n;

void solve ()
{
  scanf ("%d", &n);
  
  int O = 0, B = 0;
  int Opos = 1, Bpos = 1; 
  
  char who[2];
  int button;
  int i;
  for (i = 0; i < n; i ++)
  {
	scanf ("%s%d",who, &button);
	if (who[0] == 'O')
	{
	  int distance = (Opos - button) < 0 ? (button - Opos) : (Opos - button);
	  int free = B - O;
	  if (free < 0) free = 0;
	  if (free >= distance) distance = 0;
	  else
		distance -= free;
	  
	  O += distance + free;
	  O++;
	  Opos = button;
	}
	else
	{
	  int distance = (Bpos - button) < 0 ? (button - Bpos) : (Bpos - button);
	  int free = O - B;
	  if (free < 0) free = 0;
	  if (free >= distance) distance = 0;
	  else
		distance -= free;
	  
	  B += distance + free;
	  B ++ ;
	  Bpos = button;
	}
	
  }
  printf ("%d\n", max (O, B));
}
int main ()
{
  
  scanf ("%d", &t);
  
  for (int i = 1; i <= t; i ++)
  {
	
	printf ("Case #%d: ", i);
	solve ();
	
  }
  
  return 0;
}