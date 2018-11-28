#include <stdio.h>
#include <string.h>

int ntc;
int n, m;

int mm[100][100];
int dy[] = {-1, 0, 0, 1};
int dx[] = {0, -1, 1, 0};
bool valid(int y, int x)
{
	return (y>=0 && y<n && x>=0 && x<m);
}

bool con[100][100][4];

void gen_map()
{
	memset(con, 0, sizeof(con));
	int i, j;
	int k;

	int ny, nx;
	int minv, tmin;

	for (i=0; i<n; i++) for (j=0; j<m; j++)
	{

		tmin = -1;
		minv = 1000000;
		for (k=0; k<4; k++)
		{
			ny = i + dy[k];
			nx = j + dx[k];
			if (!valid(ny,nx)) continue;

			if (mm[ny][nx] < minv)
			{
				minv = mm[ny][nx];
				tmin = k;
			}
		}

		if (minv >= mm[i][j]) continue;
		con[i][j][tmin] = true;
		con[i+dy[tmin]][j+dx[tmin]][3-tmin] = true;
	}
}

int lab[100][100];
int qy[10000], qx[10000];
int nq;

void add(int y, int x, int v)
{
	qy[nq] = y;
	qx[nq] = x;
	lab[y][x] = v;
	nq++;
}

void ff(int y, int x, int v)
{
	nq = 0;
	add(y, x, v);

	int it;
	int i, ny, nx;
	for (it=0; it<nq; it++)
	{
		y = qy[it];
		x = qx[it];

		for (i=0; i<4; i++) if (con[y][x][i])
		{
			ny = y + dy[i];
			nx = x + dx[i];
			if (lab[ny][nx] == -1)
				add(ny, nx, v);
		}
	}
}

int main()
{
	FILE* fi = fopen("B-large.in", "r");
	FILE* fo = fopen("B-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int tc;
	int i, j;
	int nlab;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d %d", &n, &m);
		for (i=0; i<n; i++) for (j=0; j<m; j++)
			fscanf(fi, "%d", &mm[i][j]);

		gen_map();
		memset(lab, -1, sizeof(lab));

		nlab = 0;
		for (i=0; i<n; i++) for (j=0; j<m; j++)
		{
			if (lab[i][j] == -1)
			{
				ff(i,j,nlab++);
			}
		}

		printf("Case #%d:\n", tc);
		fprintf(fo, "Case #%d:\n", tc);
		for (i=0; i<n; i++)
		{
			for (j=0; j<m; j++)
			{
				if (j) 
				{
					printf(" ");
					fprintf(fo, " ");
				}

				printf("%c", lab[i][j]+'a');
				fprintf(fo, "%c", lab[i][j]+'a');
			}
			printf("\n");
			fprintf(fo, "\n");
		}
	}	

	fclose(fi); fclose(fo);
}