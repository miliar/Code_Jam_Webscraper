#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n,x[102][2], dp[102][102][102];
int next[2][102];

int calc(int ind, int a, int b)
{
	if(ind == n) return 0;
	if(dp[ind][a][b] != -1) return dp[ind][a][b];
	
	int ta, tb;
	
	if(next[0][ind] > a) ta=1;
	else if(next[0][ind] == a || next[0][ind] == -1) ta=0;
	else ta=-1;
	
	if(next[1][ind] > b) tb=1;
	else if(next[1][ind] == b || next[1][ind] == -1) tb=0;
	else tb=-1;
	
	if(x[ind][1] == 0 && x[ind][0] == a) ++ind;
	else if(x[ind][1] == 1 && x[ind][0] == b) ++ind;
	
	return dp[ind][a][b] = calc(ind, a+ta, b+tb)+1;
}

int main()
{
	int T,t,k,i;
	char c,ch;
	
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1; t<=T; ++t) {
		scanf("%d%c",&n,&ch);
		
		for(i=0;i<n;++i) {
			scanf("%c %d%c",&c,&x[i][0],&ch);
			
			x[i][0]--;
			if(c == 'O') x[i][1] = 0;
			else if(c == 'B') x[i][1] = 1;
			else printf("BUG\n");
		}
		
		next[0][100] = next[1][100] = -1;
		
		for(i=99; i>=0; --i) {
			next[0][i] = next[0][i+1];
			next[1][i] = next[1][i+1];
			
			next[x[i][1]][i] = x[i][0];
		}
		
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",t,calc(0,0,0));
	}
}


