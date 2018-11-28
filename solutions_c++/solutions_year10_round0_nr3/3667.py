#include<iostream>
#include<list>

using namespace std;

int main(){
  int t, a, b, c, i, aux, topo, tot, cont, teste=1;    

  scanf("%d",&t);
  
  while(t--){
    scanf("%d %d %d", &a, &b, &c);
    list<int>lista;
    
    for(i=0; i<c; i++){
      scanf("%d",&aux);
      lista.push_back(aux);
    }
    
    tot = 0;
    while(a--){
      cont = aux = 0;
      topo = lista.front();
      while(aux+topo <= b && cont < lista.size()){
        aux += topo;
        lista.pop_front();
        lista.push_back(topo);
        topo = lista.front();
        cont++;
      }
      tot += aux;
    }
    printf("Case #%d: %d\n",teste++, tot);
  }
  return 0;    
}
