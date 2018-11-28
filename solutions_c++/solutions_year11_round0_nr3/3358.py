#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;
vector <int> caramelos;
long resp=0;

int imprimir (vector <int> sean, vector <int> patric){
    cout<<"sean: ";
    for (int i=0; i<sean.size(); i++){
        cout<<sean[i]<<" ";
    }

    cout<<"patric: ";
    for (int i=0; i<patric.size(); i++){
        cout<<patric[i]<<" ";
    }
    cout<<endl;


}

int solucionar( int posicion, vector<int> sean, vector <int> patric)
{
  if (posicion==caramelos.size()) {
     // cout<<"adentro:"<<endl;
    if ((sean.size()>0) && (patric.size()>0)){
      // decidir y responder
      // sumar sean
      int ss=sean[0];
      for (int i=1; i<sean.size(); i++){
          ss=ss^sean[i];
      }

      // sumar patric
      int sp=patric[0];
      for (int i=1; i<patric.size(); i++){
          sp=sp^patric[i];
      }

    //  cout<<"llega: sp="<<sp<<" |ss="<<ss<<endl;

      if (sp==ss){
          ss=0;
          for (int i=0; i<sean.size(); i++){
          ss+=sean[i];
          }
         // cout<<" sean tiene:"<<ss;

          sp=0;
          for (int i=0; i<patric.size(); i++){
          sp+=patric[i];
          }

          if (ss>sp) sp=ss;
          if (sp>resp) resp=sp;
      }
    }
  } else {
      // asignar a sean
      sean.push_back(caramelos[posicion]);
     // imprimir (sean, patric);
      solucionar(posicion+1, sean, patric);

      // asignar a patric
      sean.erase(sean.end()-1);
      patric.push_back(caramelos[posicion]);
     // imprimir (sean, patric);
      solucionar(posicion+1, sean, patric);
  }

 // cout<<"antes de salir";

  return 0;
}

int main(){

   // cout<<(288762&332610)<<endl;

  ifstream fin( "C-small-attempt1.in" ); //A-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "C-small-attempt1.out"); // salida-large.out");
  int T; // casos de Testeo

  fin>>T;
 // cout<<T<<endl;

  //Leer Caso Siguiente
  for (int t=0; t<T; t++ ){

      //Memorizar transformaciones a no-base
      int N;
      fin>>N;
 //     cout<<N<<" "<<endl;

      caramelos.clear();

      for (int c=0; c<N; c++){
          int aux;
          fin>>aux;
          caramelos.push_back(aux);
   //       cout<<aux<<" ";
      }
      vector <int> sean;
      vector <int> patric;
      sean.push_back(caramelos[0]);
      resp=0;

      solucionar(1, sean, patric);

    fout<<"Case #"<<t+1<<": ";
    if (resp==0){
        fout<<"NO"<<endl;}
    else {
        fout<<resp<<endl;
    }
  }

  fin.close();
  fout.close();
  return 0;
}
