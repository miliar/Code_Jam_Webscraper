//
//  R1CA.cpp
//  
//
//  Created by Josh Deprez on 21/05/11.
//  Copyright 2011 Josh Deprez. All rights reserved.
//


#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
    
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        
        bool p = true;
        
        vector<string> pic;
        string z;
        int R,C;
        cin >> R >> C;
        while (R--) {
            cin >> z;
            pic.push_back(z);
        }

        R=pic.size();
        for (int r=0; r<R && p; ++r) {
            for (int c=0; c<C && p; c++) {
                if (pic[r][c] == '#') {
                    if (r<R-1 && c<C-1 && pic[r+1][c]=='#' && pic[r][c+1]=='#' && pic[r+1][c+1]=='#') {
                        pic[r][c] = pic[r+1][c+1] = '/';
                        pic[r+1][c] = pic[r][c+1] = '\\';
                    }
                    else
                    {
                        p = false;
                    }
                }
            }
        }
        
        
        cout << "Case #" << t << ":" << endl;
        if (p) {
            for (int r=0; r<R; ++r) {
                cout << pic[r] << endl;
            }
        } else {
            cout << "Impossible" << endl;
        }
    }
    
    return 0;
}