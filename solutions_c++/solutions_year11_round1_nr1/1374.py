#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <sstream>

#include <algorithm>

using namespace std;


int min(int a, int b, int c)
{
    if (a<b)
    {
        if (a<c)
        {
            return a;
        }
        else {
            return c;
        }
    } else {
        if (b <c )
        {
            return b;
        } else
        {
            return c;
        }
    }
}


int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output.txt");

    int noTests;

    inputFile>>noTests;

    for (size_t i = 0; i<noTests; i++)
    {

        long long N;
        int Pd, Pg;

        inputFile>>N>>Pd>>Pg;
        int minGamesToday = -1;

        for (int j=1; j<100;j++)
        {
            if (j>N)
            {
                break;
            }
            if (j*Pd%100 ==0)
            {
                minGamesToday = j;
            }
        }



        outputFile<<"Case #"<<i+1<<": ";

        if ((Pg==100) && (Pd!=100))
        {
            outputFile<<"Broken"<<endl;
        } else if ((Pg==0) && (Pd!=0)) {
            outputFile<<"Broken"<<endl;
        }
        else if (minGamesToday==-1)
        {
            outputFile<<"Broken"<<endl;
        } else {
            outputFile<<"Possible"<<endl;
        }



    }



}
