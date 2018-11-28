//
//  main.cpp
//  google code jam
//
//  Created by Guillaume Derval on 14/04/12.
//  Copyright (c) 2012 ITSelf.be. All rights reserved.
//

#include <iostream>
#include <fstream>

int main (int argc, const char * argv[])
{
    std::ifstream fin ("/Users/guillaumederval/Desktop/in.in", std::ifstream::in);
    std::ofstream fout("/Users/guillaumederval/Desktop/out.out", std::ofstream::out | std::ofstream::trunc);
    
    char corres[26] = 
    {
        'y', //a
        'h', //b
        'e', //c
        's', //d
        'o', //e
        'c', //f
        'v', //g
        'x', //h
        'd', //i
        'u', //j
        'i', //k
        'g', //l
        'l', //m 
        'b', //n
        'k', //o
        'r', //p
        'z', //q
        't', //r
        'n', //s
        'w', //t
        'j', //u
        'p', //v
        'f', //w
        'm', //x
        'a', //y
        'q', //z
    };
    
    int count = 0;
    fin >> count;
    
    std::string *in = new std::string[count];
    std::getline(fin, in[0]);
    for(int i = 0; i < count; i++)
        std::getline(fin, in[i]);
    
    for(int i = 0; i < count; i++)
    {
        for(int j = 0; j < in[i].size(); j++)
        {
            if(in[i][j] == ' ')
                continue;
            
            in[i][j] = corres[((int)in[i][j])-((int)'a')];
        }
        
        fout << "Case #" << (i+1) << ": " << in[i] << std::endl;
    }
    //std::cout << "STOP" << std::endl;
}