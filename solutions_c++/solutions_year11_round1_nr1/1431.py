#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int GCD(int a, int b)
{
	while( 1 )
	{
		a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

		if( b == 0 )
			return a;
	}
}

int main()
{
	ifstream input("A-small-attempt2.in");
	ofstream output("outputs.txt");

	int T;
	input >> T;

	for(int caseID = 1; caseID <= T; caseID++)
	{
		//read data
		int N;
		int a,b,c;
		input >> a >> b >> c;
		if (b != 100 && b != 0)
		{
			int x = b;
			int y = 100-b;
			int mygcd = GCD(x,y);
			int NLimit = x/mygcd + y/mygcd;
			if (NLimit > a)
			{
				output << "Case #" << caseID << ": "<< "Broken" << endl;
				continue;
			}
			

		}
		if (c != 100 && c!= 0)
		{
			output << "Case #" << caseID << ": "<< "Possible" << endl;
			continue;
		}

		if (c == 100)
		{
			if (b == 100)
			{
				output << "Case #" << caseID << ": "<< "Possible" << endl;
			}
			else
			{
				output << "Case #" << caseID << ": "<< "Broken" << endl;
			}
			continue;
		}
		if (c == 0)
		{
			if (b == 0)
			{
				output << "Case #" << caseID << ": "<< "Possible" << endl;
			}
			else
			{
				output << "Case #" << caseID << ": "<< "Broken" << endl;
			}
			continue;
		}


		//solve

		//output result
		//output << "Case #" << caseID << ": "<< count << endl;
	}
}