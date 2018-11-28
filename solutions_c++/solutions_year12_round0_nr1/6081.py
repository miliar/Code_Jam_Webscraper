#include <string>
#include <map>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	map<char, char> my_map;
	my_map['e'] = 'o';
	my_map['j'] = 'u';
	my_map['p'] = 'r';
	my_map['m'] = 'l';
	my_map['y'] = 'a';
	my_map['s'] = 'n';
	my_map['l'] = 'g';
	my_map['c'] = 'e';
	my_map['k'] = 'i';
	my_map['d'] = 's';
	my_map['x'] = 'm';
	my_map['v'] = 'p';
	my_map['n'] = 'b';
	my_map['r'] = 't';
	my_map['i'] = 'd';
	my_map['b'] = 'h';
	my_map['t'] = 'w';
	my_map['a'] = 'y';
	my_map['h'] = 'x';
	my_map['w'] = 'f';
	my_map['f'] = 'c';
	my_map['o'] = 'k';
	my_map['u'] = 'j';
	my_map['g'] = 'v';
	my_map['q'] = 'z';
	my_map['z'] = 'q';
	
	
	ofstream fout;
	fout.open("ouput.out");
	
	ifstream fin("A-small-attempt1.in");
	int T;
	string line;
	if(fin.is_open())
	{
		fin >> T;
		getline(fin, line);
		int case_num = 1;
		while(fin.good() && case_num <= T)
		{
			getline(fin, line);
			fout << "Case #" << case_num << ": ";
			for(int j = 0; j < 100 && line[j] != '\0'; ++j)
			{
				if(line[j] == ' ') 
					fout << ' ';
				else 
					fout << my_map[line[j]];
			}
			fout << endl;
			case_num++;
		}
	}
	return 0;
}
