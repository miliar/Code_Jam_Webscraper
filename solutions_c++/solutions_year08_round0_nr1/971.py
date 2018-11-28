#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int o = 0; o  < numTests; o++)
	{
		printf("Case #%d: ", o + 1);
		map<string, int> m;
		map<string, int>::iterator itr;
		int s;
		cin >> s;

		string str;
		getline(cin, str);
		for(int i = 0; i < s; i++)
		{
			getline(cin, str);
			m.insert(make_pair(str, i));
		}

		int q;
		cin >> q;
		getline(cin, str);

		vector<int> v(s, 0);
		for(int i = 0; i < q; i++)
		{
			getline(cin, str);
			if((itr = m.find(str)) == m.end())
				continue;
			else
			{
				int minm = 1000000;
				for(int j = 0; j < s; j++)
				{
					if(j == itr->second)
						continue;
					else
						minm = min(minm, v[j]);
				}
				v[itr->second] = minm + 1;
			}
		}

		int minm = 10000000;
		for(int i = 0; i < s; i++)
			minm = min(minm, v[i]);
		cout << minm << endl;
	}
	return 0;
}