#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;
string mapping="yhesocvxduiglbkrztnwjpfmaq";

int main (int argc, char *argv [])
{
    int T = 0;
    int j = 0;
    int i = 1;

	char line [200];

	cin >> T;
	cin.getline (line, 101);

    while (T)
	{
		cin.getline (line, 101);

		printf ("Case #%d: ", i);

		for (j = 0; j < strlen (line); j ++) {
			if (line [j] >= 'a' && line [j] <= 'z') {
				printf ("%c", mapping [line [j] - 'a']);
			} else {
				printf (" ");
			}
		}

		printf ("\n");

		i ++;
		T --;
    }

    return 0;
}
