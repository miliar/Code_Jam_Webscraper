#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <utility>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

const double pi = 2*acos(0.0);

char picture[52][52];

bool CanPut(int f, int c)
{
	picture[f][c] = '/';
	if (picture[f][c+1] == '#')
	{
		picture[f][c+1] = '\\';
		if (picture[f+1][c] == '#')
		{
			picture[f+1][c] = '\\';
			if (picture[f+1][c+1] == '#')
			{
				picture[f+1][c+1] = '/';
				return true;
			}
			else
				return false;
		}
		else
			return false;
	}
	else
		return false;
}

int main() 
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T, R, C;
	char line[60];

	scanf("%d", &T);
	For(test, 1, T) 
	{
		scanf ("%d%d", &R, &C);
		Fill(picture, 0);

		Rep(f, R)
		{
			scanf ("%s", line);
			Rep (c, C)
			{
				picture [f][c] = line[c];
			}
		}

		int f = 0;
		int c = 0;
		bool ok = true;
		while ((f < R-1) && (ok))
		{
			c = 0;
			while (c < C-1)
			{
				if (picture[f][c] == '#')
				{
					ok = CanPut(f, c);
					if (!ok)
						break;
					else
						c += 2;
				}
				else
					c++;
			}
			f++;
		}
		// Verify last row
		Rep (c, C)
			if (picture[R-1][c] == '#')
			{
				ok = false;
				break;
			}
		// Verify last column
		Rep (f, R)
			if (picture[f][C-1] == '#')
			{
				ok = false;
				break;
			}

		if (ok)
		{
			printf("Case #%d:\n", test);
			Rep(f, R)
			{
				printf ("%s\n", picture[f]);
			}
		}
		else
			printf("Case #%d:\nImpossible\n", test);
	}

	fclose (stdin);
	fclose (stdout);

	exit(0);
}

