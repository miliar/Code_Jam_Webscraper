#include <stdio.h>
#include <string.h>

#define nmax 50

int T, n, x[nmax];
long long a[nmax][2][3][5][7];
char s[nmax];

int main()
{
	freopen("b.in", "r", stdin);
	// freopen("b.out", "w", stdout);

	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++)
	{
		fgets(s, nmax, stdin);
		for(int i = 0; i < (int)strlen(s) - 1; i++)
			x[i + 1] = s[i] - '0', n = i + 1;
		memset(a, 0, sizeof(a));
		a[0][0][0][0][0] = 1;
		for(int i = 0; i < n; i++)
		{
			for(int i2 = 0; i2 < 2; i2++)
				for(int i3 = 0; i3 < 3; i3++)
					for(int i5 = 0; i5 < 5; i5++)
						for(int i7 = 0; i7 < 7; i7++)
							if(a[i][i2][i3][i5][i7] != 0)
							{
								int r2 = 0, r3 = 0, r5 = 0, r7 = 0;
								for(int j = i + 1; j <= n; j++)
								{
									r2 = (r2 * 10 + x[j]) % 2;
									r3 = (r3 * 10 + x[j]) % 3;
									r5 = (r5 * 10 + x[j]) % 5;
									r7 = (r7 * 10 + x[j]) % 7;
									a[j][(r2 + i2) % 2][(r3 + i3) % 3][(r5 + i5) % 5][(r7 + i7) % 7] += a[i][i2][i3][i5][i7];

									int nr2 = (i2 - r2) % 2; while(nr2 < 0) nr2 += 2;
									int nr3 = (i3 - r3) % 3; while(nr3 < 0) nr3 += 3;
									int nr5 = (i5 - r5) % 5; while(nr5 < 0) nr5 += 5;
									int nr7 = (i7 - r7) % 7; while(nr7 < 0) nr7 += 7;
									a[j][nr2][nr3][nr5][nr7] += a[i][i2][i3][i5][i7];
								}

							}
		}

		long long sum = 0;
		for(int i2 = 0; i2 < 2; i2++)
			for(int i3 = 0; i3 < 3; i3++)
				for(int i5 = 0; i5 < 5; i5++)
					for(int i7 = 0; i7 < 7; i7++)
						if(i2 == 0 || i3 == 0 || i5 == 0 || i7 == 0) 
							sum += (long long)a[n][i2][i3][i5][i7];
		sum /= 2;	

		printf("Case #%d: %Ld\n", t, sum);
	}
}
