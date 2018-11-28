#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	fstream inp,outp;
	inp.open("input.txt");
	outp.open("output.txt");
	int numTest;
	inp>>numTest;
	for(int i=0; i<numTest; i++)
	{
		int numRides, numPeeps, numGroups;
		inp>>numRides>>numPeeps>>numGroups;
		vector<int> groups;
		groups.resize(numGroups);
		for(int j=0; j<numGroups; j++)
		{
			inp>>groups[j];
		}		
		long int monies=0;
		int pos=0;
		for(int j=0; j<numRides; j++)
		{
			int k=0;
			while(1)
			{
				if(pos<(numGroups*(j+1)))
				{
					cout<<k<<"+"<<groups[pos%numGroups]<<endl;
					if((k+(groups[pos%numGroups]))<=numPeeps)
						k+=groups[pos%numGroups];
					else break;
					pos++;
				}else break;
			}
			monies+=k;
		}
		outp<<"Case #"<<i+1<<": "<<monies<<endl;
	}
	inp.close();
	outp.close();
	return 0;
}
