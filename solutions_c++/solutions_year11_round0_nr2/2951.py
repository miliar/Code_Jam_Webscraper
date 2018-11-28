#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <numeric>

#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define EPS 1e-9
#define INF INT_MAX
#define SQR(X) (X) * (X)
#define round(x) (int)floor((x) + 0.5 + EPS)

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long LL;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <uint> vu;
typedef vector <ull> vull;
typedef vector <pii> vpii;
typedef vector <vpii> vvpii;
typedef vector <string> vs;
typedef pair<char, char> pcc;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++)
	{
		printf("Case #%d: [", z);	
		map<pcc, char> f;
		char op[500];
		memset(op, 0, sizeof(op));
		int c;
		cin >> c;
		for (int i = 0; i < c; i++)
		{
			string t;
			cin >> t;
			f[pcc(t[0], t[1])] = t[2];
			f[pcc(t[1], t[0])] = t[2];
		}
		cin >> c;
		for (int i = 0; i < c; i++)
		{
			string t;
			cin >> t;
			op[t[0]] = t[1];
			op[t[1]] = t[0];
		}
		vector<char> lst;
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			char t;
			cin >> t;
			lst.push_back(t);
			if (sz(lst) < 2) continue;
			if (f.find(pcc(lst[sz(lst) - 1], lst[sz(lst) - 2])) != f.end())
			{
				char r = f[pcc(lst[sz(lst) - 1], lst[sz(lst) - 2])];
				lst.pop_back();
				lst.pop_back();
				lst.push_back(r);

			}
			else for (int j = 0; j < sz(lst); j++)
				if (op[lst[j]] == lst[sz(lst) - 1]) lst.clear(); 
		}
		for (int i = 0; i < sz(lst); i++)
		{
			if (i != 0) printf(", ");
			printf("%c", lst[i]);
		}
		printf("]\n");
	}
	return 0;
}