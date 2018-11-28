#include <cstdio>
#include <cstring>


int nt;

int n, k;

int a[100][25];

int c[100][100];

bool before(int x, int y)
{
	for(int i = 0; i < k; i++) if (a[x][i] >= a[y][i]) return false;
	return true;
}

char wA[100],wB[100];
int toA[100], toB[100];

int goB(int x);

int goA(int x)
{
	if (wA[x]) return 0;
	wA[x]=1;

	for(int i=0; i<n; i++) 
	if (c[x][i]) 
		if (goB(i))
		{
			toA[i]=x;
			toB[x]=i;
			return 1;
		}

	return 0;
}

int goB(int x)
{
	if (wB[x]) return 0;
	wB[x]=1;

	if (toA[x]==-1)	return 1;

	return goA(toA[x]);
}

int increase()
{
	memset(wA,0,sizeof wA);
	memset(wB,0,sizeof wB);

	int i;
	for(i=0; i<n; i++)
	if (toB[i]==-1)
	{
		if (goA(i)) return 1;
	}
	return 0;
}



int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d", &n, &k);

		for(int i = 0; i < n; i++)
		for(int j = 0; j < k; j++) scanf("%d", &a[i][j]);

		memset(c, 0, sizeof c);

		for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++) if (before(i, j)) c[i][j] = 1;

		memset(wA, 0, sizeof wA);
		memset(wB, 0, sizeof wB);

		memset(toA,-1,sizeof toA);
		memset(toB,-1,sizeof toB);


		int res = 0;

		while(increase()) res++;

		printf("%d\n", n - res);
	}

	return 0;	
}