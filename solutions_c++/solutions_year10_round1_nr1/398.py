#include "cstdio"

const int maxn = 51;

int n,k;
char a[maxn][maxn];

void init()
{
	scanf("%ld %ld",&n,&k);
	int i,j;
	char ch;
	for (i = 0; i < n; ++ i)
		for (j = 0; j < n; ++ j){
			do
				ch = getchar();
			while (ch != '.' && ch != 'R' && ch != 'B');
			a[i][j] = ch;
		}
}
/*
7 3
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
*/

char b[maxn][maxn];
const int step[4][2] = {{1,0},{0,1},{1,-1},{1,1}};

void doit()
{
	int i,j;

	for (i = 0; i < n; ++ i)
		for (j = 0; j < n; ++ j)
			b[i][j] = '.';

	int j1,j2;
	for (i = n - 1; i >= 0; --i){
		j1 = n - 1;
		while (j1 >= 0 && a[i][j1] == '.') --j1;
		j2 = n - 1;
		while (j1 >= 0){
			b[i][j2] = a[i][j1];
			--j2;
			--j1;
			while (j1 >= 0 && a[i][j1] == '.') --j1;
		}
	}

	int ii,jj,g,k0;
	bool flagr = false;
	bool flagb = false;
	for (i = 0; i < n; ++ i){
		for (j = 0; j < n; ++ j){
			if (b[i][j] != '.')
				for (g = 0; g < 4; ++ g){
					ii = i;
					jj = j;
					k0 = 0;
					while (ii >= 0 && ii < n &&
						   jj >= 0 && jj < n &&
						   b[ii][jj] == b[i][j]){
						++k0;
						ii += step[g][0];
						jj += step[g][1];
						if (k0 >= k){
							if (b[i][j] == 'R')
								flagr = true;
							else
								flagb = true;
							break;
						}
					}
					if (flagr && flagb)
						break;
				}
			if (flagr && flagb)
				break;
		}
		if (flagr && flagb)
			break;
	}

	if (flagr)
		if (flagb)
			printf("Both\n");
		else
			printf("Red\n");
	else
		if (flagb)
			printf("Blue\n");
		else
			printf("Neither\n");

}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int test,testnum;
	scanf("%ld",&testnum);
	for (test =	1; test <= testnum; ++ test){
		printf("Case #%ld: ",test);
		init();
		doit();
	}
	return 0;
}
