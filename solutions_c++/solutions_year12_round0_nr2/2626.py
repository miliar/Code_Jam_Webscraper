#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int maxgooglers(vector<int> totals, int surprises, int atleast)
{
    int maxg = 0;
    for(int i=0; i<totals.size(); ++i)
    {
        int total = totals[i];
        if((total%3) == 0)
        {
            int max = total/3;
            int min = total/3;
            if(max>=atleast)
            {
                maxg++;
            }
            else
            {
                if(max==atleast-1 && surprises>0 && min>0)
                {
                    maxg++;
                    surprises--;
                }
            }
        }
        if((total%3) == 2)
        {
            int max = (total/3) + 1;
            int min = total/3;
            if(max>=atleast)
            {
                maxg++;
            }
            else
            {
                if(max==atleast-1 && surprises>0 && min>0)
                {
                    maxg++;
                    surprises--;
                }
            }
        }
        if((total%3) == 1)
        {
            int max = (total/3) + 1;
            if(max>=atleast)
            {
                maxg++;
            }
        }
    }
    return maxg;
}

int main(int argc, char* argv[])
{
    ifstream infile;
    ofstream outfile;
    infile.open( "/Users/Guy/Downloads/B-small-attempt0.in");
//    infile.open( "/gcjam/input.txt");
    outfile.open( "/gcjam/output.txt");

    int ntestcases;
    infile >> ntestcases;
    infile.ignore(1, '\n');
    for(int i=0; i<ntestcases; ++i)
    {
        int numgooglers;
        infile >> numgooglers;
        int surprises;
        infile >> surprises;
        int atleast;
        infile >> atleast;
        vector<int> totals;
        for(int j=0; j<numgooglers; ++j)
        {
            int total;
            infile >> total;
            totals.push_back(total);
        }

        outfile << "Case #" << i+1 << ": " << maxgooglers(totals, surprises, atleast) << endl;
        cout << "Case #" << i+1 << ": " << maxgooglers(totals, surprises, atleast) << endl;
    }
	return 0;
}