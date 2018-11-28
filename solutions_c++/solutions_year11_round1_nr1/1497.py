#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>  // para abs(float)
#include <cstdlib> // para abs(int)
#include <sstream>  // para manipular strings

using namespace std;

int pos(char e, string s){
    int i=0;
    while (e!=s[i]) i++;
    return i;
}

int main(){

  ifstream fin( "A-small-attempt1.in" ); //A-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "A-small-attempt1.out"); // salida-large.out");
  int T; // casos de Testeo

  fin>>T;
  cout<<T<<endl;
  int N, PD, PG;

  for(int t=0; t<T; t++){
      fin>>N;
      fin>>PD;
      fin>>PG;

      cout<<N<<" "<<PD<<" "<<PG<<endl;
      bool resp=false;
      for (int j=1; j<=N; j++){
          // cout<<j<<" "<<j*PD<<" "<<j*PD%100;
          if (j*PD%100==0) {
              cout<<j<<" "<<j*PD<<" "<<j*PD%100;
              resp=true; cout<<"posible pues: Ganados Hoy="<<j*PD/100<<endl;}
      }

      if (PG==100&& PG>PD) resp=false;
      if (PG==0&& PG<PD) resp=false;

      if (resp==false){
      fout<<"Case #"<<t+1<<": Broken"<<endl;
      } else {
      fout<<"Case #"<<t+1<<": Possible"<<endl;
      }
  }

  fin.close();
  fout.close();

  return 0;
}
