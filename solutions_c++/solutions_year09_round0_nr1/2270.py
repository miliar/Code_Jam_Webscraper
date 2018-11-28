// BEGIN CUT HERE

// END CUT HERE
#line 5 "HanoiTower.cpp"
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;



int main()
{
	
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

	vector< char > pattern[16];
	vector<string> words;
	vector<string> testcases;
	string str;
	int l, d, n, i, j, k, sum;

	cin>>l>>d>>n;

	for(i=0; i<d; i++)
	{
		cin>>str;
		words.push_back(str);
	}
	for(i=0; i<n; i++)
	{
		cin>>str;
		testcases.push_back(str);
	}


	for(i=0; i<n; i++)
	{
		str = testcases[i];
		for(j=0; j<l; j++)
			pattern[j].clear();

		for(j=0, k=0; j<str.length(); j++)
		{
			if(str[j]=='(')
			{
				j++;
				while(str[j]!=')')
				{
					pattern[k].push_back(str[j]); j++;
				}
				k++;
			}
			else
			{
				pattern[k].push_back(str[j]);
				k++;
			}
		}

		sum=0;
		for(j=0; j<d; j++)
		{
			for(k=0; k<l; k++)
			{
				if( find(pattern[k].begin(), pattern[k].end(), words[j][k])  == pattern[k].end() )
					break;
			}
			if(k==l)
				sum++;
		}

		cout<<"Case #"<<i+1<<": "<<sum<<endl;
	}


	return 0;
}