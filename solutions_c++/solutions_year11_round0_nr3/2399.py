#include<iostream>
#include<vector>
#include <algorithm>
#include <stack>
#include <string>
#include <map>
#include <climits>

using namespace std;

string reverse(string s)
{
	string s2 = s;
	reverse(s2.begin(),s2.end());
	return s2;
}

bool check_r(map<string,bool>rmap, string t)
{
	for(int i = 0; i < t.length(); i++)
	{
		for(int j = 0; j < t.length(); j++)
		{
			if(i==j)
				continue;
			if(rmap[t.substr(i,1)+t[j]] || rmap[reverse(t.substr(i,1)+t[j])])
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	int tests;
	cin >> tests;
	for(int j = 0; j < tests; j++)
	{
		int N;
		cin >> N;
		long long x = 0;
		long long sum = 0;
		int min = LONG_MAX;
		for(int i = 0; i < N; i++)
		{
			int tmp;
			cin >> tmp;
			sum+= tmp;
			x = x^tmp;
			if(tmp<min)
				min = tmp;
		}
		if(x)
			printf("Case #%ld: NO\n",j+1);
		else
			printf("Case #%ld: %d\n",j+1,sum-min);
	}
}