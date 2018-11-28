//
//  main.cpp
//  Googlerese
//
//  Created by Lyamani Moulay on 14/04/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define LINESZ 1024

map <string,string>  rules ;

/*string changeline(string str)
{
    string line = "" ;
    
    return line;
}*/

int main (int argc, const char * argv[])
{
    freopen("/Users/lyamanimoulay/Desktop/Googlerese/Googlerese/output.in","w", stdout);
    FILE* IN = freopen("/Users/lyamanimoulay/Desktop/Googlerese/Googlerese/input.txt","r", stdin);
    
    
    int test,cases;
    
    string in  = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z" ;
    
    string out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q" ;
    
    for(int s=0; s<in.length(); s++)
    {
        string sin = in.substr(s,1) ;
        string sout = out.substr(s,1) ;
        map<string,string>::iterator it = rules.find(sin) ;
        
        if( (sin !=" ") && (it == rules.end()) )
            rules[sin] = sout ;
    }
    
    char str[LINESZ] ;
    //char* buffer ;
    cases=0;
    scanf("%d",&test);
    fgets (str, LINESZ, IN) ;
    while (test){
        test--;
        cases++;
        fgets (str, LINESZ, IN) ;
        
        string line = (string)str;
        line = line.substr(0,line.size()-1);
        
        string newline = "";
        
        //long sizeOfNewLine = (line.length()<=100)? line.length() : 100 ;
        
        for(int s=0; s< line.length(); s++)
        {
            string sin = line.substr(s,1) ;
            if (sin ==" ")
               newline = newline + " " ;
            else
            {
                map<string,string>::iterator it = rules.find(sin) ;
                
                if( it != rules.end() ) 
                    newline = newline + it->second ; 
                else
                    break ;
            }
        }
        
        if(newline.length() != line.length() )
            break ;
        
        cout<<"Case #"<<cases<<": "<< newline <<endl;
        
       // if(cases==30)
         //   break;
    }
    return 0;
}

