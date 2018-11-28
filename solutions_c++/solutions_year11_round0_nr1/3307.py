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

  ifstream fin( "A-large.in" ); //A-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "A-large.out"); // salida-large.out");
  int T; // casos de Testeo


  fin>>T;
  cout<<T<<endl;
  string aux;
  int ai;
  //getline(fin,aux);
  int N; // Numero de Botones que necesitan ser presionados
  vector <int> boton;
  vector <string> color;

  int ta=0; // tiempo actual
  int tO=0; // tiempo de la ultima posicion de Orange
  int pO=1; // posicion de Orange en el tiempo tO
  int tB=0; // tiempo de la ultima posicion de Blue
  int pB=1; // posicion de Blue en el tiempo tB

  for (int t=0; t<T; t++){
      boton.clear();
      color.clear();

      ta=0; // tiempo actual
      tO=0; // tiempo de la ultima posicion de Orange
      pO=1; // posicion de Orange en el tiempo tO
      tB=0; // tiempo de la ultima posicion de Blue
      pB=1; // posicion de Blue en el tiempo tB


      fin>>N;
      cout<<N;

      for (int n=0; n<N; n++){
          fin>>aux;
          fin>>ai;
          boton.push_back(ai);
          color.push_back(aux);
          // Obs: aux es el boton que debe presionar cierto robot.
          if (color[n][0]=='O'){
              int desp;
              int tOcup;
              if (pO>ai){ desp=pO-ai; } else desp=ai-pO;
              tOcup=ta-tO;
              if (desp>tOcup) ta=tO+desp;
              ta++; // tiempo que tarda en presionar el boton.
              tO=ta;
              pO=ai;
          } else {
              int desp;
              int tOcup;
              if (pB>ai){ desp=pB-ai; } else desp=ai-pB;
              tOcup=ta-tB;
              if (desp>tOcup) ta=tB+desp;
              ta++; // tiempo que tarda en presionar el boton.
              tB=ta;
              pB=ai;
          };

          cout<<" "<<aux<<" "<<ai<<"("<<ta<<")";
      };
      cout<<endl;
      fout<<"Case #"<<t+1<<": "<<ta<<endl;

  }

  fin.close();
  fout.close();
  return 0;
}
