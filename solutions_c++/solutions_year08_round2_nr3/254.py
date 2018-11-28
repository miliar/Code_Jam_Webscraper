#include <cstdio>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <map>
using namespace std;

typedef struct ligada * ponte;
struct ligada{
  int val;
  ponte next;
};

struct ligada elems[1001001];

void gerapermut(int k){
  int i, tam, val, anda;
  ponte at, ant;
  
  for (i = 0; i < k-1; i++){
    elems[i].next = &elems[i+1];
  }
  elems[k-1].next = &elems[0];

  tam = k;
  at = &elems[k-1];
  val = anda = 1;
  while (tam > 0){
    //if (anda > tam){
    //  printf("era %d, virou %d\n", anda, anda%tam);
    //  anda = anda%tam;
    //}
    for (i = 1; i <= anda; i++){
      ant = at;
      at = at->next;
    }
    at->val = val;
    val++;
    tam--;
    anda = val;
    at = ant;
    at->next = at->next->next;
  }

}

int main(){
  int desejados[111];
  int t, ka, k, n, i;

  scanf("%d", &t);
  for (ka = 1; ka <= t; ka++){
    scanf("%d", &k);
    scanf("%d", &n);
    for (i = 0; i < n; i++)
      scanf("%d", &desejados[i]);
    gerapermut(k);
    //for (i = 0; i < k; i++)
    //  printf("%d ", elems[i].val);
    //printf("\n");
    printf("Case #%d:", ka);
    for (i = 0; i < n; i++){
      printf(" %d", elems[desejados[i]-1].val);
    }
    printf("\n");
  }

  return 0;
}
