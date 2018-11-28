#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

int main(int argc, char **argv)
{
	if(argc != 2)
	{
		cout << "Wrong args" << endl;
		return 1;
	}

	ifstream f(argv[1]);
	ofstream o("output.txt", ofstream::out);

	int T;
	string temp;
	f >> T;
	getline(f, temp);

	int j;

	for(int i = 0 ; i < T; i++)
	{

		int A, B;
		double p[100000];
		double op[100000];

		f >> A >> B;
		getline(f, temp);

		for( j = 0; j < A; j++)
		{
			f >> p[j];
		}
		getline(f, temp);

		double result = 0.0;
		int numoptions = (int)pow(2,A);

		int retypelen = B+1;
		int continuelen = B-A+1;

		cout << "Case " << i+1 << endl;

		for(j = 0; j < numoptions; j++)
		{
			op[j] = 1.0;
			for(int b = 0; b < A; b++)
			{
				int mask = 1 << b;
				if((mask & j)) op[j] *= 1-p[A-b-1];
				else op[j] *= p[A-b-1];
				
			}
			cout << op[j] << " ";
		}
		cout << endl;
		
		double minev = retypelen+1; // Just press enter and start over
		// k is num backspaces
		for(int k = 0; k <= A; k++)
		{
			double ev = 0;
			int valcap = 1;
			valcap = (k == 0) ? 0 : valcap << (k-1);
			cout << "valcap " << valcap << endl;
			for(int c = 0; c < numoptions; c++)
			{
				if(op[c] <= 0.0) continue;
				int numkeys;
			 	numkeys = continuelen + k*2;
				if(c > valcap) numkeys += retypelen;
				cout << numkeys << " " << op[c] << "   ";
				ev += op[c]*numkeys;
			}
			cout << endl;
			if(ev < minev) minev = ev;
		}

		o.setf(ios::fixed,ios::floatfield);
		o.precision(6);
		o << "Case #" << i+1 << ": " << minev << endl;
	}

	return 0;
}
