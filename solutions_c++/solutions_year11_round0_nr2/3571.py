// CodeJam 2011 Qualification Q1
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int main()
{
    ifstream infile;
    infile.open("B-large.in");
    ofstream outfile;
    outfile.open("B-large.out");
    
    int caseno;
    infile >> caseno;
    for (int i=0; i<caseno; i++)
    {
        string elementlist = "";
        vector<char*> comb[27]; 
        vector<char> oppose[27];
        for (int i=0; i<27; i++)
        {
            comb[i].clear();
            oppose[i].clear();
        }
        vector<char*>::iterator combIt;
        vector<char>::iterator opposeIt;
        
        int C, D, N;
        infile >> C;
        for (int j=0; j<C; j++)
        {    
            string newcomb;
            infile >> newcomb;
            char *firstpair = new char[2], *secondpair = new char[2];
            firstpair[0] = newcomb[1];
            firstpair[1] = newcomb[2];
            combIt = comb[newcomb[0] - 'A'].end();
            comb[newcomb[0] - 'A'].insert(combIt, firstpair);    
            secondpair[0] = newcomb[0];
            secondpair[1] = newcomb[2];
            combIt = comb[newcomb[1] - 'A'].end();
            comb[newcomb[1] - 'A'].insert(combIt, secondpair);                        
        }
        
        infile >> D;
        for (int j=0; j<D; j++)
        {
            string newop;
            infile >> newop;
            opposeIt = oppose[newop[0] - 'A'].end();
            oppose[newop[0] - 'A'].insert(opposeIt, newop[1]);
            opposeIt = oppose[newop[1] - 'A'].end();
            oppose[newop[1] - 'A'].insert(opposeIt, newop[0]);
        }
        
        infile >> N;
        for (int j=0; j<N; j++)
        {
            char newelement;
            int combcheck = 0, opposecheck = 0;
            infile >> newelement;
            if (elementlist.length() > 0)
            {
                for (int k=0; k<comb[newelement - 'A'].size(); k++)
                {    
                    if (comb[newelement - 'A'][k][0] == elementlist[elementlist.length()-1])
                    {
                        elementlist[elementlist.length()-1] = comb[newelement - 'A'][k][1];
                        combcheck = 1;
                        break;
                    }
                }
                if (combcheck == 1)
                    continue;
                for (int k=0; k<oppose[newelement - 'A'].size(); k++)
                {
                    if (string::npos != elementlist.find(oppose[newelement - 'A'][k]))
                    {
                        elementlist = "";
                        opposecheck = 1;
                        break;
                    }
                }
                if (opposecheck == 1)
                    continue;
                elementlist += newelement;
            }
            
            else
                elementlist += newelement;
        }
        
        if (elementlist.length() == 0)
        {
            outfile << "Case #" << (i+1) << ": []\n";
            continue;
        }

        outfile << "Case #" << (i+1) << ": [";
        
        for (int k=0; k < (elementlist.length()-1); k++)
            outfile << elementlist[k] << ", ";            
        
        outfile << elementlist[elementlist.length()-1] << "]\n";
    }
    
    infile.close();
    outfile.close();
    return 0;
}