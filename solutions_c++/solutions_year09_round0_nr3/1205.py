#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_TAILLE = 500;

int nbTests;
char s[MAX_TAILLE + 100];
int tailleS;
int dp[MAX_TAILLE + 10][MAX_TAILLE + 10];
const char* orig = "welcome to code jam";
int tailleO;


int solve(int pos, int posO)
{
	if(posO == tailleO) return 1;
	if(pos == tailleS) return 0;
	
	if(dp[pos][posO] != -1)
		return dp[pos][posO];
		
	//printf("s : %d/%d (%c)\to: %d/%d (%c)\n", pos, tailleS, s[pos], posO, tailleO, orig[posO]);
	dp[pos][posO] = solve(pos+1, posO);
	
	if(s[pos] == orig[posO])
		dp[pos][posO] += solve(pos+1, posO+1);
	
	dp[pos][posO] = dp[pos][posO]  % 10000;
	return dp[pos][posO];
}

int main()
{
	tailleO = strlen(orig);
	scanf("%d\n", &nbTests);
	
	for(int c = 0; c < nbTests; c++)
	{
		memset(dp, -1, sizeof(dp));
		scanf(" %[^\n]s", s);
		//printf("%s\n", s);
		tailleS = strlen(s);
		printf("Case #%d: %04d\n", c+1, solve(0, 0));
	}
		
	return 0;
}
