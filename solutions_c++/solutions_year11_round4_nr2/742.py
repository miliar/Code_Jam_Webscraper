#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <set>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>

#define MAXR 501
#define MAXC 501

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) (x).begin(), (x).end()
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

long long R, C, D, M[MAXR][MAXC];

bool check(long long r, long long c, long long K)
{
	long long i, j;
	long long totalR = 0, totalC = 0;
	if ((r < K) || (r >= R-K) || (c < K) || (c >= R-K))
		return false;
	for (i = -K; i <= K; ++i)
	{
		for (j = -K; j <= K; ++j)
		{
			if ((i == K) && (j == K))
				continue;
			if ((i == K) && (j == -K))
				continue;
			if ((i == -K) && (j == K))
				continue;
			if ((i == -K) && (j == -K))
				continue;
			totalR += i*(M[r+i][c+j]+D);
			totalC += j*(M[r+i][c+j]+D);
		}
	}
	return (totalR == 0) && (totalC == 0);
}

bool check2(long long r, long long c, long long K)
{
	long long i, j;
	double totalR = 0, totalC = 0;
	if ((r < K-1) || (r >= R-K) || (c < K-1) || (c >= R-K))
		return false;
	for (i = -K+1; i <= K; ++i)
	{
		for (j = -K+1; j <= K; ++j)
		{
			if ((i == K) && (j == K))
				continue;
			if ((i == K) && (j == -K+1))
				continue;
			if ((i == -K+1) && (j == K))
				continue;
			if ((i == -K+1) && (j == -K+1))
				continue;
			totalR += (i-0.5)*(M[r+i][c+j]+D);
			totalC += (j-0.5)*(M[r+i][c+j]+D);
		}
	}
	return (totalR == 0) && (totalC == 0);
}

int main()
{
	long long t, T, r, c, k;
	string line;
	cin >> T;
	for (t = 0; t < T; ++t)
	{
		cout << "Case #" << t+1 << ": ";
		cin >> R >> C >> D;
		for (r = 0; r < R; ++r)
		{
			cin >> line;
			for (c = 0; c < C; ++c)
			{
				M[r][c] = line[c]-'0';				
			}
		}
		long long maxk = 0;
		for (r = 1; r < R; ++r)
		{
			for (c = 1; c < C; ++c)
			{
				for (k = 1; k <= r; ++k)
					if (check(r, c, k) && (k > maxk))
						maxk = k;
			}
		}
		int maxk2 = 0;
		for (r = 0; r < R; ++r)
		{
			for (c = 0; c < C; ++c)
			{
				for (k = 1; k <= r+1; ++k)
					if (check2(r, c, k) && (k > maxk2))
						maxk2 = k;
			}
		}
		if (maxk2 == 1)
			maxk2 = 0;
		int rmaxk = 2*maxk+1;
		if (2*maxk2 > 2*maxk+1)
			rmaxk = 2*maxk2;
		if (rmaxk == 1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << rmaxk << endl;
	}

    return 0;
}
