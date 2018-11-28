#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAX_TAILLE = 100;

int alt[MAX_TAILLE][MAX_TAILLE];
int nbTests;
int nbLigs, nbCols;

int nbB;
int b[MAX_TAILLE][MAX_TAILLE];
char alias[26];

int dirl[4] = {-1, 0, 0, 1};
int dirc[4] = {0, -1, 1, 0};

int rec(int l, int c)
{
	if(b[l][c] != -1)
		return b[l][c];
		
	int nc, nl;
	int vc = c, vl = l;
	for(int dir = 0; dir < 4; dir++)
	{
		nc = c + dirc[dir];
		nl = l + dirl[dir];
		if(nc < 0 || nc >= nbCols || nl < 0 || nl >= nbLigs) continue;
		if(alt[nl][nc] < alt[vl][vc])
		{
			vl = nl;
			vc = nc;
		}
	}
	if(vl == l && vc == c)
	{
		//printf("(%d, %d) is a sink\n", l, c);
		b[l][c] = nbB++;
	}
	else
	{
		b[l][c] = rec(vl, vc);
		//printf("(%d, %d) is flows to (%d, %d)\tB : %d\n", l, c, vl, vc, b[l][c]);
	}
	return b[l][c];
}

void solve(int t)
{
	nbB = 0;
	memset(b, -1, sizeof(b));
	memset(alias, 0, sizeof(alias));
	
	scanf("%d%d\n", &nbLigs, &nbCols);
	for(int l = 0; l < nbLigs; l++)
		for(int c = 0; c < nbCols; c++)
			scanf("%d", &alt[l][c]);
			
	for(int l = 0; l < nbLigs; l++)
		for(int c = 0; c < nbCols; c++)
			rec(l, c);
			
	printf("Case #%d:\n", (t+1));
	int car = 'a';
	for(int l = 0; l < nbLigs; l++)
		for(int c = 0; c < nbCols; c++)
		{
			if(alias[b[l][c]] == 0)
				alias[b[l][c]] = car++;
			printf("%c", alias[b[l][c]]);
			//printf("%d", b[l][c]);
			if(c != nbCols - 1)
				printf(" ");
			else
				printf("\n");
		}	
}

int main()
{
	scanf("%d\n", &nbTests);
	
	for(int c = 0; c < nbTests; c++)
		solve(c);
		
	return 0;
}
