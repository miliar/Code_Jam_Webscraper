#include <fstream>
#include <string>
#include <iostream>

using namespace std;

main(){

  ifstream in("A-large.in");
  ofstream out("A-large.out");
  int L,D,N;
  string palabra;
  
  in >> L >> D >> N;

  string diccionario[D];
  string palabras;
  string verifik[L];

  for(int i=0; i < D ; i++){
    in >> diccionario[i];
  }

  for(int i=0; i < N ; i++){
    in >> palabra;
  
    int j=0,p=0;

    while(palabra[j] != '\0'){
      if (palabra[j] == '('){
	palabras = "";
	j++;

	do{
	  palabras = palabras + palabra[j];
	  j++;
	}while(palabra[j] != ')');

        verifik[p] = palabras;
	p++;
      }else{
	verifik[p] = palabra[j];
	p++;
        }
      j++;
      }

    //revisar
     int ct = 0;
     for(int z=0 ; z < D ; z++){
	bool band = true;
	int found = 0;
	for(int x=0 ; x < L ; x++){
	  found = verifik[x].find(diccionario[z][x]);
	  if (found == -1){
	    band = false;
	    break;
	  }
	}
	if(band)
	  ct++;
      }
    
      out << "Case #"<<i+1<<":"<<" "<<ct<<endl;

  }
    
}


/*for(int i=0; i < L ; i++){
      cout << verifik[i] << endl;
      }*/
 /*for(int i=0; i < D ; i++){
    cout << diccionario[i] << endl;
  }*/
