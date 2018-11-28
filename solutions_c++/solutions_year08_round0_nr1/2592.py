#include <stdio.h>
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main(){
  int t=1, teste, n, i, j, k, ans, num, s, min, anterior;
  int busca[102][1002];
  char nome[102];
  string aux, enter;
  map <string, int> nomes;
  map<string,int>::iterator iter;
  scanf("%d", &teste);
  
  while(teste--){
    scanf("%d\n", &n);
    num=0;//----------------------->Os sites de busca comecam no 0.
    //pegando nomes das searchs
    //cout << "LISTA\n";
    for(i=0; i<n; i++){
      getline(cin, aux);
      nomes[aux]=num++;
      //cout<< num <<" " << aux << "\n";
    }
    for(i=0; i<n; i++){
      busca[i][0]=0;
      //cout << "0  ";
    }
    //cout << "\n"; 
    scanf("%d\n", &s);
    //lista de buscas
    for(i=1; i<=s; i++){//as buscas comecam em 1
      getline(cin, aux);
      //cout<< i << " "<<aux << " ";
      iter= nomes.find(aux);
      if( iter != nomes.end() ) {//Aux sempre vai estar de 1 a N
	min=s+1;//infinito
	for(j=0; j<n; j++){
	  if(busca[j][i-1]!=-1&&min>busca[j][i-1]) {
	    min=busca[j][i-1];
	  }
	}
	for(j=0; j<n; j++){
	  if(j==iter->second) busca[j][i]=-1;
	  else {
	    anterior=busca[j][i-1];
	    if(anterior==-1){//Trocou de fila
	      busca[j][i]=min+1;
	    }
	    else{
	      if(anterior<min+1) busca[j][i]=anterior;//sem trocar
	      else busca[j][i]=min+1;//trocando
	    }
	  }
	  //bizu  cout <<busca[j][i]<<"  ";
	}
	//bizu cout<< "\n";
      }
      
    }
    //printf("final\n");
    ans=s+1;// infinito
    for(i=0; i<n; i++){
      //cout<< busca[i][s];
      if(busca[i][s]!=-1&&ans>busca[i][s]) ans=busca[i][s];
    }
    //cout<<"\n";
    printf("Case #%d: %d\n", t++, ans);
    
  }
  return 0;
}
