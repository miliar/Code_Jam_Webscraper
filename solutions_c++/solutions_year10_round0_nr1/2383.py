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
    
    unsigned int snappers = 0;
    din >> snappers;

    unsigned int clicks = 0;

    din >> clicks;

    unsigned int maxclicks = (1 << snappers);

    unsigned int reminder =  (clicks+1) % maxclicks;
 

    dout << "Case #" << (no+1) << ": ";

    if(reminder)
        dout <<  "OFF";
    else 
        dout << "ON";

    dout << endl;    
}


