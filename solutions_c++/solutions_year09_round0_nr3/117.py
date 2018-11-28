# include <stdio.h>
# include <string.h>

using namespace std;
int pd[64][512];
char pal[64];
char pal2[512];
int solve(int i, int j){
	if(i==0) return pd[i][j] = 1;
	if(j==0) return pd[i][j] = 0;
	if(pd[i][j] != -1) return pd[i][j];
	if(pal[i-1] == pal2[j-1]) return pd[i][j] = (solve(i-1,j-1)%10000 + solve(i,j-1)%10000)%10000;
	else return pd[i][j] = solve(i,j-1);
}

int main (void){
	int n;
	int teste = 1;
	char s[512];
	strcpy(pal, "welcome to code jam");
	scanf("%d", &n);
	gets(s);
	while(n--){
		memset(pd, -1, sizeof(pd));
		gets(pal2);
		printf("Case #%d: %04d\n", teste++, solve(strlen(pal), strlen(pal2)));
	}
	return 0;
}