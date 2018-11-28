#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int N;
int M;
int A;
int x2;
int y2;
int x3;
int y3;

void Read()
{
	scanf("%d %d %d", &N, &M, &A);
}

bool CanDraw()
{    
	for (x2=0; x2<=N; x2++)
	for (x3=0; x3<=N; x3++)
	for (y2=0; y2<=M; y2++)
	for (y3=0; y3<=M; y3++)
		if (x2 * y3 - x3 * y2 == A || x3 * y2 - x2 * y3 == A) 
			return true;

    return false;
}

void Solve()
{
	if (CanDraw())
		printf("%d %d %d %d %d %d\n", 0, 0, x2, y2, x3, y3);
	else
		printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("2.in", "rt", stdin);
	freopen("2.out", "wt", stdout);

	int t;
	int n;

	scanf("%d", &n);
	for (t=1; t<=n; t++)
	{
		Read();		
		printf("Case #%d: ", t);
		Solve();
	}
	return 0;
}

