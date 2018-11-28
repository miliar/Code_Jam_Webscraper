#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

int main(){

  ifstream fin( "B-small-attempt0.in" ); //B-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "B-small-attempt0.out"); // salida-large.out

  int T;   fin>>T;   cout<<T<<endl;

  for (int t=0; t<T; t++){

      int L;       fin>>L;       cout<<L<<"|";
      long long tt;       fin>>tt;       cout<<tt<<"|"; // lo que demora en construir un acelerador
      int N;       fin>>N;       cout<<N<<"|";
      int C;       fin>>C;       cout<<C<<"||";

      vector<int> as;
      for (int c=0; c<C; c++){

          int a;           fin>>a;           cout<<a<<"|";
          as.push_back(a);

      }
      cout<<endl;

      vector <double> estrellas;
      int j=0;
      cout<<"[";
      for (int n=0; n<N; n++){
          double estrella;
          estrella=as[j];
          estrellas.push_back(estrella);
          j++;
          if (j==C) j=0;
  //        cout<<estrella<<",";
      }
      cout<<"]"<<endl;

      double resp=0;

      //descontar tt y borrar los primeros items (ojo puede que borre todo)
      for (;;){
          if (estrellas[0]*2<=tt){
              tt=tt-estrellas[0]*2;
              resp+=estrellas[0]*2;
              estrellas.erase(estrellas.begin());

          } else {
              estrellas[0]=estrellas[0]-tt/2.0; resp+=tt; break;

          }

          if (estrellas.size()==0) break; // OJO, YA LLEGUE.
      }

/*
      cout<<"[";
      for (int n=0; n<estrellas.size(); n++){
          cout<<estrellas[n]<<",";
      }
      cout<<"]"<<endl;

*/
      if (estrellas.size()==0) { // YA LLEGUE
          fout<<"Case #"<<t+1<<": "<<(int)resp<<endl;
      } else {

          // Burbuja de estrellas, primero las distancias mayores
        for (int i=0; i+1<estrellas.size(); i++){
          for (int k=i+1; k<estrellas.size(); k++){
              double aux;
              if (estrellas[i]<estrellas[k]) {
                  aux=estrellas[i];
                  estrellas[i]=estrellas[k];
                  estrellas[k]=aux;
              }
          }
        }
/*
      cout<<"[";
      for (int n=0; n<estrellas.size(); n++){
          cout<<estrellas[n]<<",";
      }
      cout<<"]"<<endl;
*/
        for (int l=0; l<estrellas.size() && l<L; l++){
            estrellas[l]=estrellas[l]/2.0;
        }


/*      cout<<"[";
      for (int n=0; n<estrellas.size(); n++){
          cout<<estrellas[n]<<",";
      }
      cout<<"]"<<endl;
      cout<<resp<<" ";
*/

        for (int e=0; e<estrellas.size(); e++){
            resp+=estrellas[e]*2;
            cout<<resp<<" ";
        }
        fout<<"Case #"<<t+1<<": "<<(int)resp<<endl;

      }
  }

  fin.close();
  fout.close();
  return 0;
}
