#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
	int N;
	cin >> N;
	for (int n = 1; n <= N; n++)
	{
		//cerr << 1;
		map<char, int> nums;
		string s;
		cin >> s;
		int ndig = 0;
		set<char> vals;
		for (int i = 0; i < s.size(); i++)
			vals.insert(s[i]);
		ndig = vals.size();
		//cout << "ndig " << ndig << endl;
		int base = (ndig < 2 ? 2 : ndig);
		
		//cout << "Using base " << base << endl;
		int curvalue = 1;
		long long total = 0;
		for (int i = 0; i < s.size(); i++)
		{
			//cerr << 2;
			int value;
			if (nums.count(s[i]) == 0)
			{
				nums[s[i]] = curvalue;
				if (curvalue == 0)
					curvalue = 2;
				else if (curvalue == 1)
					curvalue = 0;
				else
					curvalue++;
			}
			value = nums[s[i]];
			//cout << "For digit " << i << " using val " << value << endl;
			long long subtotal = 0;
			subtotal += value;
			for (int j = i; j < s.size() - 1; j++)
			{
				//cerr << 3;
				subtotal *= base;
			}
			//cout << "Subtotal " << subtotal << endl;
			total += subtotal;
		}
		cout << "Case #" << n << ": " << total << endl;
	}
	
	return 0;
}

