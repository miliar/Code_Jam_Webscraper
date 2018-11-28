#include <iostream>

using std::cin;
using std::cout;

bool chkugly(__int64 n)
{
	return (n % 2 == 0) || (n % 3 == 0) || (n % 5 == 0) || (n % 7 == 0);
}

__int64 gougly_recurse(__int64 currnum, char * line, bool bFirststep)
{
	__int64 nUgly = 0;
	if (*line == 0)
	{
		nUgly += (chkugly(currnum)) ? 1 : 0;
		return nUgly;
	}

	char buff[41] = {0};
	memset(buff, 0, 41);

	for (int i = 0;  ;++i)
	{
		buff[i] = line[i];
		__int64 stepnum = _atoi64(buff);

		nUgly += gougly_recurse(currnum + stepnum, line + i + 1, false);
		if (!bFirststep)
			nUgly += gougly_recurse(currnum - stepnum, line + i + 1, false);

		if (line[i+1] == 0)
			break;
	}

	return nUgly;
}

int main()
{
	int nCases = 0;

	cin >> nCases;
	cin.ignore(1);	// skip ':'
	for (int icase = 0; icase < nCases; ++icase)
	{

		char line[42];
		memset(line, 0, 42);
		cin.getline(line, 41);

		__int64 nUgly = gougly_recurse(0, line, true);
		cout << "Case #" << (icase+1) << ": " << nUgly << std::endl;
	}

	return 0;
}
