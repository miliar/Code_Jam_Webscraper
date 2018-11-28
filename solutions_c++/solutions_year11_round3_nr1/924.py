#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

int main(){
  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    int x,y;
    cin >> x >> y;
    string tablero[60];
    for (int i = 0; i < x; i++) {
      cin >> tablero[i];
    }
    for (int i = 0; i < x-1; i++) {
      for (int j = 0; j < y-1; j++) {
  //      cout << i << " " << j << endl;
        if ( tablero[i][j] == '#' && 
              tablero[i+1][j] == '#' &&
              tablero[i][j+1] == '#' &&
              tablero[i+1][j+1] == '#') {
//          cout << "Entro  " << endl;
          tablero[i][j] = '/';
          tablero[i+1][j] = '\\';
          tablero[i][j+1] = '\\';
          tablero[i+1][j+1] = '/';
        }
      }
    }
    bool bien = true;
    for (int i = 0; i < x; i++) {
      for (int j = 0; j < y; j++) {
        if (tablero[i][j] == '#') {
          bien = false;
        }
      }
    }
    cout << "Case #" << (caso) << ":" << endl;
    //bien = 1;
    if (!bien) {
      cout << "Impossible" << endl;
    }else {
      for (int i = 0; i < x; i++) {
        cout << tablero[i] << endl;
      }
    }
  }
  return 0;
}


