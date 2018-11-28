#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    int R;
    int C;
    char graph[70][70];
    bool result = true;
    int directx[3] = {1, 0, 1};
    int directy[3] = {0, 1, 1};
    char rep[3] = {'\\', '\\', '/'};
    for( int t = 0; t < T; t++ ){
        result = true;
        cin >> R;
        cin >> C;
        for( int r = 0; r < R; r++ ){
            for(int c = 0; c < C; c++ ){
                cin >> graph[r][c];
            }
        }
        for( int r = 0; r < R; r++ ){
            for(int c = 0; c < C; c++){
                if( graph[r][c] == '#' ){
                    graph[r][c] = '/';
                    if( r == R-1 || c == C-1 ){
                        result = false;
                        break;
                    }
                    else{
                        for(int i = 0; i < 3; i++ ){
                            if(graph[r+directy[i]][c+directx[i]] == '#')
                                graph[r+directy[i]][c+directx[i]] = rep[i];
                            else{
                                result = false;
                                break;
                            }   
                        }
                        if(result == false)
                            break;
                    }
                    
                }
            }
            if(result == false)
                break;
        }
        cout << "Case #" << t+1 << ":" << endl;
        if( result ){
            for( int r = 0; r < R; r++){
                for( int c = 0; c < C; c++){
                    cout << graph[r][c];
                }
                cout << endl;
            }
        }
        else
            cout << "Impossible" << endl;
    }
}
