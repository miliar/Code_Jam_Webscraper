#include<iostream>
#include<stdio.h>

using namespace std;

int main () {
   int v[1010], t, i, n, caso, imenor, soma, somacerta;
   
   scanf(" %d", &t);
   for (caso = 1; caso <= t; caso++) {
      scanf(" %d", &n);
      imenor = 0;
      for (i = 0; i < n; i++) {
         scanf(" %d", &v[i]);
         if (v[i] < v[imenor])
            imenor = i;
      }
      soma = somacerta = 0;
      for (i = 0; i < n; i++) {
         if (i != imenor) {
            soma = soma ^ v[i];
            somacerta += v[i];
         }
      }
      if (soma == v[imenor])
         printf("Case #%d: %d\n", caso, somacerta);
      else
         printf("Case #%d: NO\n", caso);
   }
   return 0;
}
