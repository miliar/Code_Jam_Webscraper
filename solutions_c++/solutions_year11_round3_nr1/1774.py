/* 
 * File:   main.cpp
 * Author: Sagar
 *
 * Created on May 22, 2011, 5:58 PM
 */

#include <cstdlib>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int T, R, C;
    cin >> T;
    for(int index=1;index<=T;index++){
        cin >>R >> C;
        char tile[R][C];
        for(int i = 0; i<R;i++)
            for(int j=0;j<C;j++)
                cin >> tile[i][j];

        for(int i=0;i<R-1;i++)
            for(int j=0;j<C-1;j++)
                if(tile[i][j] == '#' && tile[i+1][j] == '#' && tile[i][j+1] == '#' && tile[i+1][j+1] == '#') {
                    tile[i][j] = '/';
                    tile[i+1][j] = '\\';
                    tile[i][j+1] = '\\';
                    tile[i+1][j+1] = '/';
                }
        bool found = false;
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
                if(tile[i][j] == '#'){
                    found = true;
                    break;
                }
        cout << "Case #" << index << ":\n";
        if(found)
            cout << "Impossible\n";
        else
            for(int i=0;i<R;i++){
                for(int j=0;j<C;j++)
                    cout << tile[i][j];
                cout << "\n";
            }
                    

    }
    return 0;
}

