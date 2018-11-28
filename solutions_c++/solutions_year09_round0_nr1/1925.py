#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <list>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define All(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef vector<vector<int> > vvi;

const int inf = 0x0ffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 10000;
char buffer[Size];

int l, d, n;

int sum;

vector<vector<int> > token;
vector<string> dict;


int Solution(int nTest)
{
	gets(buffer);
	string s = buffer;
	vector<char> temp;
	bool open = 0;
	sum = 0;
	token.clear();
	bool flag = 1;
	token.resize(l, vector<int> (254));
	int j = 0;
	for(int i = 0; i < s.size(); i++)
	{
		if(s[i] == '(')
		{
			open = 1;
			continue;
		}
		else
		if(s[i] == ')')
		{
			j++;
			open = 0;
		}
		else
		if(open)
		{
			token[j][s[i]] = 1;
		}
		else
		{
			token[j][s[i]] = 1;
			j++;
		}
	}

	for(int i = 0; i < d; i++)
	{
		string s = dict[i];
		int j;
		for(j = 0; j < s.size(); j++)
			if(token[j][s[j]] == 0)
				break;
		if(j == s.size())
			sum++;
	}
			

	printf("Case #%d: %d\n", nTest + 1, sum);
	
	return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	scanf("%d%d%d", &l, &d, &n);
	gets(buffer);

	for(int i = 0; i < d; i++)
	{
		gets(buffer);
		string s = buffer;
		dict.pb(s);
	}

	for(int i = 0; i < n; i++) Solution(i);

//	while(Solution(n));

	return 0;
}

