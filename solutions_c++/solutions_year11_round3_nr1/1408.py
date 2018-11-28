#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

int n, m;
vector <string> v(n);
ifstream fin("a-small-in.txt");
ofstream fout("a-small-out.txt");

void ompleq(int ix, int jx){
     v[ix][jx] = 47;
     v[ix][jx+1] = 92;
     v[ix+1][jx] = 92;
     v[ix+1][jx+1] = 47;
}

int main(){
    int c;
    while (fin >>c){
          for (int d = 0; d < c; d++){
              fin >>n>>m;
              v = vector <string> (n);
              for (int i = 0; i < n; i++) fin >>v[i];
              
              for (int i = 0; i < n; i++){
                  for (int j = 0; j < m; j++){
                      if (j<=m-2 and i<=n-2){
                         if (v[i][j] == '#' and v[i+1][j]=='#' and v[i][j+1]=='#' and v[i+1][j+1]=='#') ompleq(i, j);
                      }
                  }
              }
              bool b = true;
              for (int i = 0 ; i < n; i++){
                  for (int j = 0; j < m; j++){
                      if (v[i][j] == '#') b = false;
                  }
              }
              fout <<"Case #"<<d+1<<":"<<endl;
              if (!b) fout <<"Impossible"<<endl;
              else {
                   for (int i = 0; i < n; i++) fout <<v[i]<<endl;
              }
          }
    }
}
