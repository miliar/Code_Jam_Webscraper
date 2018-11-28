#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

int MOD = 10009;

string name = "b";
string attempt = "0";
int test;

int W, K;
string w[100];

vector<int> calc(string poly)
{
	vector<int> res(K);

	int n = (int)poly.length();
	map<vi, int> cr, nx;
	vi state(n, 0);
	nx[state] = 1;

	vector<vi> step(W);
	for (int i = 0; i < W; i++)
	{
		vi state(n);
		for (int k = 0; k < n; k++)
			for (int j = 0; j < (int)w[i].length(); j++)
				if (poly[k] == w[i][j]) state[k]++;

		step[i] = state;
	}

	for (int i = 0; i < K; i++)
	{
		cr = nx;
		nx.clear();

		for (map<vi, int>::iterator it = cr.begin(); it != cr.end(); it++)
		{
			vi state = it->first;
			for (int wi = 0; wi < W; wi++)
			{
				for (int k = 0; k < n; k++) state[k] += step[wi][k];
				nx[state] = (nx[state] + it->second) % MOD;
				for (int k = 0; k < n; k++) state[k] -= step[wi][k];
			}
		}

		for (map<vi, int>::iterator it = nx.begin(); it != nx.end(); it++)
		{
			vi state = it->first;
			int val = 1;
			for (int k = 0; k < n; k++) val = (val * state[k]) % MOD;
			res[i] = (res[i] + val * it->second) % MOD;
		}
	}

	return res;
}

void solve()
{
	string poly;
	cin >> poly >> K >> W;
	for (int i = 0; i < W; i++) cin >> w[i];
	
	for (int i = 0; i < poly.length(); i++)
	{
		if (poly[i] == '+') poly[i] = ' ';
	}

	stringstream str(poly);
	
	vector<int> R(K);

	while (str >> poly)
	{
		vector<int> C = calc(poly);
		for (int i = 0; i < (int)C.size(); i++)
			R[i] = (R[i] + C[i]) % MOD;
	}

	cout << "Case #" << ++test << ":";
	for (int i = 0; i < R.size(); i++)
		cout << ' ' << R[i];
	cout << endl;
	cerr << "Case #" << test << ": " << endl;
}

int main()
{
	string fin;
	string fout;
	if (true)
	{
		fin = name + "-small-attempt" + attempt + ".in";
		fout = name + "-small-attempt" + attempt + ".out";
	}
	else
	{
		fin = name + "-large.in";
		fout = name = "-large.out";
	}
	freopen(fin.c_str(), "r", stdin);
	freopen(fout.c_str(), "w", stdout);
	int t;
	cin >> t;
	while (t--) solve();
	fclose(stdout);
	return 0;
}