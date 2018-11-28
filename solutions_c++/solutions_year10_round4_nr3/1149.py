#include <iostream>
#include <sstream>
#include <cmath>
#include <cstring>
#include <map>
#define inf 1000000000
#define len(a) int((a).size())
#define pb push_back
#define maxn 110
using namespace std;

int R;
bool T[2][maxn][maxn];

void input(){
    memset(T, 0, sizeof T);
    cin >> R; 
    for (int i = 0; i < R; i++){
        int x1, x2, y1, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for (int j = x1; j <= x2; j++){
            for (int k = y1; k <= y2; k++){
                T[0][j][k] = true;            
            }    
        }    
    }        
}

int solve(){
    int th=0, pr = 1, t = 0;
    
    
    while(true){
        t++;
        th ^= 1;
        pr ^= 1;
        int alive = 0;                
        
               
        for (int i = 1; i < maxn; i++){
            for (int j = 1; j < maxn; j++){
                if (!T[pr][i][j]){
                    T[th][i][j] = T[pr][i-1][j] && T[pr][i][j-1];                                       
                } else {
                    T[th][i][j] = T[pr][i-1][j] || T[pr][i][j-1]; 
                }
                if (T[th][i][j]){
                    alive++;   
                }
            }    
        }
        
        if (alive <= 0){
            return t;    
        }

    }    
    return 0;
}

int main(){
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        input();
        int r = 0;
        if (R != 0){
            r = solve();
        }
        cout << "Case #" << t << ": " << r << endl;
    }
    return 0;    
}
