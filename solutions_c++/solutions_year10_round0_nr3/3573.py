#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>

int main()
{
 ifstream fin("C-small-attempt0.in");
 ofstream fout("C-small-attempt0.out");
 
 int T;

 fin>>T;
 
 for (int c = 1; c <= T; c++) 
 {
  int R, k, N;
  int g[10];
  int Q[10], E = 0;

  fin>>R>>k>>N;
  
  for (int i = 0; i < N; i++)
	  fin>>g[i];

  while (R > 0)
  {
	  int temp = 0;
	  int i, j, l;
	  
	  for (i = 0; i < N; i++)
	  {
		  if (temp + g[i] > k)
			  break;
		  else
		  {
			  temp = temp + g[i];
			  E = E + g[i];
		  }
	  }

	  for (j = i, l = 0; j < N; j++, l++)
		  Q[l] = g[j];
	  for (j = 0; j < i; j++, l++)
		  Q[l] = g[j];

	  for (i = 0; i < N; i++)
		  g[i] = Q[i];

	  R--;
  }

  fout<<"Case #"<<c<<": "<<E<<endl;
 }

 fin.close();
 fout.close();
 
 return 0;
}