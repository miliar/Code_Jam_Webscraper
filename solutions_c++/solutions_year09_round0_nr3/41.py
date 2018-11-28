#define INPUT "D:\\code\\gcj09\\C-large.in"
#define OUTPUT INPUT ".out.txt"

#include <vector>
#include <string>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdio>

using namespace std;
int GI() { int t; scanf("%d", &t); return t; }

string S = "welcome to code jam";
string In;
const int Mod = (int)1e4;

int seen[512][32], seenid;
int dp[512][32];

int go (int I, int i)
{
	if (i == S.size()) return 1;
	if (I >= In.size()) return 0;
	
	int &ret = dp[I][i];
	if (seen[I][i] == seenid) return ret; 
	seen[I][i] = seenid;

	ret = go (I + 1, i);
	if (In[I] == S[i])
	{
		ret += go (I + 1, i + 1);
	}

	return ret %= Mod;
}

int main()
{
	assert (freopen(INPUT, "r", stdin));
	assert (freopen(OUTPUT, "w", stdout));
	for (int T = GI(), k = 1; k  <= T; ++ k)
	{
		cout << "Case #" << k << ": " ;
		char buff[10000];
		if (k == 1) getchar();
		gets(buff);
		In = buff;
		seenid ++;
		printf ("%04d\n", go(0,0));
	}
	return 0;
}