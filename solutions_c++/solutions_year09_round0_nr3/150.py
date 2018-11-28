#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

struct modint
{
	int k;

	modint(int n) : k(n%10000) {}

	modint operator+(modint r) { return modint(k+r.k); }
	operator int() { return k; }
};

string B, S("welcome to code jam");

int memo[512][32];
void resetmemo()
{
	for (int x = 0; x < B.size(); ++x)
	for (int y = 0; y < B.size(); ++y)
		memo[x][y] = -1;
}

modint count(int b, int s)
{
	if (s == S.size()) return 1;
	if (b == B.size()) return 0;

	if (memo[b][s] != -1) return memo[b][s];

	modint ret = count(b+1,s);
	if (B[b] == S[s]) ret = ret + count(b+1, s+1);

	return (memo[b][s] = ret);
}

int main()
{
	int n;
	cin >> n;
	cin.ignore(1);
	for (int cc = 1; cc <= n; ++cc)
	{
		getline(cin, B);

		resetmemo();
		printf("Case #%d: %04d\n", cc, count(0,0).k);
	}
	return 0;
}

