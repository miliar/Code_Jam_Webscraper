#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
using namespace std;
int func(const string& str)
{
	int x = 1;
	for(int i = 1; i < str.size(); i++)
		if(str[i] != str[i - 1])
			x++;
	return x;
}
int main()
{
	freopen("../../google.in", "r", stdin);
	freopen("../../google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n, k;
		cin >> n;
		k = n;
		vector<int> v(n);
		for(int i = 0; i < n ; i++)
			v[i] = i;
		string str;
		cin >> str;
		int minm = 10000000;
		do
		{
			string temp;
			temp.resize(str.size());
			int o = str.size() / k;
			for(int j = 0; j < o; j++)
			{
				for(int i = 0; i < k; i++)
					temp[j * k + i] = str[j * k + v[i]];
			}
			minm = min(minm, func(temp));
		}while(next_permutation(v.begin(), v.end()));
		cout << minm << endl;

	}
	return 0;
}
