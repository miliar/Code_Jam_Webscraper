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
    
    int n, local, locmax, s, count, p;
    
    fin>>count;
    
    for (int i = 0; i<count;i++) 
    {
        locmax = 0;
        
        fin>>n>>s>>p;
        for (int j = 0; j<n;j++) 
        {
            fin>>local;
            if ((local+2)/3 >= p) 
            {
                locmax++;
            }
            else 
            {
                if (s>0 && ((local+4)/3 >= p && local >=2)) 
                {
                    s--;
                    locmax++;
                }
            }
        }
        
        fout<<"Case #"<<i+1<<": "<<locmax<<endl;
        
    }
    fin.close();
    fout.close();
    return 0;
}

