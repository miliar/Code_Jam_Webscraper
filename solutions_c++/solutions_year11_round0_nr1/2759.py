#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

/* Saul Hidalgo
   Venezuela xD*/

using namespace std;

int main(){
  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    queue<int> robotO, robotB;
    vector< string > seq;
    int tam;
    cin >> tam;
    for (int i = 0; i < tam; i++) {
      string r;
      int button;
      cin >> r >> button;
      if (r == "O") {
        robotO.push(button);
      }else {
        robotB.push(button);
      }
      seq.push_back( r );
    }

    int ans = 0;
    int posO = 1, posB = 1 , act = 0;
    while ( !robotO.empty() || !robotB.empty() ) {
      if (seq[act] == "O") {
        if ( !robotO.empty()) {
          if ( posO > robotO.front() ) {
            --posO;
          }else if ( posO < robotO.front() ){
            ++posO;
          }else {
            ++act;
            robotO.pop();
          }
        }
        if ( !robotB.empty() ){
          if ( posB > robotB.front() ) {
            --posB;
          }else if ( posB < robotB.front() ) {
            ++posB;
          }else {
            ;
          }
        }
      }else {
        if ( !robotO.empty() ){
          if ( posO > robotO.front() ) {
            --posO;
          }else if ( posO < robotO.front() ){
            ++posO;
          }else {
            ;
          }
        }
        if ( !robotB.empty() ){
          if ( posB > robotB.front() ) {
            --posB;
          }else if ( posB < robotB.front() ) {
            ++posB;
          }else {
            ++act;
            robotB.pop();
          }
        }
      }

      ++ans;
    }
  
    cout << "Case #" << caso << ": " << ans << endl;
    
  }
  return 0;
}


