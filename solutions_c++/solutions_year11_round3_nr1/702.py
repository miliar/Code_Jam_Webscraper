#include <iostream>
#include <cstdio>

using namespace std;

int N, M;

const int maxN = 101;
char tx[maxN][maxN];
bool sol;

void place(int x, int y){
//    cout << "Sol " << x << " " << y << endl;
    tx[x][y] = '/';
    if(y < M-1 and tx[x][y+1] == '#'){
        tx[x][y+1] = '\\';
    }else{
        sol = false;
        return;
    }
    if(x < N-1 and tx[x+1][y] == '#'){
        tx[x+1][y] = '\\';
    }else{
        sol = false;
        return;
    }
    if(x < N-1 and y < M-1 and tx[x+1][y+1] == '#'){
        tx[x+1][y+1] = '/';
    }else{
        sol = false;
        return;
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> N >> M;
        sol = true;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                char c;
                cin >> c;
                tx[i][j] = c;
            }
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
//                cout << tx[i][j] << " ";
            }
//            cout << endl;
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(tx[i][j]=='#'){
                    place(i, j);
                    if(!sol){
                        break;
                    }
                }
                if(!sol){
                    break;
                }
            }
        }
        cout << "Case #" << t << ":" << endl;
        if(!sol){
            cout << "Impossible" << endl;
        }else{
            for(int i = 0; i < N; i++){
                for(int j = 0; j < M; j++){
                    cout << tx[i][j];
                    if(j != M-1){
//                        cout << " ";
                    }
                }
                cout << endl;
            }
        }
    }
}
