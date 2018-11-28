#include <iostream>
#include <cstring>
#include <string>
using namespace std;
const int MOD = 10000;
int memo[5005][20];

string x = "welcome to code jam", L;

int solve(int p, int idx)
{
	if (p == L.size())
		return (idx == x.size());
	int &rez = memo[p][idx];
	if (rez != -1) return rez;
	rez = solve(p + 1, idx) % MOD;	
	if (x[idx] == L[p]) rez = (rez + solve(p + 1, idx + 1) % MOD) % MOD;
	return rez;
}


int main()
{
	char line[550];
	int n;
	
	int t;
	freopen("f:/cinp.txt", "r", stdin);
	freopen("f:/co.txt", "w", stdout);
	
	
	gets(line);
	n = atoi(line);
	for (int T = 1; T <= n; ++T)
	{
		gets(line);
		L = line;
		memset(memo, -1, sizeof memo);
		cout << "Case #" << T << ": ";
		printf("%.4d\n",solve(0, 0));
		
	}
}
