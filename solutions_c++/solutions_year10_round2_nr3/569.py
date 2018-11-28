#include<stdio.h>

int T, N, cas;
int c[510][510], f[510][510], a[510];

void pre()
{
	int i, j, p, sum;
	c[1][1] = c[1][0] = 1;
	for (i=2; i<=500; i++)
		for (j=0;j<=i;j++){
			c[i][j] = c[i-1][j];
			if (j) c[i][j] += c[i-1][j-1];
			c[i][j] %= 100003;
		}
		
	f[2][1] = 1;
	f[3][1] = f[3][2] = 1;
	a[2] = 1;
	a[3] = 2;
	for (i = 4; i<= 500; i++){
		f[i][1] = f[i][i-1] = 1;
		a[i] = 2;
		for (j=2;j<i-1;j++){
			sum = 0;
			for (p=1;p<j;p++){
				sum = sum + c[i-j-1][j-p-1] * f[j][p] % 100003;
				sum %= 100003;
			}
			f[i][j] = sum % 100003;
			//if (i<10) printf("f[%d][%d]=%d\n", i, j, f[i][j]);
			a[i] = (a[i] + f[i][j]) % 100003;
		}
		//if (i<10) printf("a[%d]=%d\n", i,a[i]);
	}
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	pre();
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas ++){
		scanf("%d", &N);
		printf("Case #%d: %d\n", cas, a[N]);
	}
	return 0;
}
