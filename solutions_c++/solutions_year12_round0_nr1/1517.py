#include <iostream>
#include <string>

using namespace std;

int main (int argc, char const* argv[])
{
	int T;
	cin >> T;
	string s;
	getline(cin,s);
	s.clear();
	int tableau[26] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
	for (int i = 0; i < T; i += 1)
	{
		getline(cin,s);
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < s.size(); j += 1)
		{
			if (s[j] == ' ')
			{
				cout << " ";
			}
			else
			{
				cout << char(tableau[s[j]-'a']+'a');
			}
		}
		cout << endl;
		s.clear();
		
	}
	return 0;
}
