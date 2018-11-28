#include <iostream>
#define MAX 105
using namespace std;

int mat[MAX][MAX];
int t,r;

int getN(int x,int y) {
    int nx = x-1;
    if (nx < 0)
       return -1;
    
    return mat[nx][y];
}

int getW(int x,int y) {
    int ny = y-1;
    if (ny < 0)
       return -1;
    
    return mat[x][ny];
}

int main() {
    cin >> t;
    for (int i=1;i<=t;i++) {
        cin >> r;
        for (int x=0;x<MAX;x++)
        for (int y=0;y<MAX;y++)
            mat[x][y] = 0;
            
            
        for (int l=1;l<=r;l++) {
            int x1,x2,y1,y2;
            cin >> y1 >> x1 >> y2 >> x2;
            for (int x=x1;x<=x2;x++)
            for (int y=y1;y<=y2;y++)
                mat[x][y] = 1;
        }
        int nu = 0;
        while (true) {
              //cout << "New round: " << nu << endl;
              
              //for (int x=1;x<7;x++)  {
              //for (int y=1;y<7;y++)
              //    cout << mat[x][y];
              //    cout << endl;
              //}
              int none = 0;
              for (int x=0;x<MAX;x++)
              for (int y=0;y<MAX;y++) {
                  if (mat[x][y]) {
                     none++;
                     if ((getN(x,y) == 0 || getN(x,y) == 3) && (getW(x,y) == 0 || getW(x,y) == 3)) {
                   //cout << x << " , " << y << " died" << endl;
                        mat[x][y] = 2;
                     }
                  }
                  else { 
                     if ((getN(x,y) == 1 || getN(x,y) == 2) && (getW(x,y) == 1 || getW(x,y) == 2)) {
                   //cout << x << " , " << y << " lived" << endl;
                        mat[x][y] = 3;  
                     }              
                  }
              }
              
            for (int x=0;x<MAX;x++)
            for (int y=0;y<MAX;y++)
                if (mat[x][y]==2) {
                   mat[x][y] = 0;
                   }
                else
                if (mat[x][y] == 3) {
                   mat[x][y] = 1;
                }
                   
              if (none == 0)
                 break;
              nu++;
        }
        cout << "Case #" << i << ": " << nu << endl;
    }
    return 0;
}
