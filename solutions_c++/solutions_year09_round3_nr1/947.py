#include <iostream>
#include <cstdlib>
#include <map>
#include <utility>
#include <cstring>

//#define _DEBUG

using namespace std;

map<char, int> getDigitTable(const char * s)
{
	const char * c = s;
	map<char, int> table;

	table.insert(pair<char, int>(*c++, 1));

	while (s[0] == *c) ++c;

	table.insert(pair<char, int>(*c++, 0));

	int n = 2;
	while (*c != '\0')
	{
		if ( table.find(*c) == table.end() )
		{
			table.insert(pair<char, int>(*c, n++));
		}

		++c;
	}

#if defined(_DEBUG)
	map<char, int>::const_iterator cit = table.begin();
	printf("base : %ld\n", table.size());
	while ( cit != table.end() )
	{
		printf("%c : %d\n", cit->first, cit->second);
		++cit;
	}
#endif

	return table;
}

size_t convert_seconds(const char * s)
{
	map<char, int> table = getDigitTable(s);
	
	const char * c = s + (strlen(s) - 1);

	size_t n = 0;
	size_t nbase = 1;
	while ( c >= s )
	{
		n += table[*c] * nbase;

		nbase *= table.size();
		--c;
	}

	return n;
}

int main(int argc, char** argv)
{
	char buf[128] = { 0 };

	cin.getline(buf, 128);
	size_t nCase = atoi(buf);

	for (size_t i = 1 ; i <= nCase ; ++i)
	{
		memset(buf, 0, 128);
		cin.getline(buf, 128);
		printf("Case #%ld: %ld\n", i, convert_seconds(buf));
	}

	return 0;
}
