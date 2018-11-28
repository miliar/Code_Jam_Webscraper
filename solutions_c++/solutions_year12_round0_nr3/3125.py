#include<iostream>
#include<sstream>
#include<string>
#include<set>

using namespace std;

string get_string(int i)
{
	string s;
	stringstream convert;
	convert << i;
	convert >> s;
	return s;
}

int get_int(string s)
{
	int i;
	stringstream convert;
	convert << s;
	convert >> i;
	return i;
}

int solve()
{
	int a, b;
	cin >> a >> b;

	int count = 0;
	string s;

	set<int> found;

	for(int i = a; i <= b; ++i)
	{
		found.clear();
		s = get_string(i);
		
		for(int j = 0; j < s.size(); ++j)
		{
			s = s.substr(1) + s[0];
			if(s[0] == '0')	continue;

			if(get_int(s) > i && get_int(s) <= b && found.find(get_int(s)) == found.end())	
			{
				found.insert(get_int(s));
				++count;
			}
		}
	}

	return count;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)	cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}
