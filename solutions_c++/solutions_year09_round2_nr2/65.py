#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for (int t=1; t<=tests; t++)
	{
		string s;
		cin >> s;
		bool sorted = true;
		for (int i=1; i<s.size(); i++)
		{
			if (s[i] > s[i-1])
				sorted = false;
		}
		if (sorted)
			s = "0" + s;
		next_permutation(s.begin(), s.end());
		cout <<"Case #" << t <<": " <<s <<endl;
	}
}
