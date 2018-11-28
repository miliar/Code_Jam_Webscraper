#include <stdio.h>
#include <algorithm>
using namespace std;

int caso;

const int MAX = 10000;
const int INF = (1 << 30);

int N;
char S[MAX];
char S2[MAX];
int perm[MAX];

int comprime () {
   int i, tam = 1;

   for (i = 0; S[i] != '\0'; i++) {
      S2[i] = S[i - (i % N) + perm[i % N]];
      if (i > 0 && S2[i] != S2[i-1])
	 tam++;
   }
   return tam;
}

void print () {
   int i;

   printf ("Permutacao: ");
   for (i = 0; i < N; i++)
      printf ("%d ", perm[i]);
   printf ("\n");

   printf ("S: ");
   for (i = 0; S[i] != '\0'; i++) {
      printf ("%c", S[i - (i % N) + perm[i % N]]);
   }
   printf ("\n");

   printf ("Tamanho: %d\n", comprime ());
}

void processa () {
   int i, j, ret = INF;

   for (i = 0; i < N; i++)
      perm[i] = i;

   do {
      //print ();
      ret = min (ret, comprime ()); 
   } while (next_permutation (perm, perm + N));

   printf ("Case #%d: ", caso);
   printf ("%d\n", ret);
}

void le () {
   int i;
   scanf ("%d %s", &N, &S);
}

int main () {
   int casos;
   scanf ("%d", &casos);

   for (caso = 1; caso <= casos; caso++) {
      le ();
      processa ();
   } 

   return 0;
}
