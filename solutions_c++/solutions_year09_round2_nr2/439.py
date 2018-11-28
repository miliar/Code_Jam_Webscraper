/*
 *  Google Code Jam 2009
 *  Round 1B - Problem B - The Next Number
 */


#include <stdio.h>
#include <string.h>

#define INPUT_FILE		"input.txt"
#define OUTPUT_FILE		"output.txt"


int T, L, Sol;
char N[64], Index[64];
int F[16];


void back(int pos)
{
  int i, j;

  if (pos == L)
  {
    Sol++;
  } else
  {
    for (i = Sol ? (pos ? 0 : 1) : Index[pos]; i < 10; i++)
      if (F[i])
      {
	N[pos] = i;
	F[i]--;

	back(pos + 1);

	if (Sol == 2)
	  return;

	F[i]++;
      };
  }
}

void Solve()
{
  int i, j;

  for (i = 0; i < 10; i++)
    F[i] = 0;

  for (i = 0; i < L; i++)
    {
      N[i] -= '0';
      F[N[i]]++;

      Index[i] = N[i];
    }

  /* 1st case - all are descending so we must add another 0 */
  int bSortDesc = 1;

  for (i = 0; i < L - 1; i++)
    if (N[i] < N[i + 1])
      {
	bSortDesc = 0;
	break;
      };

  if (bSortDesc)
  {
    int first = 1, c = 0;

    F[0]++;	    /* add another 0 */
    while (F[first] == 0) 
      first++;

    N[c++] = first;
    F[first]--;

    for (i = 0; i < 10; i++)
      for (j = 0; j < F[i]; j++)
	N[c++] = i;

    for (i = 0; i < L + 1; i++)
      printf("%d", N[i]);
    return;
  }

  /* 2nd case - backtracking */
  Sol = 0;
  back(0);

  for (i = 0; i < L; i++)
      printf("%d", N[i]);
}


int main()
{
  freopen(INPUT_FILE, "rt", stdin);
  freopen(OUTPUT_FILE, "wt", stdout);

  scanf("%d\n", &T);

  for (int i = 0; i < T; i++)
  {
    gets(N);
    while (N[strlen(N) - 1] < '0' || N[strlen(N) - 1] > '9')
      N[strlen(N) - 1] = 0;
    L = strlen(N);

    printf("Case #%d: ", i + 1);

    Solve();

    printf("\n");
  }

  fclose(stdout);
  fclose(stdin);

  return 0;
}
