#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	char tr[200];
	tr['a'] = 'y';
	tr['b'] = 'h';
	tr['c'] = 'e';
	tr['d'] = 's';
	tr['e'] = 'o';
	tr['f'] = 'c';
	tr['g'] = 'v';
	tr['h'] = 'x';
	tr['i'] = 'd';
	tr['j'] = 'u';
	tr['k'] = 'i';
	tr['l'] = 'g';
	tr['m'] = 'l';
	tr['n'] = 'b';
	tr['o'] = 'k';
	tr['p'] = 'r';
	tr['q'] = 'z';
	tr['r'] = 't';
	tr['s'] = 'n';
	tr['t'] = 'w';
	tr['u'] = 'j';
	tr['v'] = 'p';
	tr['w'] = 'f';
	tr['x'] = 'm';
	tr['y'] = 'a';
	tr['z'] = 'q';
	tr[' '] = ' ';

	int cnt;
	ifstream inf("1.in", ios::in);
	ofstream outf("1.out", ios::out);
	inf >> cnt;
	inf.get();
	int i, j;
	char w[110];
	
	
	for (i = 1; i <= cnt; i++)
	{
		j = 0;
		inf.getline(w, 104, '\n');
		while (w[j] != 0)
		{
			w[j] = tr[w[j]];
			j++;
		}
		outf << "Case #" << i <<": "<< w << endl;
	}
	outf.close();
	return 0;
}
