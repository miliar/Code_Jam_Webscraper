#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }

const int maxn = 1000;

int to[26][26];
int opposed[26];
int elements[maxn], celements;
int exist[26];
int mask;

void clear()
{
	mask = 0;
	memset(exist, 0, sizeof exist);
	celements = 0;
}

void push(int a)
{
	exist[a]++;
	if(exist[a] == 1)
		mask |= 1 << a;
	elements[celements++] = a;
}
int back()
{
	return elements[celements - 1];
}

void pop()
{
	int a = back();
	exist[a]--;
	if(exist[a] == 0)
		mask ^= 1 << a;
	celements--;
}

bool existOpposed(int a)
{
	return opposed[a] & mask;
}



void process(int a)
{
	if(celements == 0)
		push(a);
	else
	{
		int b = back();
		if(to[a][b] == -1)
		{
			if(existOpposed(a))
				clear();
			else
				push(a);
		} else
		{
			pop();
			push(to[a][b]);
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int z = 0; z < t; ++z)
	{
		int c, d, n;
		cin >> c;
		memset(to, -1, sizeof to);
		memset(opposed, 0, sizeof opposed);
		for(int i = 0; i < c; ++i)
		{
			string s; cin >> s;
			int a, b, c;
			a = s[0] - 'A';
			b = s[1] - 'A';
			c = s[2] - 'A';
			to[a][b] = c;
			to[b][a] = c;
		}

		cin >> d;
		for(int i = 0; i < d; ++i)
		{
			string s; cin >> s;
			int a = s[0] - 'A';
			int b = s[1] - 'A';
			opposed[a] |= 1 << b;
			opposed[b] |= 1 << a;
		}

		cin >> n;
		string s;
		cin >> s;
		clear();
		for(int i = 0; i < s.length(); ++i)
		{
			int a = s[i] - 'A';
			process(a);
		}

		cout << "Case #" << z + 1 << ": [";
		for(int i = 0; i < celements; ++i)
		{
			if(i) cout << ", ";
			cout << char(elements[i] + 'A');
		}
		cout << "]" << endl;

	}
	return 0;
}
#endif

