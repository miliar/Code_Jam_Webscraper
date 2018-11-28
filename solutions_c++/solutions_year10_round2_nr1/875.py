#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sz(a) a.size()
#define For(i, a, b) for(int i = a; i < b; i++)
#define Ror(i, a, b) for(int i = a - 1; i >= b; i--)

typedef pair<int, int> pii;
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int Size = 10000;
char buffer[Size];

const int inf = 0x0fffffff;
const int white = 0, gray = 1, black = 2;

const double eps = 10e-6;

vector<string> Split(string s)
{
	int l = 1;
	vector<string> res;
	For(i, 1, s.size())
	{
		if(s[i] == '/')
		{
			res.pb(s.substr(l, i - l));
			l = i + 1;
		}
	}
	res.pb(s.substr(l, s.size() - l));
	return res;
}

map<string, int> t[10000];
int top = 1;

int res;

void AddNode(int k, vector<string> v)
{
	if(v.size() == 0)
		return;
	string n = v.back();
	if(t[k].count(n))
	{
		v.pop_back();
		AddNode(t[k][n], v);
	}
	else
	{
		v.pop_back();
		t[k][n] = top++;
		AddNode(t[k][n], v);
	}
}

void AddNodeEx(int k, vector<string> v)
{
	if(v.size() == 0)
		return;
	string n = v.back();
	if(t[k].count(n))
	{
		v.pop_back();
		AddNodeEx(t[k][n], v);
	}
	else
	{
		v.pop_back();
		t[k][n] = top++;
		res++;
		AddNodeEx(t[k][n], v);
	}
}

int Solution(int nTest)
{
	int n, m;
	scanf("%d%d", &n, &m);
	gets(buffer);
	top = 1;
	For(i, 0, 10000)
		t[i].clear();
	For(i, 0, n)
	{
		gets(buffer);
		string s = buffer;
		vector<string> k = Split(s);
		reverse(all(k));
		AddNode(0, k);
	}

	vector<vector<string> > want;
	For(i, 0, m)
	{
		gets(buffer);
		string s = buffer;
		vector<string> k = Split(s);
		reverse(all(k));
		want.pb(k);
	}
	sort(all(want));
	res = 0;
	For(i, 0, m)
	{
		AddNodeEx(0, want[i]);
	}
	printf("Case #%d: ", nTest + 1);
	printf("%d\n", res);


	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 9999;
	scanf("%d", &n);
	while(i < n && Solution(i))
		i++;

	return 0;
}