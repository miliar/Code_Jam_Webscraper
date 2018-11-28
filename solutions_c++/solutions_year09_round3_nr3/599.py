#include <iostream>
using namespace std;
int mustbe[5],used[5];
int saber;
int solve(int cur, int tot, int N, int M) {
  used[cur] = 1;
  int i, aux, mine = 10000000;
  int a1,a2,padrao;
  a1 = 0;
  a2 = N+1;
  for (i = 0 ; i < M ; i++) {
    if (used[i] == 0) {
      //    printf("Agora vou colocar %d na posicao %d\n",mustbe[i],tot+1);
      aux = solve(i,tot+1,N,M);
      // printf("Consegui %d\n",aux);
      if (aux < mine) mine = aux;
    }
  }
  for (i = 0 ; i < M ; i++) {
    if (i != cur) 
      if (used[i] == 1) {
	if (mustbe[i] < mustbe[cur]) {
	  if (mustbe[i] > a1) 
	    a1 = mustbe[i];
	}
	else if (mustbe[i] > mustbe[cur]) {
	  if (mustbe[i] < a2)
	    a2 = mustbe[i];
	}
      }
  }
  used[cur] = 0;
  padrao = a2-a1-2;
  if (mine == 10000000) {
    return padrao;
  }
  else return padrao+mine;
}
  
int main() {
  int N,M,K,aux,u,i,j;
  scanf("%d",&N);
  for (i = 0 ; i < N ; i++) {
    saber = 1000000000;
    scanf("%d %d",&M,&K);
    for (j = 0 ; j < K ; j++) {
      scanf("%d",&mustbe[j]);
    }
    for (j = 0 ;  j < K  ; j++) {
      for (u = 0 ; u < 5 ; u++) used[u] = 0;
      //  printf("Solucao colocando primeiramente %d\n",mustbe[j]);
      aux = solve(j,1,M,K);
      // printf("Valor = %d\n",aux);
      if (aux < saber) saber = aux;
    }
    printf("Case #%d: %d\n",i+1,saber);
  }
}
