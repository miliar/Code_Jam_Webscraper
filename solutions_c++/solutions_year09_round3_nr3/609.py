#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <queue>
#include <utility>
#include <cstdio>
#include <cstdlib>
using namespace std;

void main()
{
	string str;

	freopen("C:\\Projects\\codejam\\Release\\input.txt", "rt", stdin);
	freopen("C:\\Projects\\codejam\\Release\\output.txt", "wt", stdout);
	
	int t;
	cin >> t;
	for (int z=0;z<t;z++)
	{
		int p,q,temp;
		cin >> p >> q;
		vector<int> v;
		for (int i=0;i<q;i++)
		{
			cin >> temp;
			v.push_back(temp);
		}
		sort(v.begin(), v.end());
		
		int min = 1000000;
		do {
			vector<bool> flags(p, false);
			int count = 0;
			for (int i=0;i<v.size();i++) {
				flags[v[i] - 1] = true;
				for (int j=v[i];j<flags.size();j++)
				{
					if (flags[j] == true) break;
					count++;
				}
				for (int j=v[i]-2;j>=0;j--)
				{
					if (flags[j] == true) break;
					count++;
				}
			}

			if (count < min) {
				//for (int i=0;i<v.size();i++) cout << v[i] << " ";
				//cout << endl;
				min = count;
			}

		} while (next_permutation(v.begin(),v.end()));
		cout << "Case #" << (z+1) << ": " << min << endl;
	}
}