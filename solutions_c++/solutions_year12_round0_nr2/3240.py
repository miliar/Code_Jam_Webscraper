//
//  main.cpp
//  Contest
//
//  Created by User on 25.03.12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int n, p, S;
int sum[111];
int res[111];
int nres[111];

int solve() {
    memset(res, 0, sizeof(res));
    for (int i = 0; i < n; ++i) {
        memset(nres, 0, sizeof(nres));
        for (int s = 0; s <= S; ++s) {
            for (int x = 0; x < 3; ++x) {
                for (int y = x; y < 3; ++y) {
                    for (int z = y; z < 3; ++z) {
                        int X = sum[i] - x - y - z;
                        if (X >= 0 && X % 3 == 0) {
                            X /= 3;
                            if (X + z <= 10 && s + (int)(z == 2) <= S) {
                                nres[s + (int)(z == 2)] = max(nres[s + (int)(z == 2)],
                                                              res[s] + (int)(X + z >= p));
                            }
                        }
                    }
                }
            }
        }
        memcpy(res, nres, sizeof(res));
    }
    return res[S];
}

int main (int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int t = 0; t < T; ++t) {
        cin >> n >> S >> p;
        for (int i = 0; i < n; ++i)
            cin >> sum[i];
        cout << "Case #" << t + 1 << ": " << solve() << endl;
    }
    
    
       
    return 0;
}

