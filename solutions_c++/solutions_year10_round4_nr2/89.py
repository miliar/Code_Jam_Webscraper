#include <iostream>
using namespace std;

int T, P;
int m[1024];
int price[10][512];
int mincost[11][1024];
int n;


int main(int argc, char *argv[]) {

  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    for(int i=0; i<=10; i++) {
      for(int j=0; j<1024; j++) {
        mincost[i][j] = -1;
      }
    }



    cin >> P >> ws;
    n = (1 << P);
    for(int i=0; i<n; i++) {
      cin >> m[i];
      for(int j=0; j<=m[i]; j++) {
        mincost[j][i] = 0;
      }
    }
    
    for(int p=0; p<P; p++) {
      for(int i=0; i<(1<<(P-p-1)); i++) {
        cin >> price[p][i];
      }
    }
    
    for(int p=0; p<P; p++) {
      for(int i=0; i<(1<<(P-p-1)); i++) {
        for(int j=0; j<10; j++) {
          if(mincost[j][2*i] == -1 || mincost[j][2*i+1] == -1) {
            mincost[j][i] = -1;
          } else if(mincost[j+1][2*i] == -1 || mincost[j+1][2*i+1] == -1) {
            mincost[j][i] = price[p][i] + mincost[j][2*i] + mincost[j][2*i+1];
          } else {
            mincost[j][i] = min(price[p][i] + mincost[j][2*i] + mincost[j][2*i+1], mincost[j+1][2*i] + mincost[j+1][2*i+1]);
          }
        }
      }
    }
    
    
    cout << "Case #" << t << ": " << mincost[0][0] << endl;

  }
  
  return 0;
}
