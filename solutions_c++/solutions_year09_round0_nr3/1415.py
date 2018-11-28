// Solution by Maxim Kulikov <maxim.coolikov@gmail.com>
// Compiled with Visual Studio 2005 Express Edition

#include <cstdio>
#include <fstream>
#include <iostream>

using namespace std;

char message[] = "welcome to code jam";
int n = sizeof (message) / sizeof (message[0]) - 1;
int counter[512];

const int BUFF_SIZE = 1024;
char buffer[BUFF_SIZE + 1];

int main ()
{
	freopen ("C-large.in", "rt", stdin);
	freopen ("C-large.out", "wt", stdout);

	int test_n;
	cin >> test_n;
	cin.getline(buffer, BUFF_SIZE);
	for (int test = 1; test <= test_n; ++test)
	{
		cin.getline(buffer, BUFF_SIZE);
		memset (counter, 0, sizeof (counter));

		for (int i = 0; buffer[i]; ++i)
		{
			for (int j = n-1; j; --j)
				if (buffer[i] == message[j])
					counter[j] = (counter[j] + counter[j-1]) % 10000;
			if (buffer[i] == message[0])
				++counter[0];
		}

		printf ("Case #%d: %04d\n", test, counter[n-1]);
	}

	return 0;
}