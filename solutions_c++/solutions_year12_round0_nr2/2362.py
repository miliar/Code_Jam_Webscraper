//
//  main.c
//  codejam2012
//
//  Created by Петро Бойчук on 4/14/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std;

bool normal(int score, int p) {
    if(((p-1) >= 0 && (score - p*3 + 2) >= 0) || p == 0){
        return true;
    }
    return false;
}

bool surprise(int score, int p) {
    if(((p-2) >= 0 && (score - p*3 + 4) >= 0)){
        return true;
    }
    return false;
}

void solve() {
    int n;
    cin >> n;
    
    int s;
    cin >> s;
    
    int p;
    cin >> p;
    int result = 0;
    for (int i=0; i<n; i++) {
        int t;
        cin >> t;
        if( normal(t, p)) {
            result++;
        } else if(surprise(t, p) && s > 0) {
            s--;
            result++;
        }
    }
    
    cout << result;
}

int main(int argc, const char * argv[])
{
    
//    ifstream in("A-small-attempt1.in");
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    
    int t;
    cin >> t;
    
    for (int test = 1; test <= t; test++) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;

    }
    
    
        
    
    
    return 0;
}

