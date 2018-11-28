#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, char* argv[])
{
	char line[64];
	int t = 0;
	cin >> t;
	getchar();
	for (int i = 0; i < t; ++i)
	{
		int charset[36]; // 0-9: 0-9; 10-35: a-z
		memset(charset, -1, 36*sizeof(int));
		gets(line);
		int len = strlen(line);
		int base = 0;
		for (int j = 0; j < len; ++j)
		{
			int index;
			if (line[j] <= '9')
			{
				index = line[j] - '0';
			}
			else
			{
				index = line[j] - 'a' + 10;
			}
			if (charset[index] == -1)
			{
				charset[index] = base++;
			}
		}

		if (base == 1)
			++base; // no unary

		int i0, i1;
		for (int j = 0; j < 36; ++j)
		{
			if (charset[j] == 0)
				i0 = j;
			else if (charset[j] == 1)
				i1 = j;
		}
		charset[i0] = 1;
		charset[i1] = 0;

		for (int j = 0; j < len; ++j)
		{
			int index;
			if (line[j] <= '9')
			{
				index = line[j] - '0';
			}
			else
			{
				index = line[j] - 'a' + 10;
			}
			line[j] = charset[index];
		}

		long long curMag = 1;
		long long res = 0;
		for (int j = len - 1; j >= 0; --j)
		{
			res += line[j] * curMag;
			curMag *= base;
		}
		cout <<"Case #" <<(i+1) <<": " <<res <<endl;
	}
	return 0;
}

