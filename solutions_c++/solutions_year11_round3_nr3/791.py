#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

int main(){

  ifstream fin( "C-small-attempt0.in" ); //C-small-attempt0.in //A-large.in //pruebita.in
  ofstream fout( "C-small-attempt0.out"); // salida-large.out

  int T;   fin>>T;   cout<<T<<endl;

  for (int t=0; t<T; t++){
      long long N;       fin>>N;       cout<<N<<"||";
      long long L;       fin>>L;       cout<<L<<"|";
      long long H;       fin>>H;       cout<<H<<"|";


      vector<int> fs;
      for (int n=0; n<N; n++){

          int f;           fin>>f;           cout<<f<<"|";
          fs.push_back(f);

      }
      cout<<endl;

      bool resp;
      long long i;
      for (i=L; i<=H; i++){
          resp=true;
          for (int n=0; n<N; n++){
              if (i%fs[n]!=0 && fs[n]%i!=0){
                  resp=false; break;
              }
          }
          if (resp) {
              fout<<"Case #"<<t+1<<": "<<i<<endl;
              break;
          }
      }

      if (!resp){
          fout<<"Case #"<<t+1<<": NO"<<endl;
      }

  }

  fin.close();
  fout.close();
  return 0;
}
