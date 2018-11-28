#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef vector<string> VS;
typedef vector<int>	VI;
typedef vector<VI>	VVI;
typedef pair<int,int>	PII;
typedef vector<PII>	VPII;
typedef vector<VPII>	VVPII;

const int MOD = 10009;
int dp[16][128];

VI mult(int f, VI v)
{
	for (int i = 0; i < v.size(); i++)
		v[i] *= f;
	return v;
}

int eval(const VI &val, const VPII &term)
{
	int res = 1;
	for (int i = 0; i < term.size(); i++)
		for (int j = 0; j < term[i].second; j++)
			res = (res * val[term[i].first]) % MOD;
	return res;
}

VVI words;
VVPII terms;

int solve(int d, const VI &val)
{
	if (d == 0)
	{
		int res = 0;
		for (int i = 0; i < terms.size(); i++)
			res = (res + eval(val, terms[i])) % MOD;
		return res;
	}
	else
	{
		int res = 0;
		for (int i = 0; i < words.size(); i++)
		{
			VI nval(val);
			for (int j = 0; j < 26; j++)
				nval[j] += words[i][j];
			res = (res + solve(d-1, nval)) % MOD;
		}
		return res;
	}
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int K, N;
		string pol, term;
		terms.clear();
		words.clear();
		cin >> pol >> K >> N;
		stringstream buf(pol);
		while (getline(buf, term, '+'))
		{
			VI w(26, 0);
			for (int i = 0; i < term.size(); i++)
				w[term[i]-'a']++;
			VPII t;
			for (int i = 0; i < w.size(); i++)
				if (w[i])
					t.push_back(PII(i, w[i]));
			terms.push_back(t);
		}

		for (int i = 0; i < N; i++)
		{
			cin >> term;
			VI w(26, 0);
			for (int i = 0; i < term.size(); i++)
				w[term[i]-'a']++;
			words.push_back(w);
		}

		cout << "Case #" << kase << ":";
		for (int d = 1; d <= K; d++)
			cout << " " << solve(d, VI(26, 0));
		cout << endl;
	}
	return 0;
}
