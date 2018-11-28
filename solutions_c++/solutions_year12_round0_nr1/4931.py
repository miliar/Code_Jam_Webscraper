/*
 *  quick.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 07/02/15.
 *  Copyright 2007 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
//#include <cmath>
using namespace std;

#include <vector>
#include <string>

int main()
{
	int T;
	
	cin>>T;
	
    vector<char> mapping(26);
    mapping[0]='y';
    mapping[1]='h';
    mapping[2]='e';
    mapping[3]='s';
    mapping[4]='o';
    mapping[5]='c';
    mapping[6]='v';
    mapping[7]='x';
    mapping[8]='d';
    mapping[9]='u';
    mapping[10]='i';
    mapping[11]='g';
    mapping[12]='l';
    mapping[13]='b';
    mapping[14]='k';
    mapping[15]='r';
    mapping[16]='z';
    mapping[17]='t';
    mapping[18]='n';
    mapping[19]='w';
    mapping[20]='j';
    mapping[21]='p';
    mapping[22]='f';
    mapping[23]='m';
    mapping[24]='a';
    mapping[25]='q';
    
    string cypher, english;

    for(int i=0; i<T; ++i)
    {
        //cin>>cypher;
        
        do getline(cin, cypher); while (cypher.length() == 0);
        
        english = cypher;
        
        for(int j=0; j<english.length(); ++j)
            if(english[j] != ' ')
            {
                english[j] = mapping[cypher[j] - 'a'];
            }
            
        cout<<"Case #"<<i+1<<": "<<english<<endl;
    
    }
    
	return 0;
}
