//
//  main.cpp
//  Q4
//
//  Created by Chih-Hung Lin on 5/7/11.
//  Copyright 2011 Carnegie Mellon University. All rights reserved.
//

#include <iostream>
using namespace std;

int main (int argc, const char * argv[])
{
    int tests;
    int candys;
    int min;
    int xor_result;
    int sum;
    freopen("C-large.in", "rt", stdin);
    
    cin >> tests;
    for (int i=1; i<= tests; i++)
    {
        cin >> candys;
        cin >> xor_result;
        min = xor_result;
        sum = xor_result;
        
        for (int j = 1 + 1; j <= candys; j++) {
            int next;
            cin >> next;
            sum += next;
            xor_result = xor_result ^ next;
            if (next < min)
                min = next;
        }
        
        if (xor_result == 0)
            cout << "Case #" << i << ": " << sum - min << endl;
        else
            
            cout << "Case #" << i << ": NO" << endl; 
    
    }
    
    return 0;
}

