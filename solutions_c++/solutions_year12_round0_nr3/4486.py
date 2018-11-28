//
//  numbers.cpp
//  
//
//  Created by Božidar Ševo on 14.4.2012..
//  Copyright (c) 2012. Seodoa. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int number_of_pairs(int x, int y);

int number_of_pairs(int x, int y)
{
    int x_i,y_i;
    int x_l,y_l;
    int i,j,k;
    int number=0;
    char tmp1[7], tmp2[7];
    string prvi, drugi;
    char tmp;
    int is;
    int n;
    x_i = x;
    y_i = y;
    stringstream ss1,ss2;//create a stringstream
    ss1 << x_i;
    ss2 << y_i;
    if (ss1.str().length()!=ss2.str().length()) 
    {
        return number;
    }
    for (i=x_i; i<y_i; i++) 
    {
//        itoa(i,prvi,10);
        for (j=i+1; j<=y_i; j++) 
        {
            //
            stringstream ss;
            ss << j;
            drugi = ss.str();
//            cout << drugi << " " << j <<endl;
//            itoa(j,drugi,10);
//            tmp2 = drugi.c_str();
//            tmp = drugi[0];
            //do a permutation
            is = 1;
            for (int l=1; l<ss1.str().length(); l++) 
            {
                if (is) 
                {
                    tmp = drugi[0];
                    for (k=0; k<ss1.str().length()-1; k++) 
                    {
                        drugi[k]=drugi[k+1];
                    }
                    drugi[k]=tmp;
                    n=atoi(drugi.c_str());
                    if (n==i) 
                    {
                        number++;
                        is=0;
                    }
                }
            }
        }
    }
    return number;
}

int main ( int argc, char **argv )
{
    int number_of_cases;
    int first,second;
    int count;
    string filename(argv[1]);
    string line;
    char temp;
    ifstream myfile(filename.c_str());
    ofstream myfileOut("output.out");
    if (myfile.is_open()) 
    {
        //first read the number of lines
        getline (myfile,line);
        number_of_cases = atoi(line.c_str());
        //go for all lines get the number
        if (myfileOut.is_open())
        {
            for (int i=0; i<number_of_cases; i++) 
            {
                getline (myfile,line);
                sscanf(line.c_str(),"%d %d",&first,&second);
                count = number_of_pairs (first,second);
                myfileOut << "Case #"<<i+1<<": "<< count<<endl;
            }
            myfileOut.close();
        }
        myfile.close();
    }
}
