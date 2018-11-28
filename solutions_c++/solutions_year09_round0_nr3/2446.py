#include <string>
#include <iostream>
#include <utility>
#include <cstdio>

using namespace std;

const string welcome("welcome to code jam");

string refine_string( const string & s )
{
	string result("");

	size_t start = s.find('w');

	for (size_t i = start ; i != string::npos && i < s.length() ; ++i)
	{
		if ( welcome.find(s[i]) != string::npos )
		{
			result.push_back(s[i]);
		}
	}

	return result;
}

void count_welcome_string(
	size_t n, const string & s, size_t pos, size_t & count )
{
	if ( n == welcome.length() )
	{
		++count;
		return;
	}

	if ( pos >= s.length() || pos == string::npos )
	{
		return;
	}

	pos = s.find(welcome[n], pos);
	while ( pos != string::npos )
	{
		count_welcome_string(n + 1, s, pos + 1, count);
		pos = s.find(welcome[n], pos + 1);
	}
}

size_t count_welcome_string(const char * s)
{
	size_t count = 0;
	count_welcome_string( 0, refine_string(string(s)), 0, count ); 
	return count;
}


int main(int argc, char ** argv)
{
	char buf[512] = { 0 };
	cin.getline(buf, 512);

	size_t nCase = atoi(buf);

	for (size_t i = 1 ; i <= nCase ; ++i)
	{
		cin.getline(buf, 512);
		printf("Case #%d: %04d\n", i, count_welcome_string(buf));
	}
	
	return 0;
}

