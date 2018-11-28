#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

struct value{
  double p;
  char label[15]; 
  value(){
    p=0.0;
    for(int i=0; i<15; i++)
      label[i]=0;
  }
};
value* Tree;
void czytaj_drzewo(int n){
  //  printf("Wykonuje sie dla %d\n", n);
  // dostaje bufor w miejscu za OTWARTYM NAWIASEM
  //czyta az znajdzie lewy nawias
  scanf("%lf", &Tree[n].p);
  //printf("%d: Liczba: %lf\n", n, Tree[n].p);
  char t=getchar();
  while(t<=' '){
    //printf("%d: czysci biale znaki\n", n);
    t=getchar();
  }
  if(t>='a' && t<='z'){
    //printf("%d: znalazl etykiete zapisuje\n", n);
    int j=0;
    Tree[n].label[j++]=t;
    t=getchar();
    while(t>='a' && t<='z'){
      Tree[n].label[j++]=t;
      t=getchar();
    } 
  }
  while(t<=' '){
    //printf("%d: czysci biale znaki\n", n);
    t=getchar();
  }
  if(t=='('){
    //printf("%d: syn TRUE\n", n);
    czytaj_drzewo(2*n);
    t=getchar();
    while(t!='('){
      //printf("%d: czysci biale znaki\n", n);
      t=getchar();
    }
    //printf("%d: syn FALSE\n", n);
    czytaj_drzewo(2*n+1);
  }else{
    Tree[2*n].p=-2.0;
    Tree[2*n+1].p=-2.0;
  }
  while(t!=')'){
    //printf("%d: czysci biale znaki\n", n);
    t=getchar();
  }
  return;
}
int main(){
  int N;
  scanf("%d", &N);
  for(int n=1; n<=N; n++){
    int L;//liczba lini drzewa
    Tree=new value[1000];
    scanf("%d", &L);
    char t=getchar();
    while(t!='(')
      t=getchar();
    czytaj_drzewo(1);
    /*for(int i=1; i<20; i++){
      printf("%lf %s\n", Tree[i].p, Tree[i].label);
    }*/
    int A;//ile zawierzat
    scanf("%d", &A);
    printf("Case #%d:\n", n);
    for(int i=0; i<A; i++){
      char wyraz[15];
      char tytuly[110][15];
      for(int a=0; a<110; a++)
	for(int b=0; b<15; b++)
	  tytuly[a][b]=0;
      scanf("%s", wyraz);//nazwa zwierzecia, niepotrzbna
      int u;
      scanf("%d", &u);
      getchar();
      for(int j=0; j<u; j++){/*
	t=getchar();
	do{
	  int r=0;
	  tytuly[j][r++]=t;
	  t=getchar();
	}while(t>='a' && t<='z');*/
	scanf("%s", tytuly[j]);
      }

      ///for(int k=0; k<u; k++)
      //printf("%s\n", tytuly[k]);

      double wynik = 1;
      int o=1;
      while(1){
	//printf("Jestem w %d\n", o);
	if(Tree[o].p<-1.0)
	  break;

	wynik*=Tree[o].p;
	
	bool czy_ma=false;
	for(int y=0; y<u; y++){
	  int error=0;
	  for(int e=0; e<15; e++){
	    if(Tree[o].label[e]!=tytuly[y][e]){
	      error=1;
	      break;
	    }
	  }
	  if(error==false){
	    czy_ma=true;
	    break;
	  }
	}

	if(czy_ma==true){
	  //printf("ma tytul\n");
	  o=2*o;}
	else{
	  o=2*o+1;
	  //printf("nie ma\n");
	}
      }
      printf("%.7lf\n", wynik);
    }
    delete[] Tree;
  }
  return 0;
}
