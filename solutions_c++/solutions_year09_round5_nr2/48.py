#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector <string> S;
string P;
int K, n;

const int modulo = 10009;

void load()
{
	cin >> P;
	cin >> K;

	cin >> n;
	S.resize(n);

	for (int i = 0; i < n; ++i) cin >> S[i];
}

int value(string &tmp)
{
	int znakovi[26] = {0};

	for (int i = 0; i < tmp.size(); ++i)
	{
		znakovi[tmp[i]-'a']++;
	}

	int sol = 0, t = 1;

	for (int i = 0; i < P.size(); ++i)
	{
		if (P[i] >= 'a' && P[i] <= 'z') t = (t * znakovi[P[i]-'a']) % modulo;
		else { sol = (sol + t) % modulo; t = 1; }
	}

	sol = (sol + t) % modulo;

	return sol;
}

void rek(int k, string tmp, vector <int>& sol)
{
	sol[k] = (sol[k]+value(tmp)) % modulo;

	if (k == 0) return;

	for (int i = 0; i < n; ++i)
	{
		rek(k-1, tmp+S[i], sol);
	}
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; ++tt)
	{
		load();

		cout << "Case #" << tt << ": ";

		vector <int> sol(K+1, 0);
		rek(K, "", sol);

		for (int i = K-1; i >= 0; --i) cout << sol[i] << ' ';

		cout << endl;
	}

	return 0;
}
