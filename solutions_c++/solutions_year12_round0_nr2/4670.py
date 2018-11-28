//
//  B.cpp
//  Google Codejam Qualification Round
//
//  Created by Seung Ho Jang on 12. 4. 15..
//  Copyright (c) 2012년 shjang1992@hotmail.com. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
    FILE* fp = fopen("/Users/FrozenGuy/XCode Projects/Google Codejam Qualification Round/Google Codejam Qualification Round/B-large.in","r");
    FILE* output = fopen("/Users/FrozenGuy/XCode Projects/Google Codejam Qualification Round/Google Codejam Qualification Round/output_large.txt","w");
    
    int lines = 0;
    fscanf(fp,"%d",&lines);
    
    vector<int> scores;
    int surprises = 0;
    int exceeders = 0;
    
    for(int cur_line = 1;cur_line<=lines;++cur_line)
    {
        //Init
        surprises = 0;
        exceeders = 0;
        scores.clear();
        
        int googlers,surprise,p;
        fscanf(fp,"%d %d %d",&googlers,&surprise,&p);
        
        for(int i=0;i<googlers;++i)
        {
            int temp_int;
            fscanf(fp,"%d",&temp_int);
            scores.push_back(temp_int);
        }
        
        sort(scores.begin(), scores.end());
        
        for(int i=0;i<scores.size();++i)
        {
            if(scores[i] >= 3*p)
            {
                ++exceeders;
                if(surprises >= surprise)
                    continue;

                ++surprises;

            }
            else if(scores[i] >= 3*p - 1 || scores[i] >= 3*p - 2)
            {
                ++exceeders;
            }
            else if(scores[i] >= 3*p - 4 && p != 1)
            {
                if(surprises >= surprise)
                    continue;
                
                 ++surprises;
                
                ++exceeders;
            }
            else if(p == 1)
            {
                if(surprises >= surprise)
                    continue;
                
                if(scores[i] != 0)
                    ++exceeders;
                
                if(scores[i] >= 2)
                    ++surprises;
            }
            
        }
        cout<<"Case #"<<cur_line<<": "<<exceeders<<endl;
        fprintf(output,"Case #%d: %d\n",cur_line,exceeders);
    }
    
    fclose(fp);
    fclose(output);
    
    return 0;
}