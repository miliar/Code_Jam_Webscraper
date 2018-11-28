//
//  main.cpp
//  codejam-lang
//
//  Created by Rajat Kumar on 4/13/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

char codebase[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

string translatelang(string inp, int casectr)
{
    string temp="";
    for (int i=0; i<inp.length(); i++) {
       if(inp[i]==' ')
           temp+=" ";
        
        else
        {
            
            int theChar = inp[i]-96-1;
            char encodedCh = codebase[theChar];
            //cout<<"flag "<<<<endl;
            temp+=encodedCh;
        }
    }
    return temp;
}

int main (int argc, const char * argv[])
{
    

    char a='1',b;
    string line;
    int n=100;
   // cin>>n;
    
    int casectr=1;
    //getline(cin,line);
    
    
    
    ifstream infile;
    string lineIn;
    infile.open("/Users/rajat/codejam/A-small-attempt0.in.txt");
    ofstream outfile;
    string lineOut;
    outfile.open("/Users/rajat/codejam/fileout-gcj1.txt");
    if (infile.is_open()){
        cout<<"**************************"<<"\n";
        while(infile.good())
        {
            getline(infile, lineIn);
            lineOut = lineIn;
            
            string lineOut = translatelang(lineIn, casectr);
            //cout<<out<<endl;
            cout<<"Case #"<<casectr<<": "<<lineOut<<endl;
            
            outfile<<"Case #"<<casectr<<": "<<lineOut<<"\n";
            casectr++;
        }
    }
    else
        cout<<"*************"<<"\n"<<"file open failed.\n";
    
    infile.close();
    outfile.close();
    cout<<"**************************\nfinished run"<<endl;
    
    
    
    
    
    /***
    while(n--)
    {
       // cout<<endl;
        
        getline(cin,line);
        
        string out = translatelang(line, casectr);
        //cout<<out<<endl;
        cout<<"Case #"<<casectr++<<": "<<out<<endl;
        
    }
        
    
    **/
    return 0;
}

