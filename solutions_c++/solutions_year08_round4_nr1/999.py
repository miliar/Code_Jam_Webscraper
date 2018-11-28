#include <stdio.h>
#include <algorithm>
using namespace std;

const int MAX = 100;
const int INF = (1 << 30);

#define BIT(x,y) ((x & (1 << (y))) != 0)

int N, tipo[MAX], permite[MAX], valor[MAX], desejado;
int caso;

int dfs (int u, int mask) {

   if (u >= (N + 1) / 2)
      return valor[u];

   int r1 = dfs (2 * u, mask),
       r2 = dfs (2 * u + 1, mask),
       ret;

   if (tipo[u] == 1) {
      if (permite[u] && BIT (mask, u))
	 ret = r1 | r2;
      else
	 ret = r1 & r2; 
   }
   else {
      if (permite[u] && BIT (mask, u))
	 ret = r1 & r2;
      else
	 ret = r1 | r2;
   }
   return ret;
}

int bits (int n) {
   int cnt = 0;
   while (n > 0) { cnt += (n % 2); n /= 2; }
   return cnt;
}

void printBits (int n) {
   while (n > 0) {
      printf ("%d", n % 2);
      n /= 2;
   }
   printf ("\n");
}

void processa () {
   int i, j, ret = INF;

   //printf ("N=%d\n", N);
   for (i = 0; i < (1 << ((N + 1) / 2)); i++) {
      if (dfs (1, i) == desejado) {
	 //printf ("%3d: ", bits (i));
	 ///printBits (i); 
	 ret = min (ret, bits (i));
      }
   }

   printf ("Case #%d: ", caso);
   if (ret == INF)
      printf ("IMPOSSIBLE\n");
   else
      printf ("%d\n", ret);
}

void le () {
   int i;
   scanf ("%d %d", &N, &desejado);

   for (i = 1; i <= (N - 1) / 2; i++) {
      scanf ("%d %d", &tipo[i], &permite[i]);
   }

   for (i = (N + 1) / 2; i <= N; i++) {
      scanf ("%d", &valor[i]);
   }
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
