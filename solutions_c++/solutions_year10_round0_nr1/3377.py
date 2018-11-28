#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ifstream dataF("Input.in");
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
		int Nsnappers;
		int Kclicks;
		int cases;
		ofstream output("Ouput.out");
		dataStr >> cases;
		for(long i = 1; i <= cases; i++)
		{
			dataStr >> Nsnappers;
			dataStr >> Kclicks;
			output << "Case #" << i << ": ";
			int neededClicks = pow(2.0,Nsnappers) - 1;
			int check = ((Kclicks + 1) % (neededClicks + 1));
			if(Kclicks >= neededClicks && check == 0)
				output << "ON" << endl;
			else
				output << "OFF" << endl;
		}
	}
	else cout << "Unable to open file"; 
}
