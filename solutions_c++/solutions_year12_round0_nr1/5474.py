#include <iostream>
#include <string>

using namespace std;

void convert(char* line, char* convline)
{
	char convchar;
	for(int i = 0; i < strlen(line); ++i)
	{
		switch(line[i])
		{
		case('a'):
			convchar = 'y';
			break;
		case('b'):
			convchar = 'h';
			break;
		case('c'):
			convchar = 'e';
			break;
		case('d'):
			convchar = 's';
			break;
		case('e'):
			convchar = 'o';
			break;
		case('f'):
			convchar = 'c';
			break;
		case('g'):
			convchar = 'v';
			break;
		case('h'):
			convchar = 'x';
			break;
		case('i'):
			convchar = 'd';
			break;
		case('j'):
			convchar = 'u';
			break;
		case('k'):
			convchar = 'i';
			break;
		case('l'):
			convchar = 'g';
			break;
		case('m'):
			convchar = 'l';
			break;
		case('n'):
			convchar = 'b';
			break;
		case('o'):
			convchar = 'k';
			break;
		case('p'):
			convchar = 'r';
			break;
		case('q'):
			convchar = 'z';
			break;
		case('r'):
			convchar = 't';
			break;
		case('s'):
			convchar = 'n';
			break;
		case('t'):
			convchar = 'w';
			break;
		case('u'):
			convchar = 'j';
			break;
		case('v'):
			convchar = 'p';
			break;
		case('w'):
			convchar = 'f';
			break;
		case('x'):
			convchar = 'm';
			break;
		case('y'):
			convchar = 'a';
			break;
		case('z'):
			convchar = 'q';
			break;
		default:
			convchar = line[i];
		}
		convline[i] = convchar;
		
	}
	convline[strlen(line)]=0;
}

int main()
{
	int nr_cases = 0;
	char line[101];
	char convline[101];

	cin >> nr_cases;
	cin.getline(line,101);	// skip past the endline

	for(int i = 0; i < nr_cases; ++i)
	{
		cin.getline(line,101);

		convert(line,convline);
		
		cout << "Case #" << i+1 << ": " << convline << endl;
	}
	return 0;
}