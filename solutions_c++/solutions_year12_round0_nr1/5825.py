#include <iostream>
#include <string>
using namespace std;

char convert(char x)
{
	if(x == 'a')
		return 'y';
	else if(x == 'b')
		return 'h';
	else if(x == 'c')
		return 'e';
	else if(x == 'd')
		return 's';
	else if(x == 'e')
		return 'o';
	else if(x == 'f')
		return 'c';
	else if(x == 'g')
		return 'v';
	else if(x == 'h')
		return 'x';
	else if(x == 'i')
		return 'd';
	else if(x == 'j')
		return 'u';
	else if(x == 'k')
		return 'i';
	else if(x == 'l')
		return 'g';
	else if(x == 'm')
		return 'l';
	else if(x == 'n')
		return 'b';
	else if(x == 'o')
		return 'k';
	else if(x == 'p')
		return 'r';
	else if(x == 'q')
		return 'z';
	else if(x == 'r')
		return 't';
	else if(x == 's')
		return 'n';
	else if(x == 't')
		return 'w';
	else if(x == 'u')
		return 'j';
	else if(x == 'v')
		return 'p';
	else if(x == 'w')
		return 'f';
	else if(x == 'x')
		return 'm';
	else if(x == 'y')
		return 'a';
	else if(x == 'z')
		return 'q';
	else if(x == ' ')
		return ' ';
	else
		cout << "ERROR IN CONVERSION\n";

	return '1';
}

int main()
{
	int numCases;
	cin >> numCases;

	string inString;
	getline(cin, inString);

	for(int i = 0; i < numCases; i++)
	{
		cout << "Case #" << i+1 << ": ";

		while(!getline(cin, inString))
			1;

		for(int j = 0; j < inString.length(); j++)
			cout << convert(inString[j]);

		cout << endl;
	}

	return 0;
}
