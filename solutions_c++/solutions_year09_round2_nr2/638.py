#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;
typedef pair<int, int> ii;



vector<int> v;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	char s[50];
		cin.getline(s, 50);
	for (int t = 0; t < T; ++t)
	{
		
		cin.getline(s, 50);
		v.clear();
		int l = strlen(s);
		for (int i = 0; i < l; ++i)
			v.push_back(s[i]-'0');
		cout << "Case #" << t+1 << ": ";
		if (next_permutation(v.begin(), v.end()))
		{
			if(v[0] == 0)
				cerr << "ASSDF!!\n";
			for (int i = 0; i < v.size(); ++i)
				cout << v[i];
			cout << endl;
		}
		else 
		{
			sort(v.begin(), v.end());
			int id = 0;
			int minid = -1;
			for (int i = 0; i < v.size(); ++i)
			{
				if (v[i] > 0)
				{
					if (minid < 0) minid = i;
					else if (v[i] < v[minid]) minid = i;
				}
			}
			if (minid == -1) cerr << "d@!!";
			swap(v[0], v[minid]);
			cout << v[0] << 0;
			
			for (int i = 1; i < v.size(); ++i)
				cout << v[i];
			cout << endl;
		}
	}
}