#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <queue>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>

using namespace std;

long long getN(string str)
{
	vector<int> v;
	char fChar = str[0];
	for(int i = 0;i<str.size();i++)
	{
		if(fChar!=str[i])
		{
			v.push_back(str[i]);
			break;
		}
	}
	
	for(int i = 0 ; i < str.size() ; i++)
	{
		int j = 0;
		for(;j<v.size();j++)
		{
			if(v[j] == str[i])
			{
				break;
			}
		}
		if(j == v.size())
			v.push_back(str[i]);
	}
	if(v.size() == 1)
	{
		v.push_back(v[0]);
		v[0]=' ';
	}
	int base = v.size();
	if(base == 1)
		base++;
	long long ans = 0;
	long long pow = 1;
	for(int i = str.size()-1;i>=0;i--)
	{
		int num = 0;
		for(int k = 0;k<v.size();k++)
		{
			if(v[k] == str[i])
			{
				num = k;
			}
		}
		ans =ans + num *  pow;
		pow*=base;
	}
	return ans;
}
int main()
{
	ifstream ifs("A-large.in",ios::in);
	ofstream cout("large.out",ios::out);
	int n;
	ifs>>n;
	for(int i = 0;i<n;i++)
	{
		string str;
		ifs>>str;
		long long ans = getN(str);
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}

	return 0;
}