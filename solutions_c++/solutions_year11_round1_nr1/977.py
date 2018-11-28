//
//  R1AA.cpp
//  
//
//  Created by Josh Deprez on 21/05/11.
//  Copyright 2011 Josh Deprez. All rights reserved.
//


#include <iostream>

using namespace std;

typedef long long ll;

ll gcd(ll p, ll q) {
	ll t;
	while (q!=0) {
		t=p;
		p=q;
	    if (q > p) {
			q=t;
		} else {
			q=t%q;
		}
	}
	return p;
}


int main() {
    
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        
        bool p = true;
        
        ll N, PD, PG;
        cin >> N >> PD >> PG;
        if ((PG == 0 && PD > 0)|| (PG == 100 && PD < 100)) p = false;
        else {
            ll D = 100 / gcd(100, PD);
            
            if (D > N) p = false;
            
        }
        cout << "Case #" << t << ": " << (p ? "Possible" : "Broken") << endl;
    }
    
    return 0;
}