#include <iostream>

using namespace std;

const int dx[4] = {-1, 0, 0, 1}, dy[4] = {0, -1, 1, 0};

#define MAXS 105

int gc[30];
int g[MAXS][MAXS], ng;
int T, H, W, a[MAXS][MAXS];

void input () {
	scanf ("%d%d", &H, &W);
	memset (a, 0x3f, sizeof(a));
	memset (g, 0, sizeof(g));
	for (int i=1;i<=H;i++)
		for (int j=1;j<=W;j++)
			scanf ("%d", &a[i][j]), g[i][j] = 0;
}

void solve () {
	ng = 1;
}

int find (int r, int c) {
	if (g[r][c]!=0)
		return g[r][c];
	int best = a[r][c], pos = -1;
	for (int i=0;i<4;i++)
		if (a[r+dx[i]][c+dy[i]]<best)
			best = a[r+dx[i]][c+dy[i]], pos = i;
	if (pos==-1)
		return g[r][c] = ng++;
	return g[r][c] = find(r+dx[pos], c+dy[pos]);
}

void output () {
	for (int i=0;i<30;i++)
		gc[i] = -1;
	int num = 0;
	for (int i=1;i<=H;i++, printf ("\n"))
		for (int j=1;j<=W;j++) {
			if (g[i][j]==0)
				find(i, j);
			if (gc[g[i][j]]==-1)
				gc[g[i][j]] = num, num++;
			if (j==1)
				printf ("%c", gc[g[i][j]]+'a');
			else
				printf (" %c", gc[g[i][j]]+'a');
		}
}

int main () {
	freopen ("prog.in", "r", stdin);
	freopen ("prog.out", "w", stdout);
	scanf ("%d", &T);
	for (int i=1;i<=T;i++) {
		printf ("Case #%d:\n", i);
		input ();
		solve ();
		output ();
	}
	return 0;
}
