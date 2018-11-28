/*
 *  rotate.h
 *  
 *
 *  Created by taras on 22.05.10.
 *  Copyright 2010 Georgia Tech. All rights reserved.
 *
 */

#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

void show (vector<string> b) {
    cout << "----\n";
    for (int i = 0; i < b.size(); ++i) {
        cout << b[i] << endl;
    }
    cout << "----\n";
}

int test_me (vector<string> b, int k) {
    int n= b.size();
    int i, j, c;
    bool winB, winR;
    winB = winR = false;
    
    for (i = 0; i < n; ++i) {
        c = 0;
        for (j = 0; j < n; ++j) {
            if (b[i][j] == 'B') {
                if (c < 0)
                    c = 0;
                c++;
            } else if (b[i][j] == 'R') {
                if (c > 0)
                    c = 0;
                c--;
            } else {
                c = 0;
            }
            if (c == k)
                winB = true;
            if (c == -k)
                winR = true;
        }
    }
    
    for (i = 0; i < n; ++i) {
        c = 0;
        for (j = 0; j < n; ++j) {
            if (b[j][i] == 'B') {
                if (c < 0)
                    c = 0;
                c++;
            } else if (b[j][i] == 'R') {
                if (c > 0)
                    c = 0;
                c--;
            } else {
                c = 0;
            }
            if (c == k)
                winB = true;
            if (c == -k)
                winR = true;
        }
    }
    
    for (i = 0; i < n; ++i) {
        c = 0;
        for (j = 0; j < n && i+j < n; ++j) {
            if (b[i+j][j] == 'B') {
                if (c < 0)
                    c = 0;
                c++;
            } else if (b[i+j][j] == 'R') {
                if (c > 0)
                    c = 0;
                c--;
            } else {
                c = 0;
            }
            if (c == k)
                winB = true;
            if (c == -k)
                winR = true;
        }
    }
    
    for (i = 0; i < n; ++i) {
        c = 0;
        for (j = 0; j < n && i-j >= 0 && i+j < n; ++j) {
            if (b[i+j][i-j] == 'B') {
                if (c < 0)
                    c = 0;
                c++;
            } else if (b[i+j][i-j] == 'R') {
                if (c > 0)
                    c = 0;
                c--;
            } else {
                c = 0;
            }
            if (c == k)
                winB = true;
            if (c == -k)
                winR = true;
        }
    }
    
    if (winB && winR)
        return 10;
    if (winB)
        return -1;
    if (winR)
        return 1;
    return 0;
}

int main () {
    int tests;
    int k, n, i, j;
    
    vector<string> board, rotated;
    
    scanf("%d", &tests);
    for (int test = 0; test < tests; ++test) {
        scanf("%d %d", &n, &k);
        board.resize(n, "");
        for (i = 0; i < n; ++i)
            cin >> board[i];
        rotated.clear();
        rotated.resize(n, string(n, '.'));
        
        //for each row of board
        for (i = 0; i < n; ++i) {
            int k = 0;
            for (j = n-1; j >= 0; j--) {
                if (board[i][j] != '.') {
                    rotated[n-k-1][n-i-1] = board[i][j];
                    k ++;
                }
            }
        }
        
//        show(board);
//        show(rotated);
        
        int ans = test_me(rotated, k);
        string res;
        if (ans == 10)
            res = "Both";
        else if (ans == 1)
            res = "Red";
        else if (ans == -1)
            res = "Blue";
        else 
            res = "Neither";
        
        printf("Case #%d: ", test+1);
        cout << res << endl;
    }
};

