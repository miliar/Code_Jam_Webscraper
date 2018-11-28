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
struct dTree
{
	double prob;
	string feature;
	dTree *left, *right;
	dTree(const string& stre)
	{
		string str = stre;
		int i = 0;
		while(str[i] != '(')
			i++;
		str[i] = ' ';
		string first, second, third;
		while(i < str.size() && str[i] != '(')
			i++;
		if( i== str.size())
		{
			stringstream ss;
			ss << str;
			ss >> prob;
			left = right = NULL;
		}
		else
		{
			string str1 = str.substr(0, i);
			str = str.substr(i, str.size() - i);
			stringstream ss;
			ss << str1;
			ss >> prob >> feature;
			int v = 1;
			i = 0;
			while(v != 0)
			{
				i++;
				if(str[i] == ')')
					v--;
				if(str[i] == '(')
					v++;
			}
			str1 = str.substr(0, i + 1);
			left = new dTree(str1);
			str = str.substr(i + 1, str.size() - i - 2);
			right = new dTree(str);
		}
	}
	double judge(const set<string> & s)
	{
		if(left == NULL)
			return prob;
		if(s.find(feature) != s.end())
			return prob * left->judge(s);
		else
			return prob * right->judge(s);
	}
};
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d:\n", testCounter + 1);
		string tree;
		int l;
		cin >> l;
		string str;
		getline(cin, str);

		for(int i = 0; i < l; i++)
		{
			getline(cin, str);
			tree += str;
		}
		dTree temp(tree);
		int k;
		cin >> k;
		for(int j = 0; j < k; j++)
		{
			string str;
			cin >> str;
			int n;
			cin >> n;
			set<string> s;
			for(int i = 0; i < n ;i++)
			{
				cin >> str;
				s.insert(str);
			}
			printf("%.9lf\n", temp.judge(s));
		}

	}
	return 0;
}
