#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

string teams[102];
int tam;

int main(){
  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    cin >> tam;
    for (int i = 0; i < tam; i++) {
      cin >> teams[i];
    }
    
    double wp[102], owp[102], oowp[102];
    for (int i = 0; i < 102; i++) {
      wp[i] = owp[i] = oowp[i] = .0;
    }
    
    for (int i = 0; i < tam; i++) {
      double bien = 0 , total = 0;
      for (int j = 0; j < teams[i].size() ; j++) {
        if (teams[i][j] == '1') {
          ++bien;
        }
        if (teams[i][j] != '.') {
          ++total;
        }
      }
      wp[i]=bien/total;
    }
 /*
    for (int i = 0; i < tam; i++) {
      cout << wp[i] << endl;
    }
    int cuanto[102];
    memset(cuanto,0,sizeof(cuanto));
    for (int i = 0; i < tam; i++) {
      int c = 0;
      for (int j = 0; j < teams[i].size() ; j++) {
        if (teams[i][j] != '.') {
          ++c;
        }
      }
      cuanto[i]=c;
    }*/
   
     
 
    for (int i = 0; i < tam; i++) {
      double bien = 0 , mal = 0;
      bool against[102];
      memset(against,0,sizeof(against));
      double av = 0;
      double total = 0;
      for (int ii = 0; ii < teams[i].size() ; ii++) {
        if (teams[i][ii] != '.') {
          double bien = 0 , totall = 0;
          for (int j = 0; j < tam; j++) {
            if (i != j) {
              
            
              if (teams[ii][j] == '1') {
                ++bien;
              }
              if (teams[ii][j] != '.') {
                ++totall;
              }
            }
          }
          av += bien/totall;
          ++total;
        }
      }

      av /= total;
      owp[i] = av;
    }
    for (int i = 0; i < tam; i++) {
      //cout << owp[i] << endl;
    }

    for (int i = 0; i < tam; i++) {
      double bien = 0 , mal = 0;
      bool against[102];
      memset(against,0,sizeof(against));
      double av = 0;
      double total = 0;
      for (int ii = 0; ii < teams[i].size() ; ii++) {
        if (teams[i][ii] != '.') {
          av += owp[ii];
          ++total;
        }
      }
      av /= total;
      oowp[i] = av;
    }
    cout << "Case #" << (caso) << ":" << endl;
    for (int i = 0; i < tam; i++) {
      cout << (.25*wp[i]+.5*owp[i]+.25*oowp[i]) << endl;
    }

  }
  return 0;
}


