#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;
char mat[50][50];


int main(){
    int T, R, C;
    int c = 1;
    cin >> T;
    while(T--){
        cin >> R >> C;
        char tmp;
        for(int i = 0; i < R; ++i){
            for(int j = 0; j < C; ++j){
                cin >> tmp;
                mat[i][j] = tmp;
            }
        }
        
        bool possible = true;
        for(int i = 0; i < R and possible; ++i){
            for(int j = 0; j < C and possible; ++j){
                if(mat[i][j] == '#'){
                    if(i == R-1 or j == C-1){
                        possible = false;
                    }
                    else{
                        if(mat[i+1][j] == '#' and mat[i][j+1] == '#' and mat[i+1][j+1] == '#'){
                            mat[i][j] = '/';
                            mat[i][j+1] = '\\';
                            mat[i+1][j] ='\\';
                            mat[i+1][j+1] ='/';
                        }
                        else{
                            possible = false;
                        }
                    }
                }
            }
        }
        
        printf("Case #%d:\n", c++);
        if(possible){
            for(int i = 0; i < R; ++i){
                for(int j = 0; j < C; ++j){
                    cout << mat[i][j];
                }
                cout << endl;
            }
        }
        else
            puts("Impossible");
    }
    return 0;
}
