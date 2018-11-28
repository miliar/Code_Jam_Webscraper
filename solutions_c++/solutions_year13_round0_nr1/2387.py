#pragma warning(disable: 4996)
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>
#include <exception>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define fori(i,n) for (int i = 0; i < (n); ++ i)
#define forv(i,v) for (int i = 0; i < (sz(v)); ++ i)
typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	if (s == "input_txt")
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	else if (sz(s) != 0)
	{
		freopen((s + ".in").c_str(),"r",stdin);
		freopen((s + ".out").c_str(),"w",stdout);
	}
	
#endif
}
	

void read(vector< string > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(s.substr(1, sz(s) - 2));
		cin >> s;
	}
}
void read(string &s)
{
	cin >> s;
	s = s.substr(1, sz(s) - 2);
}

void read(vector< int > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(atoi(s.c_str()));
		cin >> s;
	}
}

bool win(vector<string> &s, char c)
{
	int n = 4;
	//hor
	for (int i = 0; i < n; ++ i)
	{
		bool T_T = false;
		for (int j = 0; j < n; ++ j)
			if (s[i][j] != c && s[i][j] != 'T')
				T_T = true;
		if (!T_T)
			return true;
	}

	//ver
	for (int j = 0; j < n; ++ j)
	{
		bool T_T = false;
		for (int i = 0; i < n; ++ i)
			if (s[i][j] != c && s[i][j] != 'T')
				T_T = true;
		if (!T_T)
			return true;
	}

	//diag
	bool T_T = false;
	for (int i = 0; i < n; ++ i)
		if (s[i][i] != c && s[i][i] != 'T')
			T_T = true;
	if (!T_T)
		return true;
	T_T = false;
	for (int i = 0; i < n; ++ i)
		if (s[i][n - i - 1] != c && s[i][n - i - 1] != 'T')
			T_T = true;
	return !T_T;
}

bool solve()
{
	int n = 4;
	vector<string> s(4);

	for (int i = 0; i < n; ++ i)
		cin >> s[i];

	int canDrow = true;

	for (int i = 0; i < n; ++ i)
	{
		for (int j = 0; j < n; ++ j)
			if (s[i][j] == '.')
				canDrow = false;
	}
	if (win(s, 'X'))
	{
		cout << "X won";
	}
	else if (win(s, 'O'))
		cout << "O won";
	else if (canDrow)
		cout << "Draw";
	else
		cout << "Game has not completed";

	return false;
}

int main()
{
	prepare("input_txt");
	int T;
	cin >> T;
	int id = 0;
	while (T--)
	{
		cout << "Case #" << ++ id << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
