#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
	ifstream inp("C-small-attempt0.in");
	ofstream out("out.txt");
	int pmax, groupnum, times, cases, earned;
	string line;

	getline(inp, line);
	istringstream s(line);
	s >> cases;

	for(int i=0; i<cases; i++)
	{
		earned = 0;
		getline(inp, line);
		istringstream s(line);
		s >> times >> pmax >> groupnum;
		vector<int> groups;
		getline(inp, line);
		s = istringstream(line);
		for(int j=0; j<groupnum; j++)
		{
			int a;
			s >> a;
			groups.push_back(a);
		}

		for(int j=0; j<times; j++)
		{
			int gsize = 0, gnum = 0, tag = 0;
			while(tag != groupnum && ((gsize + groups[0]) <= pmax))
			{
				gsize += groups[0];
				gnum++;
				for(int k=0; k<groups.size()-1; k++)
				{
					swap(groups[k], groups[k+1]);
				}
				tag++;
			}
			earned += gsize;
		}
		out << "Case #" << i+1 << ": " << earned << endl;
	}

	return 0;
}