#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

typedef long double ld;
typedef long long ll;
const double pi = M_PI;

const int NMAX = 23;
const int SMAX = 220;
const int SH = SMAX / 2;
char a[NMAX][NMAX];
int v[NMAX][NMAX];
string d[NMAX][NMAX][SMAX];
const int MAGIC = 60;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

int n;

bool valid(int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < n;
}


bool Less(const string& a, const string& b)
{
	if (a.length() != b.length()) return a.length() < b.length();
	return a < b;
}

void solve(int tc)
{
	printf("Case #%d:\n", tc);
	int q;
	scanf("%d %d\n", &n, &q);
	forn(i, n)
	{
		forn(j, n)
		{
			scanf("%c", &a[i][j]);
			if (isdigit(a[i][j])) v[i][j] = a[i][j] - '0';
		}
		scanf("\n");
	}
	forn(i, NMAX) forn(j, NMAX) forn(k, SMAX) d[i][j][k] = "";
	forn(i, n)
	{
		forn(j, n)
		{
			if (!isdigit(a[i][j])) continue;
			d[i][j][v[i][j] + SH] += a[i][j];
 		}
	}

	string t;

	forn(it, MAGIC)
	{
		forn(i, n)	
		{
			forn(j, n)
			{
				if (!isdigit(a[i][j])) continue;
				forn(k, SMAX) 
				{
					if (d[i][j][k].length() == 0) continue;
					forn(i1, 4)
					{

						int x = i + dx[i1];
						int y = j + dy[i1];
						if (!valid(x, y)) continue;
						char op1 = a[x][y];
						///assert(!isdigit(a[x][y]));
						t.pb(op1);
						forn(i2, 4)
						{
							int xx = x + dx[i2];
							int yy = y + dy[i2];
							if (!valid(xx, yy)) continue;
							//assert(isdigit(a[xx][yy]));
							t.pb(a[xx][yy]);
							int s = k;
							if (op1 == '+') s += v[xx][yy];
							else s -= v[xx][yy];
							if (s < 0 || s >= SMAX)
							{
								t.erase(t.size()-1, 1);
								continue;
							}
							if (d[xx][yy][s].length() == 0) 
					        {
								d[xx][yy][s] = t;
								t.erase(t.size()-1, 1);
								continue;
							}
							if (d[xx][yy][s].length() < t.length()) 
							{
								t.erase(t.size()-1, 1);
								continue;
							}
							if (d[xx][yy][s].length() > t.length())
							{
								d[xx][yy][s] = t;
								t.erase(t.size()-1, 1);
								continue;
							}
							if (d[xx][yy][s] > t) d[xx][yy][s] = t;
							t.erase(t.size()-1, 1);
						}
						t.erase(t.size()-1, 1);
					}
				}
			}
		}
	}

	forn(it, q)
	{
		int val;
		scanf("%d", &val);
		val += SH;
		int i0 = -1, j0;
		forn(i, n)
		{
			forn(j, n)
			{
				if (d[i][j][val].length())
				{
					if (i0 == -1 || (Less(d[i][j][val], d[i0][j0][val])))
					{
						i0 = i;
						j0 = j;
					}
				}
			}
		}
		assert(i0 >= 0);
		puts(d[i0][j0][val].c_str());
	}
}



int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tc;
	cin >> tc;
	forn(it, tc) solve(it+1);

	return 0;
}