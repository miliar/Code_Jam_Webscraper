#include <fstream>
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

void run(istream& input){
  int ncase;
  input >> ncase;

  for(int icase = 0; icase < ncase; ++icase){
    int r, c;
    input >> r >> c;

    vector<string> tiles;
    for(int i = 0; i < r; ++i){
      string tile;
      input >> tile;
      tiles.push_back(tile);
    }

    bool impossible = false;
    for(int i = 0; i < r; ++i){
      for(int j = 0; j < c; ++j){
        string& row = tiles[i];
        if(row[j] == '#'){
          if(j + 1 >= c || i + 1 >= r){
            impossible = true;
            break;
          }

          string& row2 = tiles[i + 1];
          if(row[j + 1] != '#' || row2[j] != '#' || row2[j + 1] != '#'){
            impossible = true;
            break;
          }

          row[j] = '/'; row[j + 1] = '\\';
          row2[j] = '\\'; row2[j + 1] = '/';

        }
      }
      

      if(impossible) break;
    }

    if(impossible)
      printf("Case #%d:\nImpossible\n", icase + 1);
    else {
      printf("Case #%d:\n", icase + 1);
      for(int i = 0; i < r; ++i)
        printf("%s\n", tiles[i].c_str());
    }

  }
}

int main(int argc, char *argv[]){
  if(argc > 1)
    run(ifstream(argv[1]));
  else
    run(cin);
  return 0;
}