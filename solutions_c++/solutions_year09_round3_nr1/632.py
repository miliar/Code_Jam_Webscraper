#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

string s;

long long map[255];
long long i;
void Map()
{
	i = 0;
	map[s[0]] = 1;

	
	for(long long x = 1; x < s.length(); x++)
	{
		if(map[s[x]] == -1)
			if(!i)
				map[s[x]] = 0, i = 2;
			else
			map[s[x]] = i++;

	}

	if(i <=1) i = 2;
}

long long go()
{
	long long ret = 0;
	for(long long x = s.length()-1, y = 1; x >= 0; x--, y *= i)
	{
		ret += (map[s[x]])*y;
	}

	return ret;
}
int main()
{
	ifstream cin("qq.in");
	ofstream cout("res.txt");
	long long t, casenum =1;

	cin >> t;

	while(t--)
	{
		memset(map, -1, sizeof(map));
		cin >> s;

		Map();

		cout << "Case #" << casenum++<<": " << go() << endl;
	}

	cout.close();
	return 0;
}