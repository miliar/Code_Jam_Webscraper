#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(int argc, char **argv)
{
	cout << argc << endl;
	if(argc != 2)
	{
		cout << "Wrong args" << endl;
		return 1;
	}
	ifstream f(argv[1]);
	ofstream o("aoutput.txt", ofstream::out);

	map<char,string> d;
	d['a'] = "y";
	d['b'] = "h";
	d['c'] = "e";
	d['d'] = "s";
	d['e'] = "o";
	d['f'] = "c";
	d['g'] = "v";
	d['h'] = "x";
	d['i'] = "d";
	d['j'] = "u";
	d['k'] = "i";
	d['l'] = "g";
	d['m'] = "l";
	d['n'] = "b";
	d['o'] = "k";
	d['p'] = "r";
	d['q'] = "z";
	d['r'] = "t";
	d['s'] = "n";
	d['t'] = "w";
	d['u'] = "j";
	d['v'] = "p";
	d['w'] = "f";
	d['x'] = "m";
	d['y'] = "a";
	d['z'] = "q";
	d[' '] = " ";


	int n;
	f >> n;
	f.ignore(10, '\n');

	for(int i = 0; i < n; i++)
	{
		string line;
		getline(f, line);

		string translation;
		for(int j = 0; j < line.size(); j++)
		{
			translation +=  d[line[j]];
		}

		o << "Case #" << i+1 << ": " << translation << endl;
	}
	o << endl;

	f.close();
	o.close();
	return 0;
}
