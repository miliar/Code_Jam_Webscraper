#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <sstream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int k = 1; k <= t; k++){
        int r,c;
        scanf("%d %d", &r, &c);
        char **pattern = new char*[r];
        for(int i = 0; i < r; i++){
            pattern[i] = new char[c];
        }
        for(int i = 0 ; i < r; i++){
            string s;
            cin >> s;
            for(int j = 0 ; j < c; j++){
                pattern[i][j] = s.at(j);
            }
        }
        bool result = true;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(pattern[i][j] == '#'){
                    if((i < r - 1) && (j < c - 1)){
                        if((pattern[i + 1][j] == '#') && (pattern[i][j + 1] == '#')
                            && (pattern[i + 1][j + 1])){
                            pattern[i][j] = '/';
                            pattern[i + 1][j + 1] = '/';
                            pattern[i + 1][j] = '\\';
                            pattern[i][j + 1] = '\\';
                        } else{
                            result = false; j = c +1;
                            i = r + 1;
                        }
                    }else{
                        result = false; j = c +1;
                        i = r + 1;
                    }
                }
            }
        }
    string out = "Case #";
    stringstream ss;
    ss << k;
    out += ss.str() + ":\n";
    if(result == false){
        out += "Impossible";
        cout << out << endl;
    }
    else{
        cout << out;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c;j++){
                cout << pattern[i][j];
            }
            cout << endl;
        }
    }
    for(int i = 0; i < r; i++){
        delete[] pattern[i];
    }
    delete[] pattern;

    }
    return 0;
}
