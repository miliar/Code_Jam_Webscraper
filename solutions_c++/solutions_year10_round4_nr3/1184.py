#include <cstdio>
#include <iostream>
#include <cstring>
#define MAXN 300
using namespace std;

int T,n;
int m[2][MAXN][MAXN];
int x1,y1,x2,y2;

int main(){
    cin >> T;
    for (int t = 1; t <= T; t++){
        cin >> n;
        memset(m,0,sizeof(m));
        for (int i = 0; i < n; i++){
            cin >> y1 >> x1 >> y2 >> x2;            
            for (int x = x1; x <= x2; x++)
                for (int y = y1; y <= y2; y++)
                    m[0][x][y] = 1;
        }
        
        int k = 0;
        int g = 0;
        bool ok = n > 0;
        while (ok){
//            for (int i = 1; i <= 20; i++){
//                for (int j = 1; j <= 20; j++)
//                    cout << m[k][i][j];
//                cout << endl;
//            }
//            cout << endl;

            ok = false;
            for (int i = 1; i < MAXN; i++){
                for (int j = 1; j < MAXN; j++){
                    if (m[k][i][j] == 0 && m[k][i-1][j]== 1 && m[k][i][j-1] == 1){
                        m[1-k][i][j] = 1;
                        ok= true;
                    }else
                    if (m[k][i][j] == 1 && m[k][i-1][j]== 0 && m[k][i][j-1] == 0){  
                        m[1-k][i][j] = 0;
                    }else{
                        m[1-k][i][j] = m[k][i][j];
                        ok = ok || m[k][i][j];
                    }
                }
            }
            g++; k = 1 -k;
        }
        cout << "Case #" << t << ": " << g << endl;
    }
    return 0;
}

