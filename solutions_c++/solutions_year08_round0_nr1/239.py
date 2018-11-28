#include <iostream>
#include <cstdio>
#include <string>

using namespace std;


int Q, S;
string query[1010], engine[110];

int ans[1010];


void Load()
{
	cin >> S;
	int i;
	char c;
//	cin >> c;
	getline(cin, engine[0], '\n');
	for (i = 0; i < S; i++)
	{
		getline(cin, engine[i], '\n');
		cerr << engine[i] << "\n";
	}

	cin >> Q;
	getline(cin, query[0], '\n');

	cerr << S << " engines\n";

	for (i = 0; i < Q; i++)
	{
		getline(cin, query[i], '\n');
		cerr << query[i] << "\n";
	}

	cerr << Q << " queries\n";

}

void Solve()
{
	memset(ans, 0, sizeof(ans));
	int i, j, mi, bn;
	for (j = 0; j < Q; j++)
	{
		bn = mi = -1;
		for (i = 0; i < S; i++)
		{
			if (engine[i] != query[j])
			{
				if (mi == -1 || ans[mi] > ans[i]) mi = i;
			}
			else 
				bn = i;
		}
		mi = ans[mi]+1;
		for (i = 0; i < S; i++)
		{
			if (i == bn || ans[i] > mi)
				ans[i] = mi;
//			cerr << ans[i] << " ";
		}
//		cerr << "\n";
	}
	mi = 0;
	for (i = 1; i < S; i++)
	{
		if (ans[i] < ans[mi]) mi = i;
	}
	cout << ans[mi] << "\n";
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt;
	cin >> nt;
	for (int tt = 1; tt <= nt; tt++)
	{
		cerr << "testcase " << tt << "\n";
		cout << "Case #" << tt << ": ";
		Load();
		Solve();
	}
	return 0;

}