#include <stdio.h>
#include <iostream>
#include <string.h>
#include <map>
using namespace std;

int N;
int S;
int Q;
int matrix[2][100];

void init()
{
  int a;
  for(a = 0; a < S; ++a)
    {
      matrix[0][a] = 0;
      matrix[1][a] = 0;
    }
}

void debug_matrix()
{
  int a;
  int b;
  for(a = 0; a < 2; ++a)
    {
      for (b = 0; b < S; ++b)
	printf(" %d ", matrix[a][b]);
      printf("\n");
    }
	     
}

int min(int line, int exp)
{
  int minval = -1;
  int a;
  for(a=0; a < S; ++a)
    {
      if (a != exp)
	if (matrix[line][a]<minval || minval ==-1)
	  minval = matrix[line][a];
    }
  return minval;
}

int min2 (int line)
{
  int minval = -1;
  int a;
  for(a = 0; a < S; ++a)
    {
      if (matrix[line][a] < minval || minval == -1)
	minval = matrix[line][a];
    }
  return minval;
}

void transpose()
{
  int a;
  for(a = 0; a < S; ++a)
    {
      matrix[1][a] = matrix[0][a];
      matrix[0][a] = 0;
    }
}

void process()
{
  int b;
  for(b = 0; b < N; ++b)
    {
      scanf(" %d ", &S);

      map<string,int>servers;
      int c, val = 0;
            
      /* Receber as strings */

      for(c = 0; c < S; ++c)
	{
	  string server;
	  getline(cin, server);
	  servers[server]=c;
	}
     
      scanf(" %d ", &Q);

      init(); /* inicia-se a matriz a 0's */
      
    
      for(c = 0; c < Q; ++c) /* para cada query...*/
	{
	  string server;
	  getline(cin, server);

	  val = servers[server];
	  
	  int d;
	  for(d = 0; d < S; ++d)
	    {
	      if(d == val)
		{
		  if (!c) /* na primeira execução preenche-se a linha 1 em vez da 0 */  
		    {
		      matrix[1][d] = 1;
		    }
		  else
		    {
		      matrix[0][d] = 1 + min(1,d);
		    }
		}
	      else
		{
		  if (c)
		    {
		      matrix[0][d] = matrix[1][d];
		    }
		}
	    }
	  if (c)
	    transpose(); 
	}
      printf("Case #%d: %d\n", b+1,min2(1));
    }
}

int main ()
{
  scanf("%d ", &N);
  process();
  return 0;
}
