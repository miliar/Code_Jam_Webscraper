//
//  QualB.cpp
//  
//
//  Created by Josh Deprez on 7/05/11.
//  Copyright 2011 Josh Deprez. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {

        map<pair<char,char>,char> comb;
        set<pair<char,char> > opp;
        
        int C, D;
        string z;
        cin >> C;
        while(C--) {
            cin >> z;
            comb[make_pair(z[0],z[1])]=comb[make_pair(z[1],z[0])]=z[2];
        }
        cin >> D;
        while (D--) {
            cin >> z;
            opp.insert(make_pair(z[0],z[1]));
            opp.insert(make_pair(z[1],z[0]));
        }
        cin >> C;
        cin >> z;
        vector<char> y;
        for(int i=0; i<z.length(); ++i) {
             
            map<pair<char,char>,char>::iterator j = comb.end();
            if (y.size() > 0) j = comb.find(make_pair(*y.rbegin(),z[i]));
            if (j != comb.end()) {
                y.pop_back();
                y.push_back(j->second);
            } else {
                y.push_back(z[i]);
                for (int k=0; k<y.size(); ++k) {
                    if (opp.count(make_pair(y[k],z[i]))) {
                        y.clear();
                        break;
                    }
                }
            }
        }
        
        cout << "Case #" << t << ": [";
        for (int i=0; i<y.size(); ++i) {
            if (i>0) cout << ", ";
            cout << y[i];
        }
        cout << "]" << endl;
        
    }
    
    return 0;
}

