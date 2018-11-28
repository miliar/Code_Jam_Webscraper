#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int infinity = 1<<20;
typedef vector<int> vint;

bool inline isProperSubset(int s, int S) { return (s != S) && ( (s&S) == s); }
bool inline hasBit(int v, int i) { return v & (1<<i); }
int inline nextSubset(int i, int super) { return (i-1) & super; }

bool compat[32][32];

bool allCompatible(int set)
{
	vint idx;

	for (int c = 0; c < 16; ++c)
		if (hasBit(set, c))
			idx.push_back(c);

	for (int j = 0; j < idx.size(); ++j)
	for (int k = j+1; k < idx.size(); ++k)
		if (!compat[idx[j]][idx[k]]) return false;

	return true;
}

int memo[1<<17];
int minDiag(int set)
{
	if (set == 0) return 0;
	if (memo[set] != -1) return memo[set];
	if (allCompatible(set)) return memo[set] = 1;

	int best = infinity;

	int sub = nextSubset(set, set);

	for (int s = sub; s > 0; s = nextSubset(s, sub))
		best = min(best, minDiag(s) + minDiag(set ^ s) );

	return memo[set] = best;
}

bool isCompatible(const vint &a, const vint &b)
{
	if (a[0] == b[0]) return false;

	bool cmp = a[0] < b[0];

	for (int c = 1; c < a.size(); ++c)
		if (a[c] == b[c] || (a[c] < b[c]) != cmp ) return false;

	return true;
}

int main()
{
	int tc;
	cin >> tc;
	for (int casecnt = 1; casecnt <= tc; ++casecnt)
	{
		cout << "Case #" << casecnt << ": ";
		int nStck, nT;
		cin >> nStck >> nT;

		vector<vint> data;

		for (int s = 0; s < nStck; ++s)
		{
			vint stckDat;
			for (int t = 0; t < nT; ++t)
			{
				int price;
				cin >> price;

				stckDat.push_back(price);
			}

			data.push_back(stckDat);
		}

		for (int j = 0; j < data.size(); ++j)
		for (int k = j; k < data.size(); ++k)
			compat[j][k] = compat[k][j] = isCompatible( data[j], data[k] );

		int msk = (1<<data.size()) - 1;

		for (int c = 0; c <= msk; ++c)
			memo[c] = -1;

		cout << minDiag( msk ) << endl;
	}

	return 0;
}
