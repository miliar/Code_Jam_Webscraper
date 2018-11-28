#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
	int snappers, snaps, cases;
	ifstream inp("A-large.in");
	if(!inp.is_open())
	{
		return -1;
	}
	ofstream out("out.txt");

	string line;
	getline(inp, line);
	istringstream s(line);
	s >> cases;
	for(int i=0; i<cases; i++)
	{
		getline(inp, line);
		istringstream s(line);
		s >> snappers >> snaps;
		if(snaps % int(pow(double(2.0), double(snappers)))
			== 
			(pow(double(2.0), double(snappers)) - 1))
		{
			out << "Case #" << i+1 << ": ON" << endl;
		}
		else
		{
			out << "Case #" << i+1 << ": OFF" << endl;
		}
	}

	return 0;
}