#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

//            abcdefghijklmnopqrstuvwxyz
//char sub[] = "    o           z       a ";

//            abcdefghijklmnopqrstuvwxyz
char sub[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	char s[MAX_PATH];
	cin.getline(s, sizeof(s));

	int nCount, numCase = 1;
	nCount = atoi(s);

	while (numCase <= nCount)
	{
		cin.getline(s, sizeof(s));

		for (int i = 0, j = strlen(s); i < j; i++)
		{
			s[i] = (s[i] != ' ' ? sub[s[i] - 'a'] : ' ');

// 			if (s[i] != ' ')
// 			{
// 				char c = sub[s[i] - 'a'];
// 				if (c == ' ')
// 					c = toupper(s[i]);
// 				s[i] = c;
// 			}
		}

		cout << "Case #" << numCase << ": ";
		cout << s;
		cout << "\n";

		numCase++;
	}
	return 0;
}
