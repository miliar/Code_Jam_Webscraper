#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

char comb[128][128];
bool op[128][128];
bool base[128];

void solve(int tc)
{
	printf("Case #%d: ", tc);
	int n, c, d;
	cin >> c;

	memset(comb, 255, sizeof(comb));
	memset(op, 0, sizeof(op));

	forn(i, c)
	{
		string s;
		cin >> s;

		comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
	}

	cin >> d;
	forn(i, d)
	{	
		string s;
		cin >> s;
		op[s[0]][s[1]] = op[s[1]][s[0]] = true;
	}

	string t;

	cin >> n;
    cin >> t;

	vector<char> v;

	forv(i, t)
	{
		if (!v.empty() && comb[v.back()][t[i]] != -1)
		{
			char c = comb[v.back()][t[i]];
			v.pop_back();
			v.push_back(c);
		}	
		else
		{	
			v.push_back(t[i]);
			forv(j, v)
			{
				if (op[v[j]][v.back()])
				{
					v.clear();
					break;
				}	
			}	
		}
	}
	
	printf("[");

	forv(i, v)
	{
		if (i) printf(", ");
		printf("%c", v[i]);
	}

	printf("]\n");

}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    string bs = "QWERASDF";

    forv(i, bs) base[bs[i]] = true;

    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);

    return 0;
}
            
