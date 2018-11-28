#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }

char who_wins(const string &s)
{
	int cX = 0, cO = 0, cT = 0;
	for(int i = 0; i < s.size(); ++i)
		if(s[i] == 'X') cX++;
		else if(s[i] == 'O') cO++;
		else if(s[i] == 'T') cT++;
	if(cX + cT == 4)
		return 'X';
	else if(cO + cT == 4)
		return 'O';
	else
		return 0;
}

void solve(int test)
{
	const int n = 4;
	vector<string> a(n);
	for(int i = 0; i < n; ++i)
		cin >> a[i];

	bool empty_cell = false;
	for(int i = 0; i < n; ++i)
		empty_cell |= count(a[i].begin(), a[i].end(), '.') > 0;

	char win = 0;

	vector<string> to_check(2 * n + 2);

	for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j)
		{
			to_check[i] += a[i][j];
			to_check[n + i] += a[j][i];
			if(i == j)
				to_check[2 * n] += a[i][j];
			if(i == n - j - 1)
				to_check[2 * n + 1] += a[i][j];
		}
	
	for(int i = 0; i < to_check.size(); ++i)
		if(char ch = who_wins(to_check[i]))
		{
			assert(win == 0 || win == ch);
			win = ch;
		}

	if(win)
		cout << T(test) << " " << win << " won" << endl;
	else if(!empty_cell)
		cout << T(test) << " Draw" << endl;
	else
		cout << T(test) << " Game has not completed" << endl;
	
}

int main()
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test)
		solve(test);

	return 0;
}
/*************************
*************************/
#endif
