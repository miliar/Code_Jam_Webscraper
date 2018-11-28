#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

int main(){

  ifstream fin( "A-small-attempt0.in" ); //A-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "A-small-attempt0.out"); // salida-large.out

  int T;   fin>>T;   cout<<T<<endl;

  for (int t=0; t<T; t++){
      int R;       fin>>R;       cout<<R<<"||";
      int C;       fin>>C;       cout<<C<<endl;


      vector<string> lineas;
      for (int r=0; r<R; r++){

          string linea;           fin>>linea;          cout<<linea<<endl;
          lineas.push_back(linea);

      }
      cout<<endl;

      bool posible=true;

      for (int r=0; r<R; r++){
          for (int c=0; c<C; c++){
              if (lineas[r][c]=='#') {
                  // VEO SI ES POSIBLE:
                  if (r+1<R && c+1<C) {
                      if (((lineas[r+1][c]=='#')&&(lineas[r+1][c+1]=='#'))&&(lineas[r][c+1]=='#')){
                          //lineas[r].replace(c,1,1,'/'); lineas[r][c+1]='\\';
                          lineas[r][c]='/'; lineas[r][c+1]='\\';
                          lineas[r+1][c]='\\';  lineas[r+1][c+1]='/';
                      }
                  } else {
                      posible=false; break;
                  }
              }
          }
          cout<<r<<lineas[r]<<endl;
          if (posible==false) break;
      }


      if (posible) {
        fout<<"Case #"<<t+1<<": "<<endl;
        for (int r=0; r<R; r++){
          fout<<lineas[r]<<endl;
        }

      } else {
        fout<<"Case #"<<t+1<<":"<<endl<<"Impossible"<<endl;
      }
  }

  fin.close();
  fout.close();
  return 0;
}
