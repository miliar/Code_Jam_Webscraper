#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char Replace(char c);
int main()
{
	int n;
	ifstream in("A-small-attempt0.in");
	ofstream out("Speaking in Tongues.out");
	in >> n;
	string s;
	getline(in, s);
	for (int i = 0; i < n; i++)
	{
		getline(in, s);
		for (int j = 0; j < s.size(); j++)
			s[j] = Replace(s[j]);
		out << "Case #" << i + 1 << ": " << s << endl;
	}
	return 0;
}

char Replace(char c)
{
	switch (c)
	{
	case ' ':
		return ' ';
		break;
	case 'a':
		return 'y';
		break;
	case 'b':
		return 'h';
		break;
	case 'c':
		return 'e';
		break;
	case 'd':
		return 's';
		break;
	case 'e':
		return 'o';
		break;
	case 'f':
		return 'c';
		break;
	case 'g':
		return 'v';
		break;
	case 'h':
		return 'x';
		break;
	case 'i':
		return 'd';
		break;
	case 'j':
		return 'u';
		break;
	case 'k':
		return 'i';
		break;
	case 'l':
		return 'g';
		break;
	case 'm':
		return 'l';
		break;
	case 'n':
		return 'b';
		break;
	case 'o':
		return 'k';
		break;
	case 'p':
		return 'r';
		break;
	case 'q':
		return 'z';
		break;
	case 'r':
		return 't';
		break;
	case 's':
		return 'n';
		break;
	case 't':
		return 'w';
		break;
	case 'u':
		return 'j';
		break;
	case 'v':
		return 'p';
		break;
	case 'w':
		return 'f';
		break;
	case 'x':
		return 'm';
		break;
	case 'y':
		return 'a';
		break;
	case 'z':
		return 'q';
		break;
	}
	return 0;
}