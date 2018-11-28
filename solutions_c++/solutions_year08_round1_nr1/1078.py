#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>

bool maior(int a, int b){
  if(fabs(a)>fabs(b)) return true;
  else return false;
}

using namespace std;

int main(){
  int t=1, teste;
  int i, j, k, n, aux1, aux2, aindex, bindex, atual;
  bool atempos, atemneg, btempos, btemneg;
  long long sum;
  vector <int> a, b;
  scanf("%d", &teste);
  while(teste--){
    printf("Case #%d: ",t++);
    scanf("%d", &n);
    a.clear();
    b.clear();
    for(i=0; i<n; i++){
      scanf("%d", &aux1);
      a.push_back(aux1);
    }
    for(i=0; i<n; i++){
      scanf("%d", &aux2);
      b.push_back(aux2);
    }
    //ordenando por modulo decrescentemente
    sort(a.begin(), a.end(), maior);
    sort(b.begin(), b.end(), maior);
    
    /*printf("vetor A\n");
    for(i=0; i<a.size();i++){
      printf("%d ", a[i]);
    }
    printf("\n");
    printf("vetor B\n");
    for(i=0; i<b.size();i++){
      printf("%d ", b[i]);
    }
    printf("\n");*/
    sum=0;
    i=0;
    //os zeros estao nos finais dos vetores.
    //printf("\n");
    while(i<a.size()&&a[i]!=0){//
      bindex=0;
      if(b[0]!=0)atual=a[i]*b[0];
      else break;//todos os b's sao nulos
      for(j=0; j<b.size();j++){
	if(a[i]*b[j]<atual){
	  atual=a[i]*b[j];
	  bindex=j;
	}
      }
      sum+=a[i]*b[bindex];
      //printf("%d %d\n", a[i],b[bindex]);
      a.erase(a.begin());
      b.erase(b.begin()+bindex);
    }
    printf("%lld\n",sum);
  }
  return 0;
}
