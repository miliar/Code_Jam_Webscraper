
#include <iostream>
using namespace std;

#define S 100
#define Q 1000

string dummy;
int matches[Q][S];
int ns;
int nq;

void solve(int testcase)
{
	string engines[S];
	memset(matches, 0, sizeof(matches));

	cin >> ns;
	getline(cin, dummy);
	for (int i = 0; i < ns; i++)
		getline(cin, engines[i]);
	
	cin >> nq;
	getline(cin, dummy);
	for (int i = 0; i < nq; i++)
	{
		string query;
		getline(cin, query);
		for (int j = 0; j < ns; j++)
			if (query == engines[j])
				matches[i][j] = 2000;
	}

	for (int i = nq-2; i >= 0; i--)
		for (int j = 0; j < ns; j++)
			if (!matches[i][j])
			{
				matches[i][j] = 2000;
				for (int k = 0; k < ns; k++)
					matches[i][j] = min(matches[i][j], matches[i+1][k] + (j == k ? 0 : 1));
			}

	int mincost = 2000;
	for (int i = 0; i < ns; i++)
		mincost = min(mincost, matches[0][i]);

	printf("Case #%d: %d\n", testcase, mincost);
}

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		solve(i);
	
	return 0;
}

