#include <iostream>
#include <vector>

using namespace std;

int N,M;
bool v(int x, int y){
     return x >= 0 && y >= 0 && x < N && y < M;
}

int main(){
    int Tc;
    cin >> Tc;
    for(int tc=1; tc <= Tc; tc++){
            cin >> N >> M;
            vector<string> T(N);
            for(int i=0;i<N;i++) cin >> T[i];
            bool valid = 1;
            for(int j=0;j<M && valid;j++) for(int i=0;i<N && valid;i++){
                    if(T[i][j] == '#'){
                               T[i][j] = '/';
                               int dx[] = {1, 1, 0}, dy[] = {0, 1, 1};
                               char c[] = { '\\', '/', '\\' };
                               for(int k=0;k<3 && valid;k++){
                                       if(!v(i+dx[k], j+dy[k]) || T[i+dx[k]][j+dy[k]] != '#'){
                                                     valid = 0;
                                                     break;
                                       }
                                       T[i+dx[k]][j+dy[k]] = c[k];
                               }
                               
                    }
            }
            cout << "Case #" << tc << ":" << endl;
            if(!valid) cout << "Impossible" << endl;
            else for(int i=0;i<N;i++) cout << T[i] << endl;
    }
}
