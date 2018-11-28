#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string process()
{
	string s;
	cin >> s;
	if(!next_permutation(s.begin(), s.end()))
	{
		int cnt = count(s.begin(), s.end(), '0');
		s = s.substr(cnt).insert(1,string(cnt+1,'0'));
	}
	return s;
}

int main()
{
	int n;
	cin >> n;
	for(int i = 0; i < n; i++)
		cout << "Case #" << i+1 << ": " << process() << endl;
}