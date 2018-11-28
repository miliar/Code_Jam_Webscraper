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
    

    unsigned int riders[1000];
    unsigned int nextGroup[1000];
    unsigned long chainMoney[1000];



    unsigned int round = 0;
    din >> round;

    unsigned long sits = 0;
    din >> sits;


    unsigned int groups = 0;
    din >> groups;

    unsigned long money =  0;


    for(int i=0; i < groups; i++)
    {
        din >> riders[i];
        nextGroup[i] = 0;
        chainMoney[i] = 0;
    }


    int i = 0;
    
   while(chainMoney[i] == 0) // catched all possible solution
   {

         unsigned long currentRider = riders[i];
    
         int j = i+1;

         if(j >= groups)
                j = 0;

         while(j!=i)
         {

            if((currentRider + riders[j])>sits)
            {
                break;     
            }

            
            currentRider += riders[j];

            j++;

             if(j >= groups)
               j = 0;

         }   

         nextGroup[i] = j;
         chainMoney[i] = currentRider;
         i = j;
    }


    int currentPointer = 0; 

    for(unsigned int k=0; k<round ; k++)
    {
        money += chainMoney[currentPointer];
        currentPointer = nextGroup[currentPointer];
    }


    dout << "Case #" << (no+1) << ": ";


    dout << money << endl;    
}


