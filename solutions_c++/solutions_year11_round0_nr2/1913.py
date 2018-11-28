#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long lint;
typedef vector<int> vi;
typedef pair<int, int> pii;
const int Inf = 0x7fffffff;

int Solution(int test)
{
	int c;
	cin >> c;
	vector< vector<char> > rep(26, vector<char>(26, '0'));
	for(int i = 0; i < c; ++i)
	{
		string str;
		cin >> str;
		rep[str[0] - 'A'][str[1] - 'A'] = str[2];
		rep[str[1] - 'A'][str[0] - 'A'] = str[2];
	}
	int d;
	cin >> d;
	vector< vector<bool> > ops(26, vector<bool>(26));
	for(int i = 0; i < d; ++i)
	{
		string str;
		cin >> str;
		ops[str[0] - 'A'][str[1] - 'A'] = true;
		ops[str[1] - 'A'][str[0] - 'A'] = true;
	}
	int n;
	string s, res = "";
	cin >> n >> s;
	for(int i = 0; i < s.size(); ++i)
	{
		char now = s[i];
		if(res.size() && rep[ res[res.size() - 1] - 'A' ][ now - 'A' ] != '0')
			res[res.size() - 1] = rep[ res[res.size() - 1] - 'A' ][ now - 'A' ];
		else
		{
			bool flag = false;
			for(int j = 0; j < 26; ++j)
				if(ops[j][now - 'A'] && res.find('A' + j, 0) != -1)
				{
					res.clear();
					flag = true;
					break;
				}
			if(!flag)
				res.pb(now);
		}
	}
	cout << "Case #" << test << ": [";
	for(int i = 0; i < (int)res.size() - 1; ++i)
		cout << res[i] << ", ";
	if(res.size())
    	cout << res[res.size() - 1];
	cout << ']' << endl;
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
		Solution(i);
#ifdef debug
	system("@pause");
#endif
	return 0;
}
