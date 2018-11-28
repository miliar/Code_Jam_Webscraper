#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include <cmath>
#include <cassert>
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

#define all(s) s.begin(), s.end()

const int INF = 1000000000;

int p, q;
vi pri;

int dyn[100][100];

int rec (int l, int r)
{
	if (dyn[l][r] != -1)
		return dyn[l][r];

	int best = INF;

	if (l > r)
		return 0;

	for (int i = l; i <= r ; i++)
	{
		int left = l ? pri[l - 1] + 1 : 0;
		int right = r < q - 1 ? pri[r + 1] - 1 : p - 1;

		int c = right - left;

		c += rec (l, i - 1);
		c += rec (i + 1, r);

		best = min(best, c);
	}

	return dyn[l][r] = best;
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;



	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

		string s;
//		getline(cin, s);
//		cin >> s;

		
		cin >> p >> q;
		
		memset (dyn, 255, sizeof dyn);
		pri.assign(q, 0);
		for (int i = 0; i < q ; i++)
		{
			cin >> pri[i];
			pri[i]--;
		}

		int res = rec(0, q - 1);

		printf("Case #%d: %d\n", test + 1, res);
	}

}