#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int main(){
  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    int nPlayers, L , H;
    cin >> nPlayers >> L >> H;
    vector<int> players;
    for (int i = 0; i < nPlayers; i++) {
      int tmp;
      cin >> tmp;
      players.push_back( tmp );
    }
    cout << "Case #" << (caso) << ": ";
    bool listo = false;
    for (int nota = L; nota <= H; nota++) {
      bool bien = true;
      for (int i = 0; i < nPlayers && bien ; i++) {
        if (players[i]%nota == 0 || nota%players[i] == 0) {
          ;
        }else {
          bien = false;
        }
      }
      if (bien) {
        cout << nota << endl;
        listo = 1;
        break;
      }
    }
    if (!listo) {
      cout << "NO" << endl;
    }
  }
  return 0;
}


