/*
 * =====================================================================================
 *
 *       Filename:  welcomeToCodeJam.cpp
 *
 *    Description:
 *           
 *            How to run:   ./a.out inputfile outputfile
 *
 *        Version:  1.0
 *        Created:  09/03/2009 09:26:33 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  Mehul Rathod ( rathodmehul@gmail.com )
 *        Company:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

static int  truncatedCount = 0;


static void solveAProblem(int no, ifstream &din, ofstream &dout);

int main(int argc, char** argv)
{
    if(argc < 3)
        return 0;

    int problemCount = 0;

    ifstream din(argv[1]);
    ofstream dout(argv[2]);

    din >> problemCount;    

    string junk;

    getline(din,junk);

    for(int i = 0; i < problemCount; i++)
    {
        solveAProblem(i,din,dout);
    }

    din.close();
    dout.close();

    return 0;

}




static void solveAProblem(int no, ifstream &din, ofstream &dout)
{
    string inputLine;
    string refLine("welcome to code jam");

    getline(din,inputLine);

    vector<long long> possibleCount(inputLine.size());

    for(unsigned int i=0; i < possibleCount.size(); i++)  {
        possibleCount[i] = 0;
    }    

    for(unsigned int i=0; i < refLine.size(); i++){
        if(i==0)
        {
            for(unsigned int j=0; j < inputLine.size(); j++)  
            {
                if(refLine[i] == inputLine[j]) 
                {
                    possibleCount[j] = 1;    
                }
            }    
        }
        else 
        {
            long long tempCount = 0; 
            
            for(unsigned int j=0; j < inputLine.size(); j++)  
            {
                if(refLine[i] == inputLine[j]) 
                {
                    possibleCount[j] = tempCount;    
                }

                if(refLine[i-1] == inputLine[j])
                {
                    tempCount += possibleCount[j]; 
                    tempCount %= 10000;
                }    
            } 
        }    

    }

    long long finalCount = 0;

    for(unsigned int j=0; j < inputLine.size(); j++)  
    {
        if(refLine[refLine.size()-1] == inputLine[j]) 
        {
             finalCount += possibleCount[j]; 
        }
    } 


    int truncatedCount = finalCount % 10000; // only 4 digits
    

    dout << "Case #" << (no+1) << ": ";
    char prev = dout.fill('0');
    dout.width(4);
    dout <<  truncatedCount  << endl;
    dout.fill(prev); 

}


