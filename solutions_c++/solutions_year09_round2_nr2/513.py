#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		string N;
		cin >> N;
		vector<char> v;
		for (int j = 0; j < N.length(); ++j)
			v.push_back(N[j]);
			
		cout << "Case #" << (i+1) << ": ";
		bool f = next_permutation(v.begin(),v.end());
		if (!f)
		{
			sort(v.begin(),v.end());			
			string s = "";
			int num = 0;
			for (int j = 0; j < v.size(); ++j)
			{
				if (v[j] != '0')
					s += v[j];
				else
					++num;
			}			
			for (int j = 0; j < s.length(); ++j)
			{
				if (j == 1)
					for (int k = 0; k < num+1; ++k)
						cout << "0";
				cout << s[j];
				if (s.length() == 1)
					for (int k = 0; k < num+1; ++k)
						cout << "0";
			}
			cout << endl;
		} else
		{
			for (int j = 0; j < v.size(); ++j)
				cout << v[j];
			cout << endl;
		}
		
	}
	return 0;
}
