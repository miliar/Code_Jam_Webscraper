#include <iostream>
#include <string>
#include <sstream>
#define for0(i, N) for (int i = 0; i < (N); ++i)
using namespace std;

char c(char k)
{
	switch (k)
	{
		case ' ': return ' ';
		case 'a': return 'y';
		case 'b': return 'h';
		case 'c': return 'e';
		case 'd': return 's';
		case 'e': return 'o';
		case 'f': return 'c';
		case 'g': return 'v';
		case 'h': return 'x';
		case 'i': return 'd';
		case 'j': return 'u';
		case 'k': return 'i';
		case 'l': return 'g';
		case 'm': return 'l';
		case 'n': return 'b';
		case 'o': return 'k';
		case 'p': return 'r';
		case 'q': return 'z';
		case 'r': return 't';
		case 's': return 'n';
		case 't': return 'w';
		case 'u': return 'j';
		case 'v': return 'p';
		case 'w': return 'f';
		case 'x': return 'm';
		case 'y': return 'a';
		case 'z': return 'q';
	}
}

int main()
{
	string line;
	int N;
	cin >> N;
	getline(cin, line);
	for0(n, N)
	{
		cout << "Case #" << n + 1 << ": ";
		getline(cin, line);
		stringstream ss(line);
		char k;
		ss >> noskipws;
		ss >> k;
		while (!ss.eof())
		{			
			k = c(k);
			cout << k;
			ss >> k;
		}
		cout << endl;
	}
}	
