//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Dora on 13/04/13.
//  Copyright (c) 2013 Dora. All rights reserved.
//

#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <stdio.h>

using namespace std;

int main()
{

    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    
    int n = 0;
    cin>>n;
    string input_line, input_block, output;
    
    for (int i=0;i<n;i++)
	{
        //read each block
        for(int j=0;j<4;j++)
        {
            cin>>input_line;
            j==0?input_block=input_line:input_block+=input_line;
        }
        
        //analyse each block
        int isNotCompleted = 0;
        int isDraw = 0;
        int isWin = 0;
        string s;
        for(int j=0;j<input_block.length();j++)
        {            
            char a,b,c,d;
            s="";
            //if \\//
            
            if(j==0)
            {
                a=input_block[j];
                b=input_block[j+5];
                c=input_block[j+5*2];
                d=input_block[j+5*3];
                
                s="";
                s=s+a+b+c+d;
                
                if(s.find(".")==std::string::npos){
                    if ((s.find("X")==std::string::npos && s.find("O")!=std::string::npos)||
                        (s.find("O")==std::string::npos && s.find("X")!=std::string::npos)) {
                        isWin=1;
                        break;
                    }
                }
            }
        
            
            // if //
            if(j==3)
            {
                a=input_block[j];
                b=input_block[j+3];
                c=input_block[j+3*2];
                d=input_block[j+3*3];
                
                s="";
                s=s+a+b+c+d;
                
                if(s.find(".")==std::string::npos){
                    if ((s.find("X")==std::string::npos && s.find("O")!=std::string::npos)||
                        (s.find("O")==std::string::npos && s.find("X")!=std::string::npos)) {
                        isWin=1;
                        break;
                    }
                }
            }
            
            // if |
            if(j==0|j==1|j==2|j==3)
            {
                a=input_block[j];
                b=input_block[j+4];
                c=input_block[j+4*2];
                d=input_block[j+4*3];
                
                s="";
                s=s+a+b+c+d;
                
                if(s.find(".")==std::string::npos){
                    if ((s.find("X")==std::string::npos && s.find("O")!=std::string::npos)||
                        (s.find("O")==std::string::npos && s.find("X")!=std::string::npos)) {
                        isWin=1;
                        break;
                    }
                }
            }
            
            // if -
            if(j==0|j==4|j==8|j==12)
            {
                a=input_block[j];
                b=input_block[j+1];
                c=input_block[j+2];
                d=input_block[j+3];
                
                s="";
                s=s+a+b+c+d;
                
                if(s.find(".")==std::string::npos){
                    if ((s.find("X")==std::string::npos && s.find("O")!=std::string::npos)||
                        (s.find("O")==std::string::npos && s.find("X")!=std::string::npos)) {
                        isWin=1;
                        break;
                    }
                }
            }            
        }
        
        if(isWin==1)
        {
            if(s.find("X")!=std::string::npos) output="X won";
            else output = "O won";
        }
        else if(input_block.find(".")==std::string::npos)
        {
            isDraw=1;
            output="Draw";
        }
        else
        {
            isNotCompleted=1;
            output="Game has not completed";
        }
        cout<<"Case #"<<i+1<<": "<<output;
        if(i<n-1)cout<<endl;

	}
    
    return 0;
}

