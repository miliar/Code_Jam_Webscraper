#include<iostream>
#include<cstdio>
using namespace std;

int		i, j, n, N, L;

char	S[] = "welcome to code jam";
char	T[508];

int		f[508][20];

int		main(){
		//freopen("input.txt","r",stdin);
		//freopen("output.txt","w",stdout);
		for(scanf("%d\n", &N), n=1; n<=N; n++){
			gets(T); L = strlen(T);
			for(i=0; i<=L; i++) for(j=0; j<=19; j++) f[i][j] = 0;
			for(i=0; i<=L; i++) f[i][0] = 1;
			for(i=1; i<=L; i++) for(j=1; j<=19 && j<=i; j++){
				f[i][j] = f[i-1][j];
				if (T[i-1]==S[j-1]) f[i][j] = (f[i][j] + f[i-1][j-1]) % 10000;
			}
			printf("Case #%d: %04d\n", n, f[L][19]);
		}
		return 0;
}