#include <algorithm>  
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  

#include <stdlib.h>
#include <string.h>

#define DERR(x)   \
{  \
    cout << "error: " << (x) << endl; \
    exit(1); \
}

static int debug = 0;

using namespace std;

void process_case(ifstream& infile, int caseno)
{
    int N;
    char array[101][101];
    double wp[100], owp[100], oowp[100], nop[100];

    infile >> N;
    if(debug) cout << "N=" << N << endl;
    for(int i=0; i<N; i++)
    {
	infile >> array[i];
    }

    //wp
    for(int i=0; i<N; i++)
    {
	int sum = 0;
	int n = 0;
	for(int j=0; j<N; j++)
	{
	    if(array[i][j] != '.')
	    {
		int x = array[i][j] - '0';
	       	sum += x;
	       	n++;
	    }
	    wp[i] = (double)sum / n;
	    nop[i] = n;
	}
	if(debug) cout << "wp[" << i << "] = " << wp[i] << endl;
    }

    //owp
    for(int i=0; i<N; i++)
    {
	double wpsum = 0;
	for(int j=0; j<N; j++)
	{
	    if(array[i][j] != '.')
	    {
		int x = array[j][i] - '0';
		wpsum = wpsum + (wp[j] * nop[j] - x) / (nop[j] - 1);
	    }
	    owp[i] = wpsum / nop[i];
	}
	if(debug) cout << "owp[" << i << "] = " << owp[i] << endl;

    }

    //oowp
    for(int i=0; i<N; i++)
    {
	double owpsum = 0;
	for(int j=0; j<N; j++)
	{
	    if(array[i][j] != '.')
	    {
		owpsum = owpsum + owp[j];
	    }
	    oowp[i] = owpsum / nop[i];
	}
	if(debug) cout << "oowp[" << i << "] = " << oowp[i] << endl;
    }

    cout << "Case #" << caseno << ":" << endl;
    for(int i=0; i<N; i++)
    {
	double rpi = (wp[i]/4 + owp[i]/2 + oowp[i]/4);
	printf("%1.12f\n", rpi);
    }
}


int main(int argc, char* argv[])
{
    int T;
    if(argc==1) DERR("no arguments");
    ifstream infile(argv[1], ifstream::in);
    if(infile.fail()) DERR("cannot open file");
    infile >> T;
    if(debug) cout << "T=" << T << endl;
    for(int i=0; i<T; i++)
    {
	process_case(infile, i+1);
    }
}



