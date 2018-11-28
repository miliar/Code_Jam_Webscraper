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
    
    int count = 0;
    fin >> count;
    for(int O = 0; O < count; O++)
    {
        //std::cout << "Case " << (i+1) << std::endl;
        int N,S,P;
        int ok = 0;
        fin >> N >> S >> P;
        int nonsurprising = (P*3)-2;
        int surprising = (P*3)-4;
        if(surprising > 28 || surprising < 2)
        {
            surprising = nonsurprising;
        }
        //std::cout << "NS " << nonsurprising << " S " << surprising << std::endl;
        for(int j = 0; j < N; j++)
        {
            int score;
            fin >> score;
            if(score >= nonsurprising)
                ok++;
            else if(score >= surprising && S > 0)
            {
                ok++;
                S--;
            }
        }
        fout << "Case #" << (O+1) << ": " << ok << std::endl;
        //std::cout << "----" << std::endl;
    }
    std::cout << "STOP" << std::endl;
}