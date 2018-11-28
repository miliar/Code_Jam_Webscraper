#include <fstream>
#include <vector>
#include <string>

using namespace std;

char replacements[26];

void setup()
{
	replacements['a' - 97] = 'y' - 97;
	replacements['b' - 97] = 'h' - 97;
	replacements['c' - 97] = 'e' - 97;
	replacements['d' - 97] = 's' - 97;
	replacements['e' - 97] = 'o' - 97;
	replacements['f' - 97] = 'c' - 97;
	replacements['g' - 97] = 'v' - 97;
	replacements['h' - 97] = 'x' - 97;
	replacements['i' - 97] = 'd' - 97;
	replacements['j' - 97] = 'u' - 97;
	replacements['k' - 97] = 'i' - 97;
	replacements['l' - 97] = 'g' - 97;
	replacements['m' - 97] = 'l' - 97;
	replacements['n' - 97] = 'b' - 97;
	replacements['o' - 97] = 'k' - 97;
	replacements['p' - 97] = 'r' - 97;
	replacements['q' - 97] = 'z' - 97;
	replacements['r' - 97] = 't' - 97;
	replacements['s' - 97] = 'n' - 97;
	replacements['t' - 97] = 'w' - 97;
	replacements['u' - 97] = 'j' - 97;
	replacements['v' - 97] = 'p' - 97;
	replacements['w' - 97] = 'f' - 97;
	replacements['x' - 97] = 'm' - 97;
	replacements['y' - 97] = 'a' - 97;
	replacements['z' - 97] = 'q' - 97;
}

int getReplacement(int x)
{
	return replacements[x];
}

int main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");
	setup();

	int nLines;
	input >> nLines;

	string *strings = new string[nLines];
	getline(input, strings[0], '\n');
	for(int i = 0; i < nLines; i++)
	{
		getline(input, strings[i], '\n');
	
		output << "Case #" << i + 1 << ": ";
		for(int j = 0; j < strings[i].length(); j++)
		{
			if ( strings[i][j] > 96 && strings[i][j] < 123 )
				output << (char) (getReplacement( strings[i][j] - 97 ) + 97 );
			else
				output << strings[i][j];
		}
		output <<  endl;
	}
}