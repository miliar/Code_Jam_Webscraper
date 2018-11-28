#include <stdio.h>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, m, k;
	string s, s1;
	vector<map<string, int> > v(1);
	const int root = 0;
	cin >> t;//scanf("%lld", &t);//
	for (long long i = 0; i < t; ++i)
	{
		k = 0;
		v = vector<map<string, int> > (1);
		cin >> n >> m;//scanf("%lld %lld", &n, &m);//
		for (int j = 0; j < n; ++j)
		{
			int cur = root;
			int first = 0;
			cin >> s;
			// parsing
			while (first + 1 < s.length())
			{
				int tmp = s.find_first_of('/', first + 1);
				if (tmp == string::npos)
					tmp = s.length();
				s1 = s.substr(first + 1, tmp - first - 1);
				if (v[cur][s1] == 0)
				{
					v[cur][s1] = v.size();
					cur = v.size();
					v.push_back(map<string, int>());
					first = tmp;
				}				
				else 
				{
					first = tmp;
					cur = v[cur][s1];
				}
			}
		}
		for (int j = 0; j < m; ++j)
		{
			int cur = root;
			int first = 0;
			cin >> s;
			// parsing
			while (first + 1 < s.length())
			{
				int tmp = s.find_first_of('/', first + 1);
				if (tmp == string::npos)
					tmp = s.length();
				s1 = s.substr(first + 1, tmp - first - 1);
				if (v[cur][s1] == 0)
				{
					v[cur][s1] = v.size();
					cur = v.size();
					v.push_back(map<string, int>());
					first = tmp;
					++k;
				}				
				else 
				{
					first = tmp;
					cur = v[cur][s1];
				}
			}
		}
		cout << "Case #" << (i + 1) << ": " << k << endl;
	}
	return 0;
}