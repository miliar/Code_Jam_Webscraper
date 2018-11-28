#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;
map<char, char> GMapping;

void init()
{
	GMapping['a'] = 'y';
	GMapping['b'] = 'h';
	GMapping['c'] = 'e';
	GMapping['d'] = 's';
	GMapping['e'] = 'o';
	GMapping['f'] = 'c';
	GMapping['g'] = 'v';
	GMapping['h'] = 'x';
	GMapping['i'] = 'd';
	GMapping['j'] = 'u';
	GMapping['k'] = 'i';
	GMapping['l'] = 'g';
	GMapping['m'] = 'l';
	GMapping['n'] = 'b';
	GMapping['o'] = 'k';
	GMapping['p'] = 'r';
	GMapping['q'] = 'z';
	GMapping['r'] = 't';
	GMapping['s'] = 'n';
	GMapping['t'] = 'w';
	GMapping['u'] = 'j';
	GMapping['v'] = 'p';
	GMapping['w'] = 'f';
	GMapping['x'] = 'm';
	GMapping['y'] = 'a';
	GMapping['z'] = 'q';
}

void process(string filename)
{
	string line;
	ifstream ifs(filename.c_str());
	ofstream ofs("output");
	int numTestCases = 0;
	int cnt = 0;
	while (getline(ifs, line))
	{
		if (line[0] >= '0' && line[0] <= '9') 
		{
			numTestCases = atoi(line.c_str());
			continue;
		}
		for (int i = 0; i < line.size(); i++)
		{
			if (line[i] >= 'a' && line[i] <= 'z')
				line[i] = GMapping[line[i]];	
		}
		ofs<<"Case #"<<cnt + 1<<": "<<line<<endl;
		cnt++;
	}
	ifs.close();
	ofs.close();
}

int main(int argc, char **argv)
{
	init();
	process(argv[1]);
	return 0;
}
