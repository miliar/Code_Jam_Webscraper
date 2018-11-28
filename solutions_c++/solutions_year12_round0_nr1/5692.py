#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

char Googlerese(char chr)
{
	if (chr == 'a') return 'y';
	else if (chr == 'b') return 'h';
	else if (chr == 'c') return 'e';
	else if (chr == 'd') return 's';
	else if (chr == 'e') return 'o';
	else if (chr == 'f') return 'c';
	else if (chr == 'g') return 'v';
	else if (chr == 'h') return 'x';
	else if (chr == 'i') return 'd';
	else if (chr == 'j') return 'u';
	else if (chr == 'k') return 'i';
	else if (chr == 'l') return 'g';
	else if (chr == 'm') return 'l';
	else if (chr == 'n') return 'b';
	else if (chr == 'o') return 'k';
	else if (chr == 'p') return 'r';
	else if (chr == 'q') return 'z';
	else if (chr == 'r') return 't';
	else if (chr == 's') return 'n';
	else if (chr == 't') return 'w';
	else if (chr == 'u') return 'j';
	else if (chr == 'v') return 'p';
	else if (chr == 'w') return 'f';
	else if (chr == 'x') return 'm';
	else if (chr == 'y') return 'a';
	else if (chr == 'z') return 'q';
}

int main()
{
	int T = 0; cin >> T;
	char y[256] = {0};
	cin.getline(y, sizeof(y));
	for (int x = 1; x <= T; x++)
	{
		cout << "Case #" << x << ": ";
		//Logic here
		cin.getline(y, sizeof(y));
		for (size_t i = 0; i < strlen(y); i++)
			y[i] = Googlerese(y[i]);

		cout << y;
		//End Logic
		cout << endl;
	}	
	return 0;
}
