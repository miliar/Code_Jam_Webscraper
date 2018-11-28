//
//  main.cpp
//  numbers
//
//  Created by Leon Qiao on 14/4/12.
//  Copyright (c) 2012 qiaoliang89@gmail.com. All rights reserved.
//



#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std; 
int main(int argc, const char * argv[])
{
    
    int count,min,max, caseNum = 1;
    int origin, muted,option , toChange;
    int resultCount = 0;
    vector<int> container;
    
    string lastC , theRest , newStr;
    cin >> count ; 
    
    while(count --){
       
        
        
        cin >> min ;
        cin >> max ; 
        resultCount = 0;
        container.clear();
     //   cout << max - min<< "!!!"<< endl ;
        container.resize(max - min + 50);
        container.clear();
        for(int i = min ; i <= max ; i++ ){
            
            option = 1;
            origin = i;
            stringstream converter;
            converter << i;
            newStr = converter.str();
            
            
            for(int j = 0 ; j < newStr.length() ; j ++){
                istringstream ( newStr ) >> toChange;
                if(toChange - min >= 0 && toChange <= max)
                container[toChange - min] = 1;
                lastC = newStr.substr(newStr.size()-1, newStr.size());
                theRest = newStr.substr(0, newStr.size()-1);
                newStr = lastC + theRest;
               if(lastC == "0")
                   continue;
                //cout<<newStr << endl;
                muted = atoi(newStr.c_str()); 
                if (muted <= max && muted >= min && muted != origin && container[muted - min] != 1) {
                    option ++;
                    container[muted - min ] = 1; //  
                //    cout << "new!!!!!!!!!" << endl;
                } 
               
            }

            if( option >= 2)
            {
                resultCount += option * (option - 1) / 2;
            }
        }
        cout << "Case #"<<caseNum++<<": ";
        cout << resultCount;
        
        cout << '\n';
    }
}
