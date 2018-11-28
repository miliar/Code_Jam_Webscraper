#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
using namespace std;
string s;
string patt = "welcome to code jam";;
int dp[1000][30];

void Load()
{
	s = "";
	int c = 0; while((c = getchar()) != 10 && c != EOF) s += c;	
}

int f(int i, int j)
{
	if (i > s.size()) return 0;
	if (i == s.size()) return j == patt.size();
	if (dp[i][j] != -1) return dp[i][j];
	dp[i][j] = 0;
	dp[i][j] %= 10000;
	dp[i][j] += f(i + 1, j);
	dp[i][j] %= 10000;
	if (j < patt.size() && s[i] == patt[j]) dp[i][j] += f(i + 1, j + 1);
	dp[i][j] %= 10000;
	return dp[i][j];
}

void Solve(int Test)
{
	memset(dp, 0xFF, sizeof(dp));
	printf("Case #%d: %04d\n", Test, f(0,0));
}


#define file "c"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	nextLine();
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}