#include <iostream>
#include <fstream>
#include "parsing.h"
#include <math.h>
using namespace std;

int main()
{
	int count;
	int *n;
	int *k;
	ifstream input("b.txt");
	ofstream output("out1.txt");
	parsing(input,count,n,k);
	for(int i = 0 ; i < count ; i++)
	{
		int result = pow(2,n[i]);
		int temp = result;

		if (0 == ( (k[i]+1) % (result) ) )
		{
			cout << "Case #" << i+1 << ": " <<"ON" << endl;
			output <<	"Case #" << i+1 << ": " <<"ON" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " <<"OFF" << endl;
			output <<	"Case #" << i+1 << ": " <<"OFF" << endl;
		}

	}

	return 0;
}