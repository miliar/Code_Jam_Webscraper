//
//  QualA.cpp
//  
//
//  Created by Josh Deprez on 7/05/11.
//  Copyright 2011 Josh Deprez. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;

int sw(char c) {
    return c=='O' ? 0 : 1;
}

int main() {
    
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int N, time=0, pos[2]={1,1}, rtime[2]={0,0};
        cin >> N;
        while(N--) {
            char c;
            int b;
            cin >> c >> b;
            int l = abs(b-pos[sw(c)]);
            //cerr << "l " << l;
            int d = time-rtime[sw(c)];
            //cerr << "d " << d;
            time += (l < d ? 0 : l - d) + 1;
            rtime[sw(c)] = time;
            pos[sw(c)] = b;
        }
        
        cout << "Case #" << t << ": " << time << endl;
        
    }
    
    return 0;
}

