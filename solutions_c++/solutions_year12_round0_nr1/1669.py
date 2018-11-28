//
//  main.cpp
//  tranlater
//
//  Created by Leon Qiao on 14/4/12.
//  Copyright (c) 2012 qiaoliang89@gmail.com. All rights reserved.
//

#include <iostream>
#include <stdio.h>
int main(int argc, const char * argv[])
{

    // insert code here...
    std::string key = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
 std::string result = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    int count,caseNum = 1 ;
    std::cin >> count ; 
    
    std::string temp;
     getline(std::cin, temp);
    while(count --){
        getline(std::cin, temp);
        std::cout << "Case #"<<caseNum++<<": ";
        for(int i = 0 ; i < temp.size()+1; i ++)
        {
            
            for(int j = 0 ; j < key.size() ; j ++)
            {
                if(temp[i] == 'z'){
                    std::cout << 'q';
                    break;
                } else if (temp[i] == 'q'){
                    std::cout << 'z';
                    break;
                }
                   
                if(temp[i] == key[j])
                    {
                        std::cout << result[j];
                        break;
                    }
            }
        }
        std::cout << '\n';
    }
}

