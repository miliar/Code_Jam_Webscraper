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
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		string str;
		getline(cin, str);
		vector<int> v(n);
		int highest;
		for(int i = 0; i < n; i++)
		{
			getline(cin, str);
			highest = 0;
			for(int j = 0; j < str.size(); j++)
				if(str[j] == '1')
					highest = j;
			v[i] = highest;
		}
		int res = 0;
		int temp;
		int j;
		for(int i = 0; i < n; i++)
		{
			if(v[i] < i + 1)
				continue;
			int rest = v[i];
			for(j = i + 1; j < n; j++)
			{
				temp = v[j];
				v[j] = rest;
				rest = temp;
				if(rest < i + 1)
				{
					v[i] = rest;
					res += j - i;
					break;
				}
			}
		}
		cout << res << endl;
	}
	return 0;
}
