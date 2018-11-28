#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

string getNextNumber(string s)
{
	if (next_permutation(s.begin(), s.end()))
		return s;

	sort(s.begin(), s.end());
	string zeros("");
	string t = s;

	size_t pos = s.rfind('0');
	if ( pos != string::npos )
	{
		zeros = s.substr(0, pos + 1);
		t = s.substr(pos + 1, s.size() - zeros.size());
	}
	t = t.substr(0, 1) + "0" + zeros + t.substr(1, t.size() - 1);
	
	return t;
}

int main(int argc, char** argv)
{
	char buf[128] = { 0 };
	cin.getline(buf, 128);

	int n = atoi(buf);
	for (int i = 1 ; i <= n ; ++i)
	{
		memset(buf, 0, 128);
		cin.getline(buf, 128);
		printf("Case #%u: %s\n", i, getNextNumber(buf).c_str());
	}

	return 0;	
}
