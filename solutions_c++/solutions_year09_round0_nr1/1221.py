#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-9; 
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;


int L, D, N;
VS words;
char was[256][256];
void main()
{
#ifndef _DEBUG
	const string file_name = "A-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	cin >> L >> D >> N;
	for (int i = 0; i < D; i++)
	{
		string s;
		cin >> s;
		words.push_back(s);
	}
	
	char ggg = 0;
	memset(was, ggg, sizeof(was));
	for (int jj = 1; jj <= N; jj++)
	{
		ggg++;
		string s;
		cin >> s;
		int p = 0;
		for (int i = 0; i < L; i++)
		{
			if (s[p] == '(')
			{
				p++;
				while (s[p] != ')')
				{
					was[i][s[p]] = ggg;
					p++;
				}
			}
			else
			{
				was[i][s[p]] = ggg;
			}
			p++;
		}
		LL res = 0;
		for (int i = 0; i < D; i++)
		{
			bool ok = true;
			for (int j = 0; j < L; j++)
			{
				if (was[j][words[i][j]] != ggg)
				{
					ok = false;
					break;
				}
			}
			if (ok) res++;
		}
		cout << "Case #" << jj << ": " << res << '\n';
	}

}
