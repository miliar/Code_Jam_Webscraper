#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int64;

int handle_case(ifstream& infile)
{
    unsigned int N, K, mask;
    infile >> N >> K;
    mask = (1 << N) - 1;
    //cout << "mask=" << mask << endl;
    //cout << "K=" << K << endl;
    if((K & mask) == mask)    return 1;
    else return 0;
}

int main(int argc, char* argv[])
{
    int Ncases, result;
    if(argc < 2)
    {
        cout << "Usage: ./code <infile>" << endl;
        exit(1);
    }

    ifstream infile(argv[1]);
    if(infile.is_open())
    {
        infile >> Ncases;
	for(int i=0; i<Ncases; i++)
	{
            result = handle_case(infile);
	    cout << "Case #" << (i+1) << ": " << (result ? "ON" : "OFF") << endl;
	}
    }
    else
    {
        cout << "error opening" << argv[1] << endl;
	return 1;
    }
    return 0;
}

