#include <cstdio>  

long long a[512][512];
long long nCr[512][512];

#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i)  

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	nCr[0][1] = nCr[1][0] = nCr[1][1] = 1;
	For2(i,2,501)
	{
		nCr[i][0] = nCr[i][i] = 1;
		For2(j,1,i) nCr[i][j] = (nCr[i-1][j-1] + nCr[i-1][j]) % 100003;
	}
	a[2][1] = 1;
	For2(i,3,501)
	{
		a[i][1] = a[i][2] = a[i][i-1] = 1;
		For2(j,3,i-1)
		{
			a[i][j] = 0;
			For2(k,1,j) 
				a[i][j] += a[j][k] * nCr[i-j-1][j-k-1];
			a[i][j] %= 100003;
		}
	}
	int ti=0, tn;
	scanf("%d",&tn);
	while(tn--)
	{
		int n;
		scanf("%d",&n);
		int ans = 0;
		For2(i,1,n) ans += a[n][i];
		printf("Case #%d: %d\n",++ti,ans % 100003);
	}
}
/*
100
2
3
4
5
6
7
8
*/