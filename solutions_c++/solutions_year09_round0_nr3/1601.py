#include <cstdio>
#include <string>
#define MAX 502
#define	MAXDIGITS	3002

typedef struct {
  char digits[MAXDIGITS];
  int lastdigit;
} bignum;

void print_bignum(bignum *n) {
  int i;
  if(n->lastdigit < 6)
    for(int i = n->lastdigit+1; i < 6; ++i)
      n->digits[i] = 0;
  for (i=3; i>=0; i--)
    printf("%c",'0'+ n->digits[i]);
}

void zero_justify(bignum *n) {
  while ((n->lastdigit > 0) && (n->digits[ n->lastdigit ] == 0))
    n->lastdigit --;
}

void add_bignum(bignum *a, bignum *b, bignum *c) {
  int carry;
  int i;
  c->lastdigit = (a->lastdigit > b->lastdigit ? a->lastdigit : b->lastdigit) + 1;
  for(i = a->lastdigit + 1; i <= c->lastdigit; i++)
    a->digits[i] = 0;
  for(i = b->lastdigit + 1; i <= c->lastdigit; i++)
    b->digits[i] = 0;
  carry = 0;
  for (i=0; i<=(c->lastdigit); i++) {
    c->digits[i] = (char) (carry+a->digits[i]+b->digits[i]) % 10;
    carry = (carry + a->digits[i] + b->digits[i]) / 10;
  }
  zero_justify(c);
}

int main() {
  int N, tam1, tam2, pos1, pos2, i;
  char str1[MAX], str2[] = "welcome to code jam";
  bignum matriz[MAX], aux, ant, aux2, contador;
  scanf("%d\n", &N);
  for(i = 1; i < MAXDIGITS; i++)
    aux2.digits[i] = 0;
  aux2.lastdigit = 0;
  aux2.digits[0] = 1;
  for(int count = 1; count <= N; count++) {
    fgets(str1, 501, stdin);
    tam1 = strlen(str1);
    tam2 = 19;
    if (tam1 < tam2 || tam2 == 0) {
      printf("Case #%d: 0000\n", count);
      continue;
    }
    contador.lastdigit = 0;
    for(i = 0; i < MAXDIGITS; i++)
      contador.digits[i] = 0;
    for(pos1 = 0; pos1 < tam1; pos1++) {
      aux = contador;
      if(str1[pos1] == str2[0])
        add_bignum(&aux, &aux2, &contador);
      matriz[pos1] = contador;
    }
    for(pos2 = 1; pos2 < tam2; pos2++) {
      aux = matriz[pos2 - 1];
      for(i = 0; i < MAXDIGITS; i++)      
        matriz[pos2 - 1].digits[i] = 0;
      matriz[pos2 - 1].lastdigit = 0;
      for(pos1 = pos2; pos1 < tam1 - tam2 + pos2 + 1; pos1++) {
        ant = matriz[pos1];
        if(str1[pos1] == str2[pos2])
          add_bignum(&matriz[pos1 - 1], &aux, &matriz[pos1]);
        else
          matriz[pos1] = matriz[pos1 - 1];  
        aux = ant;
      }   
    }
    printf("Case #%d: ", count);
    print_bignum(&matriz[tam1 - 1]);
    printf("\n");
  }
  return 0;
}
