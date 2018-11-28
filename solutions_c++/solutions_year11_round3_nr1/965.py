#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int main (){
    int T;
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    fin >>T;
    for (int cas=1; cas<=T; cas++){
      int a,b;
      fin >>a>>b;
      vector <vector <char> > v (a, vector <char> (b,'.'));
      for (int i=0; i<a; i++){
          for (int k=0; k<b; k++) fin >>v[i][k];
      }
      for (int i=0; i<a-1; i++){
          for (int k=0; k<b-1; k++){
               if (v[i][k]=='#' and v[i][k+1]=='#' and v[i+1][k]=='#' and v[i+1][k+1]=='#'){
                  v[i][k]='/'; v[i][k+1]='\\'; v[i+1][k]='\\'; v[i+1][k+1]='/'; 
               }
          }
      }
      bool pot=false;
      for (int i=0; i<a; i++){
          for (int k=0; k<b; k++){
               if (v[i][k]=='#'){
                  pot=true;
               }
          }
      }
      fout <<"Case #"<<cas<<":"<<endl;
      if (pot) fout <<"Impossible"<<endl;
      else {
           for (int i=0; i<a; i++){
               for (int k=0; k<b; k++) fout <<v[i][k];
               fout <<endl;
           }
      }
    }
}
