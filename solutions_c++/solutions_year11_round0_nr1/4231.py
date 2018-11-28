//
//  main.cpp
//  Q1
//
//  Created by Chih-Hung Lin on 5/7/11.
//  Copyright 2011 Carnegie Mellon University. All rights reserved.
//

#include <iostream>
using namespace std;

int main (int argc, const char * argv[])
{
    int sets;
    int buttons;
    char button;
    int num, num_O, num_B;
    int previous_B, previous_O, total_B, total_O;
    char pre_button;
    
    
    cin >> sets;
    for (int i= 1; i <= sets; i++) {
        cin >> buttons;
        
        total_B = 0;
        total_O = 0;
        previous_B = 1;
        previous_O = 1;
        num_B = 0;
        num_O = 0;
        pre_button = ' ';
        
        for (int j =buttons; j >0; j--) {
            cin >> button >> num;
            if (button == 'O'){
                
                    
                total_O += abs(num - previous_O);
                if (pre_button == 'B')
//                    if (total_O < total_B)
//                        total_B ++;
                    total_O = max(total_B, total_O);
                //num_O ++;
                total_O ++;
                previous_O = num;
                pre_button = 'O';
            }
            else if (button == 'B'){
                total_B += abs(num - previous_B);
                if (pre_button == 'O'){
//                    if (total_B < total_O)
//                        total_O ++;
                    total_B = max(total_B, total_O);
                    
                }
                //num_B ++;
                total_B ++;
                previous_B = num;
                pre_button = 'B';
            }
        }
        
        cout << "Case #" << i << ": " << max(total_B, total_O)<< endl;
    }
    // insert code here...
    return 0;
}

