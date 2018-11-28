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

long long used[3000000];
long long z;

int solve(int A, int B) {
    int ret = 0;
    int d = 1;
    int h = 10;
    for (int x = 1; x < B; ++x) {
        if (x == h) {
            ++d;
            h *= 10;
        }
        if (x >= A) {
            ++z;
            int curx = x;
            for (int i = 1; i <= d; ++i) {
                curx = (curx % 10) * (h / 10) + curx / 10;
                if (curx > x && curx <= B) {
                    ret += (int)(used[curx] != z);
                }
                if (curx <= B)
                    used[curx] = z;
            }
        }
    }
    return ret;
}

int main (int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int t = 0; t < T; ++t) {
        int A, B;
        cin >> A >> B;
        
        cout << "Case #" << t + 1 << ": " << solve(A, B) << endl;
    }
    
    
       
    return 0;
}

