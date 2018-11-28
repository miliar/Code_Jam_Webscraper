#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

#include <math.h>

using namespace std;
// Main
int main(int arg, char** argv)
{
    // If no input file, print the usage, and exit.
    if(arg != 2)
    {
        cout << "Usage: " << endl;
        cout << "sc <filename>" << endl << endl;
	exit(0);
    }
	
    int T, N, K;

    // Parse file
    ifstream ifs(argv[1], ifstream::in);
    string sln;
    
    getline(ifs, sln);
    istringstream iss(sln, istringstream::in);
    iss >> T;

    // There are T cases
    for(int i = 1; i < T + 1; i ++)
        {
            getline(ifs, sln);
            istringstream iss(sln, istringstream::in);
            iss >> N >> K;
	    if((K % (int)pow(2,N)) == (int)(pow(2,N)) - 1)
		cout << "Case #" << i << ": ON" << endl;
            else
		cout << "Case #" << i << ": OFF" << endl;
	}
    ifs.close();

    return 0;
}
