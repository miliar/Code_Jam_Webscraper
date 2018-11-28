#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
using namespace std;


int main()
{

	freopen ("A-small-attempt1.in", "r", stdin);
	freopen ("out.txt", "w", stdout);
	map<char, char> myMap;
	int cases;
	cin >> cases;
	string s;
	
	myMap['a'] = 'y';
	myMap['b'] = 'h';
	myMap['c'] = 'e';
	myMap['d'] = 's';
	myMap['e'] = 'o';
	myMap['f'] = 'c';
	myMap['g'] = 'v';
	myMap['h'] = 'x';
	myMap['i'] = 'd';
	myMap['j'] = 'u';
	myMap['k'] = 'i';
	myMap['l'] = 'g';
	myMap['m'] = 'l';
	myMap['n'] = 'b';
	myMap['o'] = 'k';
	myMap['p'] = 'r';
	myMap['q'] = 'z';
	myMap['r'] = 't';
	myMap['s'] = 'n';
	myMap['t'] = 'w';
	myMap['u'] = 'j';
	myMap['v'] = 'p';
	myMap['w'] = 'f';
	myMap['x'] = 'm';
	myMap['y'] = 'a';
	myMap['z'] = 'q';
	
	cin.ignore();
	for(int i=1 ; i<=cases ; i++)
	{
		cout << "Case #" << i << ": ";
		getline(cin, s);

		for (int j=0 ; j<s.length() ; j++)
			if (s[j] != ' ')
				cout << myMap[s[j]] ;
			else 
				cout << " ";
		cout << endl;
	}
}