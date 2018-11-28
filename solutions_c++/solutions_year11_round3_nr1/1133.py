#include <iostream>
#include <map>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int k = 0; k < t; k++){
        int r, c;
        cin >> r >> c;

        map<int, map<int, char> > picture;
        for(int i = 0; i < r; i++){
            string line;
            cin >> line;
            for(int j = 0; j < c; j++){
                picture[i][j] = line[j];
            }
        }

        bool impossible = false;
        for(int i = 0; i < r; i++){
            if(impossible) break;
            for(int j = 0; j < c; j++){
                if(picture[i][j] == '#' && i < r-1 && j < c-1){
                    char right = picture[i][j+1];
                    char bot = picture[i+1][j];
                    char diag = picture[i+1][j+1];
                    if(right == '#' && bot == '#' && diag == '#'){
                        picture[i][j] = '/';
                        picture[i][j+1] = '\\';
                        picture[i+1][j] = '\\';
                        picture[i+1][j+1] = '/';
                    }
                    else{
                        impossible = true;
                        break;
                    }
                }
                else if(picture[i][j] == '#'){
                    impossible = true;
                    break;
                }
            }
        }        

        cout << "Case #" << k+1 << ":" << endl;
        if(impossible) cout << "Impossible" << endl;
        else{
            for(int i = 0; i < r; i++){
                for(int j = 0; j < c; j++){
                    cout << picture[i][j];
                }
                cout << endl;
            }
        }
    }
}
