//
//  main.cpp
//  codejam2013qual
//
//  Created by Petro Boychuk on 4/13/13.
//  Copyright (c) 2013 Petro Boychuk. All rights reserved.
//

#include <iostream>
using namespace std;

bool has_dots(string a[4]) {
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if(a[i][j] == '.') {
                return true;
            }
        }
    }
    return false;
}


bool won(char c, string a[4]) {
    //Lines
    bool found;
    for (int i=0; i<4; i++) {
        found = true;
        for(int j=0; j<4; j++) {
            if(a[i][j] != c && a[i][j] != 'T') {
                found = false;
                break;
            }
        }
        if(found){
            return true;
        }
    }
    
    for (int i=0; i<4; i++) {
        found = true;
        for(int j=0; j<4; j++) {
            if(a[j][i] != c && a[j][i] != 'T') {
                found = false;
                break;
            }
        }
        if(found){
            return true;
        }
    }
    
    found = true;
    for (int i=0; i<4; i++) {
        if(a[i][i] != c && a[i][i] != 'T') {
            found = false;
        }
    }
    if(found) {
        return true;
    }
    
    found = true;
    for (int i=0; i<4; i++) {
        if(a[i][3-i] != c && a[i][3-i] != 'T') {
            found = false;
        }
    }
    if(found) {
        return true;
    }
    
    return false;
    
}


void solve() {
    string a[4];
    for (int i=0; i<4; i++) {
        cin >> a[i];
    }
    
    if(won('X', a)) {
        cout << "X won";
    } else if(won('O', a)){
        cout << "O won";
    } else if(!has_dots(a)) {
        cout << "Draw";
    } else {
        cout << "Game has not completed";
    }
}


int main(int argc, const char * argv[])
{
    
    freopen("inputA.txt", "r", stdin);
    freopen("outputA.txt", "w", stdout);

    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
    
    
    return 0;
}

