

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

  ifstream in("input");
  ofstream out("output");

  int T;
  in >> T;
  for(int i = 0; i < T; i++){

    int R, C;
    in >> R >> C;
    vector<string> row(R);
    vector<string> result(R);
    for(int i = 0; i < R; i++){
      in >> row[i];
      result[i].resize(C,'.');
    }
    
    bool ok = 1;
    
    if(R == 1 || C == 1){
      for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++) 
          if(row[i][j] == '#') ok = 0;
    }else{
      for(int i = 0; i < R-1; i++)
        for(int j = 0; j < C-1; j++){
          if(row[i][j] == '#' && row[i+1][j] == '#' && row[i][j+1] == '#' && row[i+1][j+1] == '#'){
            row[i][j] = '.';
            row[i+1][j] = '.';
            row[i][j+1] = '.';
            row[i+1][j+1] = '.';
            
            result[i][j] = '/';
            result[i][j+1] = '\\';
            result[i+1][j] = '\\';
            result[i+1][j+1] = '/';
          }
        }
      
      for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++){
          if(row[i][j] == '#'){
            ok = 0;
            break;
          }
        }
    }
    
    out << "Case #" << i+1 << ":\n";
    if(ok){
      for(int i = 0; i < R; i++){
        out << result[i] << "\n";
      }
    }
    else out << "Impossible\n";
    
  }


  return 0;
}



