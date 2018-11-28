//
//  google1.cpp
//  
//
//  Created by Božidar Ševo on 14.4.2012..
//  Copyright (c) 2012. Seodoa. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main ( int argc, char **argv )
{
    int array_of_change[26] = {24,6,2,15,10,-3,15,16,-5,11,-2,-5,-1,-12,-4,2,9,2,-5,3,-11,-6,-17,-11,-24,-9};
    int number_of_lines;
    string filename(argv[1]);
    string line;
    char temp;
    ifstream myfile(filename.c_str());
    ofstream myfileOut("output.out");
    if (myfile.is_open()) 
    {
        //first read the number of lines
        getline (myfile,line);
        number_of_lines = atoi(line.c_str());
        //go for all lines and translate to Googlerese
        if (myfileOut.is_open())
        {
            for (int i=0; i<number_of_lines; i++) 
            {
                getline (myfile,line);
                for (int j=0; j<line.length(); j++) {
                    //change every char
                    temp=line[j];
                    if (temp!='\n') {
                        temp = temp + array_of_change[temp-'a'];
                        line[j]=temp;
                    }
                }
                myfileOut << "Case #"<<i+1<<": "<< line<<endl;
            }
            myfileOut.close();
        }
        myfile.close();
    }
}
