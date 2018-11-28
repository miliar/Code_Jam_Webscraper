// CodeJam 2011 Qualification Q1
#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int main()
{
    ifstream infile;
    infile.open("A-large.in");
    ofstream outfile;
    outfile.open("A-large.out");
    
    int caseno;
    infile >> caseno;
    for (int i=0; i<caseno; i++)
    {
        int oplace = 1, otime = 0, bplace = 1, btime = 0, walktime;
        string robot, buttonStr;
        int buttonno, button;
        infile >> buttonno;
        for (int j=0; j<buttonno; j++)
        {
            infile >> robot >> buttonStr;
            button = atoi(buttonStr.c_str());
            
            if (robot == "O")
            {
                walktime = button > oplace ? (button - oplace) : (oplace - button) ;
                if ((otime + walktime) >= btime)
                {
                    otime += walktime;
                    otime++;
                }
                else if ((otime + walktime) < btime)
                {
                    otime = btime + 1;
                }
                            
                oplace = button;                
                
            }
            
            else
            {
                walktime = button > bplace ? (button - bplace) : (bplace - button);
                if ((btime + walktime) >= otime)
                {
                    btime += walktime;
                    btime++;
                }
                else if ((btime + walktime) < otime)
                {
                    btime = otime + 1;
                }
                        
                bplace = button;                
            }    
        }
        outfile << "Case #" << i+1 << ": " << (otime > btime ? otime : btime) << "\n";
    }
    
    infile.close();
    outfile.close();
    return 0;
}
