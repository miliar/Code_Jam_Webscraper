#include<stdio.h>
#include<string.h>

int T, K, N, cas;
char a[100][100], b[100][100];

int check(char s[100][100], char c)
{
	int i, j, k;
	for (i=0;i<N;i++)
		for (j=0;j<N;j++)
			if (s[i][j] == c){
				if (j+K<=N){
					for (k=j;k<j+K;k++)
						if(s[i][k]!=c) break;
					if (k>=j+K) return 1;
				}
				if (i+K<=N){
					for (k=i;k<i+K;k++)
						if(s[k][j]!=c) break;
					if (k>=i+K) return 1;
				}
				if (i+K<=N && j+K<=N){
					for (k=0;k<K;k++)
						if (s[i+k][j+k]!=c) break;
					if (k>=K) return 1;
				}
				if (i-K+1>=0 && j+K<=N){
					for (k=0;k<K;k++)
						if (s[i-k][j+k]!=c) break;
					if (k>=K) return 1;
				}
			}
	return 0;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, R, B, c;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++ ){
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		scanf("%d%d", &N, &K);
		//printf("%d %d\n", N, K);
		for (i=0;i<N;i++){
			scanf("%s",a[i]);
			for (j=N-1, c=N-1; j>=0; j--)
				if (a[i][j] != '.'){
					b[i][c--] = a[i][j];
					//printf("$%c:%c$\n", a[i][j],b[i][c+1]);
				}
			for (;c>=0;c--)
				b[i][c]='.';
		//	printf("%s\n",b[i]);
		}
		R = check(b, 'R');
		B = check(b, 'B');
		if (R && B) printf("Case #%d: Both\n", cas);else
		if (R) printf("Case #%d: Red\n", cas);else
		if (B) printf("Case #%d: Blue\n", cas);else
		printf("Case #%d: Neither\n", cas);
	}
	return 0;
}
