//
//  QualC.cpp
//  
//
//  Created by Josh Deprez on 7/05/11.
//  Copyright 2011 Josh Deprez. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int N;
        cin >> N;
        int n, mn=1000000000, sum=0, osum=0;
        while(N--) {
            cin >> n;
            mn = min(n,mn);
            sum += n;
            osum ^= n;
        }
        
        
        
        cout << "Case #" << t << ": "; 
        
        if (osum == 0) {
            cout << sum - mn;
            
        } else {
            cout << "NO";
        }
        
        cout << endl;
        
    }
    
    return 0;
}

