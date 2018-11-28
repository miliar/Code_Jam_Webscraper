#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

char decode(char c);

void solve()
{
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("speaking_in_tongues-out.txt", "wt", stdout);

	int N, n;
	string line, word;
	cin >> N >> ws;
	n = 1;
	while(N--)
	{
		getline(cin, line);
		cout << "Case #" << n++ << ": ";
		for(int i = 0; i < line.length(); i++)
		{
			cout << decode(line[i]);
		}
		cout << endl;
	}
}

char decode(char c)
{
	switch(c)
	{
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
		default: return ' ';
	}
}