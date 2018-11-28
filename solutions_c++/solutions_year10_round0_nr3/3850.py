#include <stdio.h>
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main(){
   ofstream fout ("C-small-attempt0.out");
   ifstream fin ("C-small-attempt0.in");
   int t;
   fin>>t;
   for(int i=0; i<t;i++){
      long long r, k, n;
      
      fin>>r;
      fin>>k;
      fin>>n;
      queue<long long> fila;     
      
      for(int j=0; j<n;j++){
        long long aux;
        fin>>aux;
        fila.push(aux);
      }//fim do for
      
      long long soma=0;
      long long grupo;
      int cont;
      int aux;
      for(int j=0;j<r;j++){
        grupo=0;
        cont=0;
        aux= (fila.front());
        while((grupo+(aux)<=k)&&(cont<fila.size())){
          grupo+= aux;
          fila.pop();
          fila.push(aux);
          cont++;
          aux= fila.front();
        }//fim do while
        soma+= grupo;
      }//fim do for
      fout<<"Case #"<<(i+1)<<": "<<soma<<endl;
   }//fim do for
           

}
