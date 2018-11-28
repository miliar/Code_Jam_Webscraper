#include<cstdio>

using namespace std;

int T;
int H, W;
int map[100][100];
char r[100][100];

char c;

int di[4] = {-1, 0, 0, 1};
int dj[4] = {0, -1, 1, 0};

void set(int i, int j)
{
	if(r[i][j] != '?') return;

	int x, y;
	int a = map[i][j];

	int ii, jj;
	int k;

	for(k=0; k<4; k++) {
		ii = i + di[k];
		jj = j + dj[k];

		if(ii < 0 || ii >= H || jj < 0 || jj >= W) continue;

		if(map[ii][jj] < a) {
			a = map[ii][jj];
			x = ii;
			y = jj;
		}
	}
	
	if(a == map[i][j]) {
		r[i][j] = c++;
	}
	else {
		set(x, y);
		r[i][j] = r[x][y];
	}
}


int main()
{
	FILE *infile = fopen("b.in", "rt");
	FILE *outfile = fopen("b.out", "wt");

	fscanf(infile, "%d", &T);
	int loop;
	for(loop=1; loop<=T; loop++) {
		fscanf(infile, "%d %d", &H, &W);
		int i, j;
		for(i=0; i<H; i++)
			for(j=0; j<W; j++) {
				fscanf(infile, "%d", &map[i][j]);
				r[i][j] = '?';
			}
		c = 'a';		
		for(i=0; i<H; i++)
			for(j=0; j<W; j++)
				set(i, j);

		fprintf(outfile, "Case #%d:\n", loop);
		for(i=0; i<H; i++) {
			for(j=0; j<W-1; j++)
				fprintf(outfile, "%c ", r[i][j]);
			fprintf(outfile, "%c\n", r[i][W-1]);
		}
	}

	fclose(infile);
	fclose(outfile);
	return 0;
}
