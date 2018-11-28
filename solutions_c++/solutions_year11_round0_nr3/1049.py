#include <iostream>
#include <fstream>

#include <stdlib.h>

#define DERR(x)   \
{  \
    cout << "error: " << (x) << endl; \
    exit(1); \
}

using namespace std;

static int debug = 0;

int main(int argc, char* argv[])
{
    int T, N, i;
    unsigned int c[1000];
    if(argc==1) DERR("no input file specified");

    ifstream infile(argv[1], ifstream::in);
    if(infile.fail()) DERR("cannot open file");
    infile >> T;
    if(debug) cout << "T=" << T << endl;
    for(int k=0; k<T; k++)
    {
	// Read input
	infile >> N;
	if(debug) cout << "N=" << N << endl;
	for(i=0; i<N; i++)
	{
	    infile >> c[i];
	    if(debug) cout << c[i] << " ";
	}
	if(debug) cout << endl;

	unsigned int x=0;
	for(i=0; i<N; i++) 
	{
	    x = x ^ c[i];
	}
	if(x>0)
	    cout << "Case #" << (k+1) << ": NO" << endl;
	else
	{
	    unsigned int sum, min;
	    sum=0; min=1.0e+7;
	    for(i=0; i<N; i++)
	    {
		sum += c[i];
		if(min > c[i]) min = c[i];
	    }
	    cout << "Case #" << (k+1) << ": " << (sum-min) << endl;
	}
    }
    return 0;
}
