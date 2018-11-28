//
//  main.cpp
//  google code jam
//
//  Created by Guillaume Derval on 14/04/12.
//  Copyright (c) 2012 ITSelf.be. All rights reserved.
//

#include <iostream>
#include <fstream>

int nbdigits(int nb, int & offset)
{
    int i = 1;
    int totest = 10;
    while(true)
    {
        if(nb % totest == nb)
        {
            offset = totest/10;
            return i;
        }
        totest *= 10;
        i++;
    }
    return 0;
}

int left(int nb, int offset)
{
    int temp = nb % 10;
    nb = nb/10;
    nb = nb - (nb - (nb%offset)) + temp*offset;
    return nb;
}

int main (int argc, const char * argv[])
{
    std::ifstream fin ("/Users/guillaumederval/Desktop/in.in", std::ifstream::in);
    std::ofstream fout("/Users/guillaumederval/Desktop/out.out", std::ofstream::out | std::ofstream::trunc);
    
    bool *testbool = new bool[2000001];
    
    int ccount  = 0;
    fin >> ccount;
    for(int c = 0; c < ccount; c++)
    {
        int scount = 0;
        int from, to, digits, offset = 0;
        fin >> from >> to;
        digits = nbdigits(from, offset);
        for(int i = offset; i < std::min(10*offset, 2000001); i++)
        {
            testbool[i] = false;
        }
        for(int i = from; i <= to; i++)
        {
            if(testbool[i])
                continue;
            int test = i;
            testbool[test] = true;
            int sub = 0;
            for(int j = 0; j < digits; j++)
            {
                test = left(test, offset);
                if(test >= from && test <= to && test != i && test % offset != 0 && !testbool[test])
                {
                    //if(sub == 0)
                    //    std::cout << i << std::endl;
                    scount += (++sub);
                    testbool[test] = true;
                    //if(c == 3)
                    //    std::cout << test << std::endl;
                }
            }
        }
        fout << "Case #" << (c+1) << ": " << scount << std::endl;
    }
}