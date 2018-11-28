#include <stdio.h>
#include <stdlib.h>
#define MAXm 10100
#define INF 0x3f3f3f3f

int pd[MAXm][2];
int m,v;
int op[MAXm],ch[MAXm]; /*operacao, changeable*/
int val[MAXm];

int calc(int v1, int v2, int op){
  if(op) return (v1 & v2);
  else return (v1 | v2);
}

int nao(int k){
  return (k+1)%2;
}

int main(){
  int nt,nt0;
  int i,j, aux;

  scanf(" %d", &nt0);
  for(nt=1 ; nt<=nt0 ; nt++){
    scanf(" %d %d", &m,&v);
    for(i=0 ; i<=m ; i++) pd[i][0]=pd[i][1]=INF;

    for(i=1 ; i<=(m-1)/2 ; i++){
      scanf(" %d %d", &op[i],&ch[i]);

      val[i]=0;
    }

    for(j=1 ; j<=(m+1)/2 ; j++){
      i=j+ (m-1)/2;
      scanf(" %d", &val[i]); /*valor das folhas*/

      pd[i][val[i]]=0;
    }

    for(i=(m-1)/2 ; i>=1 ; i--){
      aux = calc(val[2*i],val[2*i+1],op[i]);
      pd[i][aux] <?= pd[2*i][val[2*i]] + pd[2*i+1][val[2*i+1]];

      aux = calc(nao(val[2*i]),val[2*i+1],op[i]);
      pd[i][aux] <?= pd[2*i][nao(val[2*i])] + pd[2*i+1][val[2*i+1]];

      aux = calc(val[2*i],nao(val[2*i+1]),op[i]);
      pd[i][aux] <?= pd[2*i][val[2*i]] + pd[2*i+1][nao(val[2*i+1])];

      aux = calc(nao(val[2*i]),nao(val[2*i+1]),op[i]);
      pd[i][aux] <?= pd[2*i][nao(val[2*i])] + pd[2*i+1][nao(val[2*i+1])];

      if(ch[i]){
	aux = calc(val[2*i],val[2*i+1],nao(op[i]));
	pd[i][aux] <?= pd[2*i][val[2*i]] + pd[2*i+1][val[2*i+1]] +1;

	aux = calc(nao(val[2*i]),val[2*i+1],nao(op[i]));
	pd[i][aux] <?= pd[2*i][nao(val[2*i])] + pd[2*i+1][val[2*i+1]] +1;

	aux = calc(val[2*i],nao(val[2*i+1]),nao(op[i]));
	pd[i][aux] <?= pd[2*i][val[2*i]] + pd[2*i+1][nao(val[2*i+1])] +1;

	aux = calc(nao(val[2*i]),nao(val[2*i+1]),nao(op[i]));
	pd[i][aux] <?= pd[2*i][nao(val[2*i])] + pd[2*i+1][nao(val[2*i+1])] +1;
      }
    }

    printf("Case #%d: ", nt);
    if(pd[1][v]==INF) puts("IMPOSSIBLE");
    else printf("%d\n", pd[1][v]);
  }

  return 0;
}
