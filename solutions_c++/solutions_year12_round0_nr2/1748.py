//
//  main.cpp
//  dance
//
//  Created by Leon Qiao on 14/4/12.
//  Copyright (c) 2012 qiaoliang89@gmail.com. All rights reserved.
//

#include <iostream>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std; 
int main(int argc, const char * argv[])
{
    
    int count,caseNum = 1 ,numOfValue, numOfSurprise , minimum , countMinimum = 0,instanceOfValue;
    int temp,tempSur;
    vector<int> value;
    cin >> count ; 
    
    while(count --){
        cout << "Case #"<<caseNum++<<": ";
       
        
        cin >> numOfValue ;
        cin >> numOfSurprise ; 
        cin >> minimum;
        while (numOfValue --){
            cin >> instanceOfValue;
            value.push_back(instanceOfValue);
        }
        sort (value.begin(), value.end());
        reverse (value.begin(), value.end());
        
        
        // ... (populate the vector)
        
        for (vector<int>::iterator i = value.begin();
             i != value.end();
             ++i)
        {
            if(*i == 0 && minimum == 0)
            {
                countMinimum++;
                continue;
            }
            else if(*i == 0)
            {
                continue;
            }
            switch (*i%3) {
                case 0:
                    temp = *i/3 ;
                    break;
                case 1:
                    temp = *i/3 + 1;
                    break;
                case 2:
                    temp = *i/3 + 1;
                    break;
                    
                default:
                    break;
            }
            if(temp >= minimum)
                countMinimum ++;
            else{
                if(numOfSurprise > 0){
                    switch (*i%3) {
                        case 0:
                            tempSur = *i/3 + 1;
                            break;
                        case 1:
                            tempSur = (*i+2)/3;
                            break;
                        case 2:
                            tempSur = (4+*i)/3;
                            break;
                            
                        default:
                            break;
                    }
                    if(tempSur >= minimum){
                        countMinimum++;
                        numOfSurprise --;
                    }
                    else break;
                } else {
                    break;
                }
            }
        }
        
        
        cout << countMinimum;
         cout << '\n';
        value.clear();
        countMinimum = 0;
    }
}
