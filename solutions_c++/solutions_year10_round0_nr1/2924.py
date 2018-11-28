#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int main(int argc, char* argv[])
{
	//Open file
	ifstream ifs;
	ifs.open(argv[1]);

	if(ifs.good())
	{
		int cases;
		
		//Read number of cases
		ifs >> cases;

		int i = 0;
		for(int i = 1; i <= cases; i++)
		{
			//Local vars
			int snappers;
			long clicks;
				
			//Get data for this case
			ifs >> snappers;
			ifs >> clicks;

			//Apply test
			if(clicks % (long)pow(2.0, (double)snappers) == (pow(2.0, (double)snappers) - 1))
				cout << "Case #" << i << ": ON" << endl;
			else
				cout << "Case #" << i << ": OFF" << endl;

		}
	}

	ifs.close(); 

	return 0;	
}

