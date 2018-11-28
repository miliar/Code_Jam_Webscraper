#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;
#define MOD 10000
char Wel[25] = "welcome to code jam";
int opt[25][510];
char st[1000];
int solve(){
	gets(st);
	int len = strlen(st);
	memset(opt, 0, sizeof(opt));
	int i, j, k;
	
	for (i = 0; i < len; i++)
		if (st[i] == Wel[0]) opt[0][i] = 1;
	
	for (k = 0; k < 18; k++)
	for (i = 0; i < len; i++)
	if (opt[k][i] > 0 ) 
		for (j = i+1; j < len; j++)
		if (st[j] == Wel[k+1]) {
			opt[k+1][j] += opt[k][i];
			if (opt[k+1][j] >= MOD)  
				opt[k+1][j] %= MOD;
		}
		
	int ans = 0;
	for (i = 0; i <= len; i++)
		ans = (ans + opt[18][i]) % MOD;
	return ans;
}
int main(){
	int ca, Case;
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	scanf("%d\n", &Case);
	for (int ca = 1; ca <= Case; ca++) 
		printf("Case #%d: %04d\n", ca, solve());
	//while (1);
	return 0;
}
