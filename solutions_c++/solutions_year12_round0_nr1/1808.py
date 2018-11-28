#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	int casos, i, j;
	map<char,char> googlerese;
	string linea;
	
	googlerese['a'] = 'y';
	googlerese['b'] = 'h';
	googlerese['c'] = 'e';
	googlerese['d'] = 's';
	googlerese['e'] = 'o';
	googlerese['f'] = 'c';
	googlerese['g'] = 'v';
	googlerese['h'] = 'x';
	googlerese['i'] = 'd';
	googlerese['j'] = 'u';
	googlerese['k'] = 'i';
	googlerese['l'] = 'g';
	googlerese['m'] = 'l';
	googlerese['n'] = 'b';
	googlerese['o'] = 'k';
	googlerese['p'] = 'r';
	googlerese['q'] = 'z';
	googlerese['r'] = 't';
	googlerese['s'] = 'n';
	googlerese['t'] = 'w';
	googlerese['u'] = 'j';
	googlerese['v'] = 'p';
	googlerese['w'] = 'f';
	googlerese['x'] = 'm';
	googlerese['y'] = 'a';
	googlerese['z'] = 'q';
	googlerese[' '] = ' ';
	
	cin >> casos;
	cin.ignore();
	for (i = 0; i < casos; i++)
	{
		getline(cin,linea);
		cout << "Case #" << i+1 << ": ";
		for (j = 0; j < (int)linea.length(); j++)
		{
			cout << googlerese[linea[j]];
		}
		cout << endl;
	}
	
	return 0;
}

