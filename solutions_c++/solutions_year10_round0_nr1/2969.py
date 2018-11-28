// Google CodeJam 2010 Entry
// By Steven Duda (duda69@gmail.com)
// C++ Source code; compile using gcc 4.2.2;

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
    unsigned long T=1, n=1, k=0;
    const long double base = 2.0;

    ofstream output("output.txt");
    ifstream ifs("A-large.in");
    ifs >> T;
    
    //Read T Tests
    for(unsigned long i=0;i<T;++i)
    {
        //Read Next Test Values (n, k)
        ifs >> n;
        ifs >> k;
        
        unsigned long power = static_cast<unsigned long>(pow(base,static_cast<long double>(n)));
        
        if((k!=0)&&((k % power)==(power-1)))
            output << "Case #" << (i+1) << ": " << "ON" << endl;
        else
            output << "Case #" << (i+1) << ": " << "OFF" << endl;
    }

    ifs.close();
    output.close();
    
    return (0);
}

