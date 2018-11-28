// test.cpp : Defines the entry point for the console application.
//

//---------------------------------------------------------------------------

#include <conio.h>
#include <stdio>
#include <string>
#include <math>

#include <vector>
#include <list>
#include <slist>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <hash_map>
#include <set>
#include <hash_set>

#include <numeric>
#include <algorithm>


int main(void)
{
  int R, k, N;
  int T;
  int *g, *runs, curr_run, curr_group, cycle, group_count;
  long long *euros, total_euros, curr_pessengers;

  g = new int[1000];
//  runs = new int[1000];
//  euros = new long long[1000];

//  char n[10];
  FILE * inFile, * outFile;

  inFile = fopen ("C:\\Qual\\B-small.in","r");
  outFile = fopen ("C:\\Qual\\B-small.out","w");

  if (inFile!=NULL)
  {
	fscanf (inFile, "%d", &T);
	for (int i = 1; i <= T; i++)
	{
	  fscanf (inFile, "%d", &R);
	  fscanf (inFile, "%d", &k);
	  fscanf (inFile, "%d", &N);
	  for (int j = 0; j < N; j++)
	  {
		  fscanf (inFile, "%d", g+j);
//		  runs[j] = 0;
//		  euros[j] = 0;
	  }

	  curr_run = 0;
	  curr_group = 0;
	  total_euros = 0;
	  cycle = 0;

	  while (curr_run != R)
	  {
		  curr_pessengers = 0;
		  group_count = 0;
		  while (((curr_pessengers + g[curr_group]) <= k) && group_count < N)
		  {
			  curr_pessengers += g[curr_group];
			  curr_group++;
			  group_count++;
			  if (curr_group == N) curr_group = 0;
		  }

/*
		  if (runs[curr_group] && (cycle == 0))
		  {
			  curr_pessengers += (total_euros + curr_pessengers - euros[curr_group]) * (R - curr_run) / (curr_run - runs[curr_group]);
			  curr_run = R - (R - curr_run) % (curr_run - runs[curr_group]);
			  cycle = 1;
		  }
		  else
*/
		  curr_run++;
		  total_euros += curr_pessengers;
//  		  runs[curr_group] = curr_run - 1;
//		  euros[curr_group] = total_euros;
	  }
	  fprintf(outFile, "Case #%d: %lld\n", i, total_euros);
	}

	fclose (inFile);
	fclose (outFile);
  }

  printf("Problem A Solved\n");
  getch();
  return 0;
}
//---------------------------------------------------------------------------

