#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int x = 1; x <= t; x++){
            char a[4][4];
            bool filled = true;
            bool finished = false;
            for(int i = 0; i < 4; i++)
                    for(int j = 0; j < 4; j++){
                            cin >> a[i][j];
                            if(a[i][j] == '.') filled = false;
                    }
            cout << "Case #" << x << ": ";
            for(int i = 0; i < 4 && !finished; i++){
                    bool thesame = true;
                    int start = 0;
                    if(a[i][0] == 'T') start++;
                    if(a[i][start] != '.'){
                        for(int j = start + 1; j < 4; j++){
                                if(a[i][j] != a[i][start] && a[i][j] != 'T'){
                                           thesame = false;
                                           break;
                                }
                        }
                        if(thesame) { cout << a[i][start] << " won" << endl; finished = true; }
                    }
            }
            if(!finished){
            for(int i = 0; i < 4 && !finished; i++){
                    bool thesame = true;
                    int start = 0;
                    if(a[0][i] == 'T') start++;
                    if(a[start][i] != '.'){
                        for(int j = start + 1; j < 4; j++){
                                if(a[j][i] != a[start][i] && a[j][i] != 'T'){
                                           thesame = false;
                                           break;
                                }
                        }
                        if(thesame) { cout << a[start][i] << " won" << endl; finished = true; }
                    }
            }
            if(!finished){
            bool thesame = true;
            int start = 0;
            if(a[0][0] == 'T') start++;
            if(a[start][start] != '.'){
                    for(int i = start + 1; i < 4; i++){
                            if(a[i][i] != a[start][start] && a[i][i] != 'T'){
                                       thesame = false;
                                       break;
                            } 
                    }
            } else thesame = false;
            if(thesame) { cout << a[start][start] << " won" << endl; finished = true; }
            }
            if(!finished){
            bool thesame = true;
            int start = 0;
            if(a[0][3] == 'T') start++;
            if(a[start][3 - start] != '.'){
                    for(int i = start + 1; i < 4; i++){
                            if(a[i][3 - i] != a[start][3 - start] && a[i][3 - i] != 'T'){
                                       thesame = false;
                                       break;
                            }
                    }
            } else thesame = false;
            if(thesame) { cout << a[start][3 - start] << " won" << endl; finished = true; }
            }
            if(!finished){
                       if(filled) cout << "Draw" << endl;
                       if(!filled) cout << "Game has not completed" << endl;
            }
            }
    }
    return EXIT_SUCCESS;
}
