#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(i,n) for(int i=0; i<(n); i++)

void doit(int a[100][100], int how[100][100], int n)
{
	FOR(k, n)
		FOR(i, n)
			FOR(j, n)
				if (a[i][k] + a[k][j] < a[i][j])
					a[i][j] = a[i][k] + a[k][j];
	memset(how, 0, sizeof(how));
	
	int du[100] = {0};
	FOR(i, n)
		FOR(j, n)
			if (a[i][j] == 1)
				du[i]++;
	
	FOR(k, n)
		FOR(i, n)
			FOR(j, n)
				if (a[i][j] == k)
					how[i][k] += du[j];
		
}

int readg(int a[100][100])
{
	int n;
	scanf("%d", &n);
	FOR(i, n)
	{
		FOR(j, n)
			a[i][j] = 1000000;
		a[i][i] = 0;
	}
	FOR(i, n-1)
	{
		int x, y;
		scanf("%d%d", &x, &y);
		x--;
		y--;
		a[x][y] = 1;
		a[y][x] = 1;
	}
	return n;
}

int main()
{
	int C;
	scanf("%d", &C);
	for (int ca=1; ca<=C; ca++)
	{
		int na, nb;
		int a[100][100], b[100][100];
		int tmp[100][100];
		na = readg(a);
		nb = readg(b);
		
		if (nb > na)
		{
			swap(na, nb);
			memmove(tmp, a, sizeof(a));
			memmove(a, b, sizeof(b));
			memmove(b, tmp, sizeof(b));
		}
/*
		doit(a, howa, n);
		doit(b, howb, n);
		
		FOR(i, n)
		{
			FOR(j, n)
			printf("%d\n", howa[i][j]);
		putchar(10);
		*/
		int p[100];
		FOR(i, na)
			p[i] = i;
			
		bool ok = 0;
		do
		{
			int aa[100][100];
			FOR(i, na)
				FOR(j, na)
				{
					aa[p[i]][p[j]] = a[i][j];
				}
			
			
			/*
			printf("checking:\n");
			FOR(i, na)
			{
				FOR(j, na)
					printf("%d ", aa[i][j]);
			putchar(10);
			}
			printf("???\n");
			FOR(i, nb)
			{	FOR(j, nb)
					printf("%d ", b[i][j]);
			
			putchar(10);
			}
			printf("-------------\n");
			*/
			
			bool oo = 1;
			FOR(i, nb)
				FOR(j, nb)
					if (aa[i][j] == 1000000 && b[i][j] < 1000000)
					{
						oo = 0;
						break;
					}
			if (oo)
			{
				ok = 1;
				break;
			}
				
				
		}
		while (next_permutation(p, p+na));
		
		if (ok)
			printf("Case #%d: YES\n", ca);
		else
			printf("Case #%d: NO\n", ca);
	}
		
		
}
