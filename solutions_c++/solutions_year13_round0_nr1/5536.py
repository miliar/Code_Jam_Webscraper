#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >>T;
    vector<char> vWin (4);
    vector<char> dWin (2);
    bool complete = true;
    char hWin = '.';
    char win = '.';
    
    char cell;
    
    for (int i =1; i <= T; i++) {
        int j = 0;
        win = '.';
        complete = true;
        
        while (j < 16) {
              cin >>cell;
              
              //if noone has win yet
              if (win == '.') {
                  //checking if is complete
                  if (cell == '.') complete = false;         
                  
                  //checking for a horizontal victory
                  if (j % 4 == 0) hWin = cell;
                  if (hWin != '.') {
                      if (j % 4 > 0) {
                           if (cell != 'T') {
                              if (cell != hWin) hWin = '.';
                           }
                      }
                  }
                  if (j % 4 == 3) win = hWin;
              }
                  
              //if noone has win yet
              if (win == '.') {
                  //checking for a vertical victory
                  if (j / 4 == 0) vWin[j%4] = cell;
                  if (vWin[j%4] != '.') {
                      if (j / 4 > 0) {
                           if (cell != 'T') {
                              if (cell != vWin[j%4]) vWin[j%4] = '.';
                           }
                      }
                  }
                  if (j / 4 == 3) win = vWin[j%4];
              }
                  
              //if noone has win yet
              if (win == '.') {
                  //checking for a diagonal victory
                  if ((j%4) - (j/4) == 0) { //diag0
                     if (j/4 == 0) dWin[0] = cell;
                     if (dWin[0] != '.') {
                        if (j / 4 > 0) {      
                            if (cell != 'T') {
                               if (cell != dWin[0]) dWin[0] = '.'; 
                            }
                        }
                     }
                     if (j / 4 == 3) win = dWin[0];         
                  }
                  
                  if ((j%4) + (j/4) == 3) { //diag1
                     if (j/4 == 0) dWin[1] = cell;
                     if (dWin[1] != '.') {
                        if (j / 4 > 0) {      
                            if (cell != 'T') {
                               if (cell != dWin[1]) dWin[1] = '.'; 
                            }
                        }
                     }
                     if (j / 4 == 3) win = dWin[1];   
                  }
              }
              
              
              
              j++;
        }
        
        
        cout <<"Case #" <<i <<": ";
        
        if (win != '.') cout <<win <<" won" <<endl;
        else if (complete) cout <<"Draw" <<endl;
        else cout <<"Game has not completed" <<endl;
    }
}
