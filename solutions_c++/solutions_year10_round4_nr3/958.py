#include <iostream>

using namespace std;

int main(){
    int Nc; cin >> Nc;
    for (int q = 1; q <= Nc; q++){
        int tab[200][200];
        memset(tab,0,sizeof(tab));
        int R; cin >> R;
        for (int i = 0; i < R; i++){
            int X1,X2,Y1,Y2;
            cin >> X1 >> Y1 >> X2 >> Y2;
            for (int j1=X1;j1<=X2;j1++) for (int k1 = Y1; k1 <= Y2; k1++) tab[j1][k1] = 1;
        }
        int nturnos = 0;
        while (true){
              bool move = false;
              int tab2[200][200];
              for (int i=0;i<200;i++){
                  for (int j=0;j<200;j++){
                      if (tab[i][j] && !tab[i][j-1] && !tab[i-1][j]){ tab2[i][j] = 0; move = true; }
                      else if (!tab[i][j] && tab[i][j-1] && tab[i-1][j]){ tab2[i][j] = 1; move = true; }
                      else tab2[i][j] = tab[i][j];
                  }
              }
              for (int i=0;i<200;i++) for (int j=0;j<200;j++) tab[i][j] = tab2[i][j];
              if (!move) break;
              nturnos++;
        }
        cout << "Case #" << q << ": " << nturnos << endl;
    }
    return 0;
}
