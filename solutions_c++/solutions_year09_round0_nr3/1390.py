#include <string>
#include <cstring>
#include <iostream>
#include <cstdio>

#define MOD 10000

using namespace std;

int memo[510][30];

string key = "welcome to code jam";
string str;
char st[600];
int solve(int,int);

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.txt", "w", stdout);
	int n, tc, i;
	scanf("%d ", &n);
	for(tc = 1; tc <= n; ++tc)
	{
		gets(st);
		str = st;
		memset(memo, -1, sizeof(memo));
		int ans = solve(0, 0) % MOD;
		printf("Case #%d: %04d\n", tc, ans);
	}
	
	return 0;
}
int solve(int pos, int cur)
{

	if(cur >= key.size())
	{
		//printf("%d\n", pos);
		return 1;
	}
	if(pos >= (int) str.size())
	{
		return 0;		
	}
	//char ch = key[cur] - 'a';

	if(memo[pos][cur] != -1)  return memo[pos][cur];
	
	int i;
	
	int toret = 0;
	for(i = pos; i < (int)str.size(); ++i)
	{
		//toret = solve(i + 1, cur );
		if(str[i] == key[cur]) toret += solve(i+1, cur+1);
		toret %= MOD;
	}
	memo[pos][cur] = toret;
	return toret;
}




