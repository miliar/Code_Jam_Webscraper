#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

typedef vector <string> vs;

int tc, ntc;
int n, K;

char mm[60][60];
char tmm[60][60];

void rot()
{
	int i, j;
	for (i=0; i<n; i++) for (j=0; j<n; j++)
		tmm[i][j] = mm[n-j-1][i];
	for (i=0; i<n; i++) for (j=0; j<n; j++)
		mm[i][j] = tmm[i][j];
}

void norm()
{
	int i, j;
	for (j=0; j<n; j++)
	{
		int x = n-1;
		for (i=n-1; i>=0; i--) if (mm[i][j] != '.')
			mm[x--][j] = mm[i][j];
		while (x >= 0) mm[x--][j] = '.';
	}
}

void print()
{
	int i;
	for (i=0; i<n; i++) printf("%s\n", mm[i]);
	printf("\n");
}

int val[60][60];
char C;

bool valid(int y, int x)
{
	return (y>=0 && y<n && x>=0 && x<n);
}

bool win1(int dy, int dx)
{
	int i, j;
	for (i=0; i<n; i++) for (j=0; j<n; j++)
	{
		if (mm[i][j] != C) val[i][j] = 0;
		else
		{
			val[i][j] = 1;
			if (valid(i+dy, j+dx)) val[i][j] += val[i+dy][j+dx];
		}
		
		if (val[i][j] >= K) return true;		
	}	
	return false;
}

bool win(char c)
{
	C = c;
	if (win1(-1,0)) return true;
	if (win1(0,-1)) return true;
	if (win1(-1,-1)) return true;
	if (win1(-1,1)) return true;
	return false;
}

int main()
{
	scanf("%d", &ntc);
	int i;
	for (tc = 1; tc <= ntc; tc++)
	{
		scanf("%d %d", &n, &K);
		for (i=0; i<n; i++) scanf("%s", mm[i]);
		
		//print();
		rot();
		//print();
		norm();	
		//print();	
		
		int wb = win('B');
		int wr = win('R');
		
		printf("Case #%d: ", tc);
		if (wb && wr) printf("Both\n");
		else if (wb) printf("Blue\n");
		else if (wr) printf("Red\n");
		else printf("Neither\n");
	}
}