#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>

#define all(x) (x).begin(),(x).end()

using namespace std;

int n;

void write(const vector <char> &t)
{
	cout << "[";
	for (int i = 0 + 1; i < t.size(); i ++)
		cout << t[i] << ", ";
	if (t.size())
		cout << t.back();
	cout << "]" << endl;
}

void solve(int _case)
{
	map <pair<char,char>,char> m;
	map <pair<char,char>,bool> an;
	cin >> n;
	for (int i = 0; i < n; i ++)
	{
		string s;
		cin >> s;
		m[make_pair(s[0],s[1])]=s[2];
		m[make_pair(s[1],s[0])]=s[2];
	}
	int d;
	cin >> d;
	for (int i = 0; i < d; i ++)
	{
		string s;
		cin >> s;
		an[make_pair(s[0],s[1])]=1;
		an[make_pair(s[1],s[0])]=1;
	}
	cin >> n;
	string s;
	cin >> s;
	vector<char> t;
	for (int i = 0; i < n; i ++)
	{
		if (t.size() > 0 && isalpha(m[make_pair(t.back(),s[i])]))
		{
			char r = m[make_pair(t.back(),s[i])];
			t.pop_back();
			t.push_back(r);
		}
		else
			t.push_back(s[i]);
		for (int j = 0; j + 1 < (int)t.size(); j ++)
		{
			if (an[make_pair(t[j],t.back())])
				t.resize(0);
		}
//		write(t);
	}
	cout << "Case #" << _case << ": [";
	for (int i = 0; i + 1 < t.size(); i ++)
		cout << t[i] << ", ";
	if (t.size())
		cout << t.back();
	cout << "]" << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i ++)
		solve(i + 1);
	return 0;
}
