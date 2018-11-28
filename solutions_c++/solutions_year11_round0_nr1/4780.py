//
//  main.cpp
//  CodeJam
//
//  Created by Cong Vo on 5/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;




int main (int argc, const char * argv[]) {

    
//	freopen("..\\A-small-attempt0.in","r",stdin);freopen("..\\A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
    
    //	freopen("..\\A-small-attempt1.in","r",stdin);freopen("..\\A-small-attempt1.out","w",stdout);
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
        
	int testcase;

    cin >> testcase;
//    cout << testcase;
    
    for (int i = 0; i < testcase; i++) {
        int pn[2];
        pn [0] = pn [1] = 0;

        int pa[2];
        pa [0] = pa [1] = 0;
        
        int t = 0;
        
        int lp[2];
        lp [0] = lp [1] = 0;
        
        int c[2];
        c[0] = c[1] = 1;

        int step;
        cin >> step;
//        cout << step << "\n";        
        
        for (int j = 0; j < step; j++) {
            char b;
            int p;
            cin >> b >> p;
//            cout << b << " " << p << " ";
            
            int bi = 0;

            // O -> 79 -> 0
            // B -> 66 -> 1
            if (b == 66) bi = 1;
            
            pn[bi] = abs(p - c[bi]);
            
            pa[bi] = lp[1 - bi];
            
            lp[1-bi] = 0;
            
            int pt = max(pn[bi] - pa[bi], 0) + 1;
            
            lp[bi] += pt;
            
            t += pt;
            
            c[bi] = p; 
//            cout << t << "\n";
            
            
        }
        cout << "Case #" << i + 1 << ": " << t << "\n";        
    }
    
    return 0;
}

