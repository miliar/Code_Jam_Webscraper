#include "iostream"
#include "fstream"
#include "string"
#include "algorithm"
#include "math.h"

using namespace std;

void main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	long T, N, K;
	infile >> T;
	string str = "";
	for(int i=0; i<T; i++)
	{
		infile >> N >> K;

		if(K < N)
		{
			str = "OFF";
		}
		else
		{
			long x = (long)pow(2., N);
			if(K % x == x - 1)
				str = "ON";
			else
				str = "OFF";
		}

		outfile << "Case #" << i+1 << ": " << str << endl;
	}
	infile.close();
	outfile.close();
}