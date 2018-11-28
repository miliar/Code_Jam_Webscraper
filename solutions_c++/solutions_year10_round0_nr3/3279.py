#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>

using namespace std;

int main()
{
	ifstream dataF("Input.txt");
	string data;
	string line;
	if (dataF.is_open())
	{
		while (! dataF.eof() )
		{
			getline (dataF,line);
			data += line + '\n';
		}
		dataF.close();

		stringstream dataStr;
		dataStr.clear();
		dataStr.str(data);
		int Rides;
		int Kmaxpeople;
		int Ngroups;
		int cases;
		ofstream output("Ouput.out");
		dataStr >> cases;
		for(long i = 1; i <= cases; i++)
		{
			dataStr >> Rides;
			dataStr >> Kmaxpeople;
			dataStr >> Ngroups;
			output << "Case #" << i << ": ";
			queue<int> theLine;
			int nextGroup;
			for(int n = 0; n < Ngroups; n++)
			{
				dataStr >> nextGroup;
				theLine.push(nextGroup);
			}
			
			int moneys = 0;
			for(int r =0; r < Rides; r++)
			{
				queue<int> onRide;
				int numberOn = 0;
				while(numberOn < Kmaxpeople && !theLine.empty())
				{
					int front = theLine.front();
					if(front + numberOn > Kmaxpeople)
						break;
					numberOn += front;
					onRide.push(front);
					theLine.pop();
				}
				moneys += numberOn;
				while(!onRide.empty())
				{
					theLine.push(onRide.front());
					onRide.pop();
				}
			}
			output << moneys << " " << endl;
		}
	}
	else cout << "Unable to open file"; 
}
