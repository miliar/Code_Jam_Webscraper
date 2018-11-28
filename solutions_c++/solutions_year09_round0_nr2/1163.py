#include <stdio.h>
#define N 110
int r, c, m[N][N], di[]={-1, 0, 0, 1}, dj[]={0, -1, 1, 0}, q[]={3, 2, 1, 0}, w[N][N], u[N][N], a;
bool is(int i, int j) { return i>=0 && i<r && j>=0 && j<c; }
void dfs(int i, int j)
{
	int k;
	u[i][j]=a;
	for(k=0; k<4; k++)
		if(is(i+di[k], j+dj[k]) && w[i+di[k]][j+dj[k]]==q[k] && u[i+di[k]][j+dj[k]]==-1) dfs(i+di[k], j+dj[k]);
	if(w[i][j]!=-1 && u[i+di[w[i][j]]][j+dj[w[i][j]]]==-1) dfs(i+di[w[i][j]], j+dj[w[i][j]]);
}
int main()
{
	int i, j, k, t, ts, bk, h;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &r, &c), i=0; i<r; i++)
			for(j=0; j<c; scanf("%d", &m[i][j]), j++);
		for(i=0; i<r; i++)
			for(j=0; j<c; w[i][j]=bk, j++)
				for(bk=-1, h=m[i][j], k=0; k<4; k++)
					if(is(i+di[k], j+dj[k]) && m[i+di[k]][j+dj[k]]<h) { h=m[i+di[k]][j+dj[k]]; bk=k; }
		for(i=0; i<r; i++)
			for(j=0; j<c; u[i][j]=-1, j++);
		for(a=0, i=0; i<r; i++)
			for(j=0; j<c; j++)
				if(u[i][j]==-1) { dfs(i, j); a++; }
		for(printf("Case #%d:\n", t+1), i=0; i<r; printf("%c\n", u[i][j]+'a'), i++)
			for(j=0; j<c-1; printf("%c ", u[i][j]+'a'), j++);
	}
	return 0;
}