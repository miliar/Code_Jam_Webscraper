#include <algorithm>
#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>

using namespace std;

int l, d, n, leng;
string dict[5000];
string in;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	getline(cin, in);
	istringstream iss(in);
	iss >> l >> d >> n;
	
	for(int i = 0; i < d; ++i)
	{
		getline(cin, in);
		dict[i] = in;
	}
	
	for(int i = 1; i <= n; ++i)
	{
		getline(cin, in);
		leng = in.size();
		int res = 0;
		for(int word = 0; word < d; ++word)
		{
			bool ok = true;
			for(int j = 0, pos = 0; j < leng; ++j, ++pos)
				if(in[j] == '(')
				{
					int lim = -1;
					for(int k = j + 1; k < leng; ++k)
						if(in[k] == ')')
						{
							lim = k;
							break;
						}
					bool found = false;
					for(int k = j + 1; k < lim; ++k)
						if(dict[word][pos] == in[k])
						{
							found = true;
							break;
						}
					if(found)
						j = lim;
					else
					{
						ok = false;
						break;
					}
				}
				else if(dict[word][pos] != in[j])
				{
					ok = false;
					break;
				}
			if(ok)
				++res;
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}
