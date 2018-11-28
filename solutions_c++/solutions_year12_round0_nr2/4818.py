/*
 *  quick.cpp
 *  
 *
 *  Created by Chuan-Chih Chou on 07/02/15.
 *  Copyright 2007 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>
#include <algorithm>

using namespace std;

#include <vector>
//#include <string>

int main()
{
	int T;
	
	cin>>T;
	
    for(int i=0; i<T; ++i)
    {
        int N, S, p;
        
        cin>>N>>S>>p;
        
        int non_surprising_requirement = p + 2*max(0, p-1);
        int surprising_requirement = p + 2*max(0, p-2);
        
        //vector<int> scores(N);
        
        int total = 0;
        int surprising_total = 0;
        
        for(int j=0; j<N; ++j)
        {        
            int score;
            cin>>score;
            
            if(score >= non_surprising_requirement)
                ++total;
            else if(score >= surprising_requirement)
                ++surprising_total;
        }    
        /*
        
        With best score p,
        non-surprising total score >= p + 2(p-1) = 3p - 2
        surprising total score >= p + 2(p-2) = 3p - 4
        
        UNLESS p-1<0.
        */
            
        cout<<"Case #"<<i+1<<": "<< total + min(S, surprising_total) <<endl;
    
    }
    
	return 0;
}
