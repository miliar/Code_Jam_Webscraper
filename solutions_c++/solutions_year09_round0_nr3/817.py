/*
Language: c++
*/

#include<stdio.h>
#include<string.h>

const long w = 19;
char wel[25]={" welcome to code jam"};
char str[600];
long L[25][600];

long solve(void)
{
	long i, j, n;
	gets(str);
	n = strlen(str);
	if(n<w) return 0;
	for(i=0; i<n; i++) L[0][i] = 1;
	for(i=1; i<=w; i++){
		for(j=0; j<i-1; j++)
			L[i][j] = 0;
		for(j=0; j<i; j++)
			if(str[j]!=wel[j+1]) break;
		if(j<i) L[i][i-1] = 0;
		else L[i][i-1] = 1;
		for(j=i; j<n; j++){
			if(str[j]==wel[i])
				L[i][j] = (L[i-1][j-1] + L[i][j-1])%10000;
			else L[i][j] = L[i][j-1]%10000;
		}
	}
	return L[w][n-1];
}

int main()
{
	long t, i;
	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d", &t);
	getchar();
	for(i=1; i<=t; i++)
		printf("Case #%d: %04d\n", i, solve());
	return 0;
}

