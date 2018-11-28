//
//  main.cpp
//  codejam
//
//  Created by Victor Schepanovsky on 14.04.12.
//  Copyright (c) 2012 Kuadriga. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main(int argc, const char * argv[])
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    
  /*  string str1, str2;
    
    cin>> str1;
    cin>> str2;
    
    char chars[29];
    
    for (int i = 0; i<= 'z'-'a'; i++) 
    {
        int pos = str1.find('a'+i);
        chars[i] = str2[pos];
        cout <<(char)('a'+i)<<"'"<<chars[i]<<"'"<<endl;
    }*/
    
    char chars[] = {'y',
        'h',
        'e',
        's',
        'o',
        'c',
        'v',
        'x',
        'd',
        'u',
        'i',
        'g',
        'l',
        'b',
        'k',
        'r',
        'z',
        't',
        'n',
        'w',
        'j',
        'p',
        'f',
        'm',
        'a',
        'q'};
    
    int n;
    fin>>n;
    char c;
    //fout<<"Case #"<<1<<": ";

    for (int i = 0; i<=n && !fin.eof();) 
    {
        fin.get(c);
        if (c == '\n') 
        {
            i++;
            if (i!=n+1) 
            {
                if (i>1) 
                {
                    fout<<endl;
                }
                
                fout<<"Case #"<<i<<": ";
            }
        }
        else 
        {
            if (c == ' ') 
            {
                fout<<" ";
            }
            else 
            {
                fout<<chars[c-'a'];                
            }
        }
        
    }

    return 0;
}

