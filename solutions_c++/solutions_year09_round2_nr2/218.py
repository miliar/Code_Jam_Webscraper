#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

int main (void)
{
	int t;
	int i;
	int c=1; 
	cin >> t;
	
	while (t-->0)
	{
		std::string s;
		int j;		
		cin >> s;
		
		for (i=1; i<s.size(); ++i)
		{
			if (s[i]>s[i-1]) break;
		}
		if (i==s.size())
		{
			s = "0" + s;
		}
		next_permutation(s.begin(), s.end());
		cout << "Case #" << (c++) << ": " << s << endl;
	}
	return 0; 
	
}