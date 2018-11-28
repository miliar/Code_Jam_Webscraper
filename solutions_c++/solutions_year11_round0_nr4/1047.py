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
    int T, N, i, j;
    int c[1000];

    if(argc==1) DERR("no input file specified");

    ifstream infile(argv[1], ifstream::in);
    if(infile.fail()) DERR("cannot open file");
    infile >> T;
    if(debug) cout << "T=" << T << endl;
    for(i=0; i<T; i++)
    {
	// Read input
	infile >> N;
	if(debug) cout << "N=" << N << endl;
	for(j=0; j<N; j++)
	    infile >> c[j];

	// Count # of numbers in wrong position
	int count = 0;
	for(j=0; j<N; j++)
	    if(c[j] != j+1) count ++;

	// Output
	double expectation = count;
	printf("Case #%d: %.6f\n", i+1, expectation);
    }
    return 0;
}
