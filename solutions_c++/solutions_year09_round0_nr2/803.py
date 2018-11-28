#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;

#define FOR(i,n) for((i) = 0; (i) < (n); ++(i))
#define SFOR(i,m,n) for((i) = (m); (i) < (n); ++(i))

char cur;
int A[110][110];
int S[110][110];
char R[110][110];

int dx[5] = {0, -1, 0, 0, 1};
int dy[5] = {0, 0, -1, 1, 0};

int validate(int a, int b, int c1, int c2, int c3, int c4)
{
	return (a<b) && (a <=c1) && (a <=c2) && (a <=c3) && (a <=c4);
}

void doit(int a, int b)
{
	if (R[a][b] != 0) return;
	R[a][b] = cur;
	doit(a + dx[S[a][b]], b + dy[S[a][b]]);
	if (dx[S[a+1][b]] == -1) doit(a+1, b);
	if (dy[S[a][b+1]] == -1) doit(a, b+1);
	if (dx[S[a-1][b]] == 1) doit(a-1, b);
	if (dy[S[a][b-1]] == 1) doit(a, b-1);
}

int main(void)
{
	FILE *fi, *fo;	
	fi = fopen("d:\\a.in", "rt");
	fo = fopen("a.out", "wt");

	
	int t, tt;
	fscanf(fi, "%d", &tt);

	FOR(t, tt)
	{
		int n,m,i,j;
		fscanf(fi, "%d%d", &n, &m);
		memset(R, 0,sizeof(R));
		FOR(i, 110) FOR(j, 110)  A[i][j] = 1000000000;
		SFOR(i, 1, n+1) SFOR(j, 1, m+1) fscanf(fi, "%d", &A[i][j]);
		SFOR(i, 1, n+1) SFOR(j, 1, m+1)
		{
			if (validate(A[i-1][j], A[i][j], A[i-1][j], A[i][j-1], A[i][j+1], A[i+1][j])) {S[i][j] = 1; continue;}
			if (validate(A[i][j-1], A[i][j], A[i-1][j], A[i][j-1], A[i][j+1], A[i+1][j])) {S[i][j] = 2; continue;}
			if (validate(A[i][j+1], A[i][j], A[i-1][j], A[i][j-1], A[i][j+1], A[i+1][j])) {S[i][j] = 3; continue;}
			if (validate(A[i+1][j], A[i][j], A[i-1][j], A[i][j-1], A[i][j+1], A[i+1][j])) {S[i][j] = 4; continue;}
			S[i][j] = 0;
		}
		int fl = 1;
		cur = 'a';
		while (fl)
		{
			fl = 0;
			SFOR(i, 1, n+1) SFOR(j, 1, m+1) if (R[i][j] == 0)
			{
				fl = 1;
				doit(i, j);
				++cur;
			}
		}
		fprintf(fo, "Case #%d:\n", t+1);
		SFOR(i, 1, n+1){
			SFOR(j, 1, m+1) fprintf(fo, "%c ", R[i][j]);
			fprintf(fo, "\n");
		}
	}

	fclose(fi);
	fclose(fo);

	return 0;
}