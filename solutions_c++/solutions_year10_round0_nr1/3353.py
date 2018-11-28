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

//---------------------------------------------------------------------------



int main()
{
  int N, K;
  int T; 
//  char n[10];
  FILE * inFile, * outFile;

  inFile = fopen ("C:\\Qual\\A-small.in","r");
  outFile = fopen ("C:\\Qual\\A-small.out","w");

  if (inFile!=NULL)
  {
	fscanf (inFile, "%d", &T);
	for (int i = 1; i <= T; i++)
	{
	  fscanf (inFile, "%d", &N);
	  fscanf (inFile, "%d", &K);

	  if ((((K + 1) >> N) << N) == (K + 1))
		  	  fprintf(outFile, "Case #%d: ON\n", i);
	  else
		  	  fprintf(outFile, "Case #%d: OFF\n", i);
	}

	fclose (inFile);
	fclose (outFile);
  }

  printf("Problem A Solved\n");
  getch();
  return 0;
}
//---------------------------------------------------------------------------

