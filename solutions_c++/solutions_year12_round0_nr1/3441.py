#include <iostream>
#include <cmath> 
#include <vector>
#include <algorithm>
#include <numeric>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <set>
#include <list>
#include <utility>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <windows.h>

using namespace std; 

void main()
{
	int n, j = 1; 
	string in;
	map<char,char>alpha;
	alpha['a'] = 'y';
	alpha['b'] = 'h';
	alpha['c'] = 'e';
	alpha['d'] = 's';
	alpha['e'] = 'o';
	alpha['f'] = 'c';
	alpha['g'] = 'v';
	alpha['h'] = 'x';
	alpha['i'] = 'd';
	alpha['j'] = 'u';
	alpha['k'] = 'i';
	alpha['l'] = 'g';
	alpha['m'] = 'l';
	alpha['n'] = 'b';
	alpha['o'] = 'k';
	alpha['p'] = 'r';
	alpha['q'] = 'z';
	alpha['r'] = 't';
	alpha['s'] = 'n';
	alpha['t'] = 'w';
	alpha['u'] = 'j';
	alpha['v'] = 'p';
	alpha['w'] = 'f';
	alpha['x'] = 'm';
	alpha['y'] = 'a';
	alpha['z'] = 'q';

	string filename = "A-small-attempt2.in";
	fstream fin(filename.c_str(), ios::in);
	fstream fout("output.out", ios::out);

	fin >> n;
	fin.ignore();

	while(n--){
		string out = "";
		stringstream ss;
		ss << "Case #" << j << ": ";
		getline(fin, in);
		
		for(int i = 0; i < in.length(); i++)
			ss << alpha[in[i]];
		
		getline(ss, out);
		out += "\n";
		
		fout << out;
		j++;
	}
}