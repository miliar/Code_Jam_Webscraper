#include<cstdio>
#define C 37
#define D 29
#define N 101

struct evolution{
  char elem1, elem2, res;
};

struct elimination{
  char elem1, elem2;
};

void res(){

  //Read evolutions
  int numEvolutions;
  scanf("%d", &numEvolutions);
  //  printf("E: %d\n",numEvolutions);
  evolution evolutions[C];
  for(int i = 0; i < numEvolutions; ++i){

    scanf(" %c%c%c", &evolutions[i].elem1, &evolutions[i].elem2,&evolutions[i].res);
    //printf("%d %d %d \n", evolutions[i].elem1, evolutions[i].elem2,evolutions[i].res);
  }

  //Read eliminations
  int numEliminations;
  scanf(" %d", &numEliminations);
  //  printf("L: %d\n", numEliminations);
  elimination eliminations[D];
  for(int i = 0; i < numEliminations; ++i){
    scanf(" %c%c", &eliminations[i].elem1,&eliminations[i].elem2);
    //    printf("%d %d\n",eliminations[i].elem1,eliminations[i].elem2);
  }

  
  int numDatos;
  scanf(" %d ", &numDatos);
  char pila[N];
  //  printf("D: %d\n",numDatos);
  int topPila = 0;
  for(int d = 0; d < numDatos; ++d){
    scanf("%c", &pila[topPila]);
    //Comb
    bool comb = false;
    for(int i = 0; i < numEvolutions && !comb; ++i){
      if(topPila > 0 && ((evolutions[i].elem1 == pila[topPila] && evolutions[i].elem2 == pila[topPila-1])
			 || (evolutions[i].elem2 == pila[topPila] && evolutions[i].elem1 == pila[topPila-1]))){
	pila[--topPila] = evolutions[i].res;
	comb = true;
      }
    }
    
    //Oposites
    bool cleared = false;
    if(!comb){
      for(int i = 0; i < numEliminations && !cleared; ++i){
	if(pila[topPila] == eliminations[i].elem1){
	  for(int ant = 0; ant < topPila && !cleared; ant++)
	    if(eliminations[i].elem2 == pila[ant]){ topPila = -1; cleared = true;}
	  
	}else
	  if(pila[topPila] == eliminations[i].elem2){
	    for(int ant = 0; ant < topPila && !cleared; ant++)
	      if(eliminations[i].elem1 == pila[ant]){ topPila = -1;cleared = true;}
	  }
      }
    }



    ++topPila;
  }
  //  printf("\n");

  printf("[");
  for(int i = 0; i < topPila; ++i){
    printf("%c",pila[i]);
    if(i != topPila-1) printf(", ");
  }
  printf("]");
}

int main(){

  int numCases;
  scanf("%d", &numCases);
  for(int i = 1; i <= numCases; i++) {
    printf("Case #%d: ",i);
    res();
    printf("\n");
  }

}
