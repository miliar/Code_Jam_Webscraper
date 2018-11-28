//
//  main.cpp
//  Candy Splitting
//
//  Created by Petro Boychuk on 07.05.11.
//  Copyright 2011 HelloWebApps. All rights reserved.
//

#include <iostream>
using namespace std;

void solve() {
    int n;
    cin >> n;
    
    string s[100];
    for (int i=0; i<n; i++) {
        cin >> s[i];
    }
    
    long double wp[100], owp[100], oowp[100];
    int cwp[100], cowp[100], coowp[100];
    
    for (int i=0; i<n; i++) {
        int win = 0;
        wp[i] = 0;
        cwp[i] = 0;
        for (int j=0; j<n; j++) {
            if(s[i][j] == '1') {
                wp[i] += 1;
                win++;
            } else if(s[i][j] == '0') {
                win++;
            }
        }
        cwp[i] = win;
        wp[i] /= win;
    }
    
    for (int i=0; i<n; i++) {
        int count = 0;
        owp[i] = 0;
        for (int j=0; j<n; j++) {
            if(s[i][j] != '.') {
                long double t = wp[j];
                if(s[i][j] == '1') {
                    t *= cwp[j];
                    t /= cwp[j] - 1;
                } else {
                    t *= cwp[j];
                    t -= 1;
                    t /= cwp[j] - 1;
                }
                owp[i] += t;
                count++;
            }
        }
        owp[i] /= (double)count;
    }
    
    for (int i=0; i<n; i++) {
        int count = 0;
        oowp[i] = 0;
        for (int j=0; j<n; j++) {
            if(s[i][j] != '.') {
                oowp[i] += owp[j];
                count++;
            }
        }
        oowp[i] /= (double)count;
    }
    
    for (int i=0; i<n; i++) {
        cout.precision(10);
        cout.setf(ios::fixed);
        cout << endl << (wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
    }
    
}


int main (int argc, const char * argv[])
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int tests;
    cin >> tests;
    for (int test=1; test <= tests; test++) {
        
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }
    
    return 0;
}

