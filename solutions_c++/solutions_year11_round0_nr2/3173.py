#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

int pos(char e, string s){
    int i=0;
    while (e!=s[i]) i++;
    return i;
}

int main(){

  ifstream fin( "B-large (1).in" ); //A-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "B-large (1).out"); // salida-large.out");
  int T; // casos de Testeo


  fin>>T;
  cout<<T<<endl;

  //Leer Caso Siguiente
  for (int t=0; t<T; t++ ){

      //Memorizar transformaciones a no-base
      int C;
      fin>>C;
      cout<<C<<" ";

      vector<string> transforma;
      transforma.clear();

      for (int c=0; c<C; c++){
          string aux;
          fin>>aux;
          transforma.push_back(aux);
          cout<<aux<<" ";
      }

      //Memorizar Opuestos
      int D;
      fin>>D;
      cout<<D<<"|";

      vector<string> opuestos;
      opuestos.clear();

      for (int d=0; d<D; d++){
          string aux;
          fin>>aux;
          opuestos.push_back(aux);
          cout<<aux<<" ";
      }

      //Memorizar caracteres base
      int N;
      fin>>N;
      cout<<N<<"|";
      string bases;
      fin>>bases;
      cout<<bases<<endl;

      // Aumentar caracteres uno a uno en lista
      vector <char> resultado;
      for (int pos=0; pos<bases.length(); pos++){
          cout<<"("<<bases[pos] <<")";
        if (resultado.size()==0){
            resultado.push_back(bases[pos]);
        }
        else{

        // Transformar a  no-Base, si hay transofrmacion al final
            // busco si el que voy a agregar, base[pos], esta en algun lugar de transforma y en ese caso transformo
            bool transf=false;
            for (int tr=0; tr<transforma.size(); tr++){
                if (transforma[tr][0]==bases[pos]){
                    if (transforma[tr][1]==resultado[(resultado.size())-1])
                    {
                        resultado[(resultado.size())-1]=transforma[tr][2];
                        transf=true;
                        break;
                    }
                }

                if (transforma[tr][1]==bases[pos]){
                    if (transforma[tr][0]==resultado[(resultado.size())-1])
                    {
                        resultado[(resultado.size())-1]=transforma[tr][2];
                        transf=true;
                        break;
                    }
                }
            }

            // si no se transforma puede que haya que borrar opuestos
            if (!transf) {
                bool borrar=false;
                // Borrar opuestos, si corresponde
                for (int op=0; op<opuestos.size(); op++){
                    if (opuestos[op][0]==bases[pos]){
                        for (int r=0; r<resultado.size(); r++){
                            if (opuestos[op][1]==resultado[r]){
                                borrar=true;
                            }
                        }
                    }
                    if (opuestos[op][1]==bases[pos]){
                        for (int r=0; r<resultado.size(); r++){
                            if (opuestos[op][0]==resultado[r]){
                                borrar=true;
                            }
                        }
                    }

                }
                if (borrar){
                    resultado.clear();
                }
                // si no hay problemas agregar el nuevo.
                else{
                    resultado.push_back(bases[pos]);
                }
            }
        }
      }
    fout<<"Case #"<<t+1<<": [";
    for (int r=0; r<resultado.size(); r++){
        fout<<resultado[r];
        if (r+1!=resultado.size()) fout<<", ";
    }
    fout<<"]"<<endl;
  }

  fin.close();
  fout.close();
  return 0;
}
