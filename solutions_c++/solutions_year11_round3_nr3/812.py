//
//  R1CC.cpp
//  
//
//  Created by Josh Deprez on 21/05/11.
//  Copyright 2011 Josh Deprez. All rights reserved.
//


#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
    
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        
        
        ll N, L, H;
        cin >> N >> L >> H;

        vector<ll> freq;
        while (N--) {
            ll f;
            cin >> f;
            freq.push_back(f);
        }
        cout << "Case #" << t << ": ";
        ll i;
        for (i=L; i<=H; ++i) {
            int j,e;
            for (j=0,e=freq.size(); j<e; ++j) {
                if (!(i%freq[j]==0 || freq[j]%i==0)) {
                    break;
                }
            }
            if (j==e) {
                cout << i << endl;
                break;
            } 
        }
        if (i>H) cout << "NO" << endl;
        

    }
    
    return 0;
}