//
//  main.cpp
//  Candy Splitting
//
//  Created by Petro Boychuk on 07.05.11.
//  Copyright 2011 HelloWebApps. All rights reserved.
//

#include <iostream>
using namespace std;

void solve2() {
    int count;
    cin >> count;
    int c[1000];
    int xsum = 0;
    long long int sum = 0;
    int minc;
    for (int i=0; i<count; i++) {
        cin >> c[i];
        
        if (i == 0) {
            minc = c[i];
        } else {
            if (c[i] < minc) {
                minc = c[i];
            }
        }
        sum += c[i];
        xsum ^= c[i];
    }
    
    if (xsum != 0) {
        cout << "NO";
        return;
    }
    
    cout << (sum-minc);
}


int main (int argc, const char * argv[])
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    
    int tests;
    cin >> tests;
    for (int test=1; test <= tests; test++) {
        
        cout << "Case #" << test << ": ";
        solve2();
        cout << endl;
    }
    
    return 0;
}

