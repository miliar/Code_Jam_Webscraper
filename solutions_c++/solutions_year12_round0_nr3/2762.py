#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_VAL = 2000000;


int nbTests;
int test;
int A, B;

int tab_n[200];
int tab_m[200];

int compteur = 0;

struct Couple
{
  int a;
  int b;

  bool operator == (const Couple &autre)
  {
    return (a == autre.a && b == autre.b);
  }

};

vector<Couple> hash[MAX_VAL];

void
engendre_rotations(int n)
{
  int cp_n = n;
  int nb_dig = 0;

  while(cp_n > 0)
    {
      cp_n /= 10;
      nb_dig++;
    }

  cp_n = n;

  for(int i = nb_dig - 1; i >= 0; i--)
    {
      tab_n[i] = cp_n % 10;
      cp_n /= 10;
    }

  for(int posDep = 1; posDep < nb_dig; posDep++)
    {
      for(int pos = posDep; pos < posDep + nb_dig; pos++)
	{
	  tab_m[pos - posDep] = tab_n[pos % nb_dig];
	}

      int eval_m = 0;
      for(int i = 0; i < nb_dig; i++)
	eval_m = eval_m * 10 + tab_m[i];
      
      if(eval_m <= B)
	if(eval_m > n)
	  {
	    Couple c;
	    c.a = n;
	    c.b = eval_m;
	  
	    if(find(
		    hash[(10*n + eval_m) % MAX_VAL].begin(), 
		    hash[(10*n + eval_m) % MAX_VAL].end(), c) == hash[(10*n + eval_m) % MAX_VAL].end()) 
	      {
		compteur++;
		hash[(10*n + eval_m) % MAX_VAL].push_back(c);
	      }
	  }
      
    }
}

void
solve()
{
  for(int n = A; n < B; n++)
      engendre_rotations(n);
}

void
init_mark()
{
  for(int i = 0; i < MAX_VAL; i++)
    hash[i].erase(hash[i].begin(), hash[i].end());
}

void
scan_input()
{
  scanf("%d", &nbTests);
  for(test = 1; test <= nbTests; test++)
    {
      compteur = 0;
      printf("Case #%d: ", test);
      scanf("%d%d", &A, &B);
      
      init_mark();
      solve();

      printf("%d\n", compteur);
    }
}

int
main()
{
  scan_input();

  return 0;
}
