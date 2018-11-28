#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

bool to_be_completed(vector<string> V) {
     for (int i=0; i<4; i++) for (int j=0; j<4; j++) if (V[i][j]=='.') return true;
     return false;
     }

bool win(vector<string> V, char C) {
     bool doable;
     for (int i=0; i<4; i++) {
          doable=true;
          for (int j=0; j<4; j++) if (V[i][j]!=C && V[i][j]!='T') doable=false;
          if (doable) return true;
          }
     for (int i=0; i<4; i++) {
          doable=true;
          for (int j=0; j<4; j++) if (V[j][i]!=C && V[j][i]!='T') doable=false;
          if (doable) return true;
          }
     doable=true;
     for (int j=0; j<4; j++) if (V[j][j]!=C && V[j][j]!='T') doable=false;
     if (doable) return true;

     doable=true;
     for (int j=0; j<4; j++) if (V[3-j][j]!=C && V[3-j][j]!='T') doable=false;
     if (doable) return true;
     
     return false;
     }

int main(void) {
     ifstream IN("A2.in");
     ofstream OUT("A2.out");
     int num_test;
     IN>>num_test;
     cout<<num_test<<"\n";
     for (int test=1; test<=num_test; test++) {
          string S;
          vector<string> V(4);
          IN>>V[0]>>V[1]>>V[2]>>V[3];
          
          string RES="Draw";
          if (to_be_completed(V)) RES="Game has not completed";
          if (win(V, 'X')) RES="X won";
          if (win(V, 'O')) RES="O won";
          OUT<<"Case #"<<test<<": "<<RES<<"\n";
          }
          
     system("pause");
     return 0;
     }
