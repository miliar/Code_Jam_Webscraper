//
//  main.cpp
//  GoroSort
//
//  Created by Petro Boychuk on 07.05.11.
//  Copyright 2011 HelloWebApps. All rights reserved.
//

#include <iostream>
using namespace std;

int solve() {
    int curBluePos = 1;
    int curOrangePos = 1;
    int res = 0;
    
    
    int countMoves;
    cin >> countMoves;
    
    int lastMoveTime = 0;
    bool lastMoveWasO = true;
    
    for (int i=0; i<countMoves; i++) {
        char player;
        int position;
        
        
        
        cin >> player >> position;
        
        if (i==0) {
            if (player == 'O') {
                lastMoveWasO = true;
            } else {
                lastMoveWasO = false;
            }
        }

        
        if (player == 'O') {
            int moveTime = abs(position - curOrangePos);
            if (lastMoveWasO) {
                res += moveTime + 1; // Move and press
                lastMoveTime += moveTime+1;
            } else {
                if (moveTime < lastMoveTime) {
                    res += 1;
                    lastMoveTime = 1;
                } else {
                    res += moveTime - lastMoveTime + 1;
                    lastMoveTime = moveTime - lastMoveTime + 1;
                }
            }
            curOrangePos = position;
            lastMoveWasO = true;
        } else {
            int moveTime = abs(position - curBluePos);
            if (!lastMoveWasO) {
                res += moveTime + 1; // Move and press
                lastMoveTime += moveTime+1  ;
            } else {
                if (moveTime < lastMoveTime) {
                    res += 1;
                    lastMoveTime = 1;
                } else {
                    res += moveTime - lastMoveTime + 1;
                    lastMoveTime = moveTime - lastMoveTime + 1;
                }
            }
            curBluePos = position;
            lastMoveWasO = false;
        }
    }
    return res;
}

int main (int argc, const char * argv[])
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int tests;
    cin >> tests;
    for (int test=1; test <= tests; test++) {
        int result = solve();
        cout << "Case #" << test << ": "<< result << endl;
    }
    return 0;
}

