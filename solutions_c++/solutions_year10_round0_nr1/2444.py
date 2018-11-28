#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fileIn("A-large.in");
    ofstream fileOut("A-large.out");
    int cant;
    fileIn >> cant;
    int n,k;
    bool result;
    int var;
    for(int i=0;i<cant;i++)
    {
            fileIn >> n;
            fileIn >> k;
            var=(int)pow(2,n);
            result = false;
            if ((k+1)%var==0)
                   result = true;
            fileOut << "Case #" << i+1 << ": ";
            if (result)
                     fileOut << "ON" << endl;
            else
                     fileOut << "OFF" << endl;
            
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
