#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

#include "math.h"

using namespace std;

string check(int N, int K)
{
  long exp = ((long)pow(2.0, (double)N) - 1);
   cout << exp << ";" << (K & exp) << ":" << ((K & exp)>=exp) << " <=> ";
   return (K & exp) >= exp ? "ON" : "OFF";
}

int main(int argc, char** argv)
{
    if(argc < 1)
    {
	cout << "You must give the input file :)" << endl;
	return 0;
    }
    
    ifstream _input;
    cout << "opening: " << argv[1] << endl;
    _input.open(argv[1], ifstream::in);
    ofstream _output;
    _output.open("output.out");
    
    int nbCases = 0;
    _input >> nbCases;
    
    cout << "treating " << nbCases << " cases." << endl;
    for(int i = 1; i <= nbCases; ++i)
    {
	int n, k;
	_input >> n;
	_input >> k;
	cout << "(n: " << n << ", k: " << k << ") => \t ";
	
	stringstream output;
	output << "Case #" << i << ": "  << check(n, k) << endl;
	
	_output << output.str();
	cout << output.str();
    }
    
    _input.close();
    _output.close();
    return 1;
}
