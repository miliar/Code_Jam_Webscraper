#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>

using namespace std;

int R,F,C;

char area[64][64];
int hs[64][64];

int digs[64][64][64]; // [row][from][to]
int INF = 1<<30;

/*
int getH(int y, int x)
{
	if (area[y][x]=='.') return 1+getH(y+1,x);
	return 0;
}*/

int dfs(int r, int f, int t)
{
	if (f>t) return INF;
	if (r==R-1) return 0;
	if (digs[r][f][t]>=0) return digs[r][f][t];

	if (area[r+1][f]=='.') {
		if (hs[r+1][f]>F) return digs[r][f][t] = dfs(r,f+1,t);
		return digs[r][f][t] = min(dfs(r+1, f,f), dfs(r,f+1,t));
	}
	if (area[r+1][t]=='.') {
		if (hs[r+1][t]>F) return digs[r][f][t] = dfs(r,f,t-1);
		return digs[r][f][t] = min(dfs(r+1, t,t), dfs(r,f,t-1));
	}

	for(int i=f; i<=t; ++i)
		if (area[r+1][i]!='#') return digs[r][f][t]=INF;
//	if (area[r+1][min(f+1,t)]=='.') return digs[r][f][t] = dfs(r+1,f,t);

	if (f>0 && area[r][f-1]=='.' && area[r+1][f-1]=='#')
		return digs[r][f][t] = dfs(r, f-1, t);
	if (t<C-1 && area[r][t+1]=='.' && area[r+1][t+1]=='#')
		return digs[r][f][t] = dfs(r, f, t+1);

//	int f2 = area[r+1][f]=='.' ? f+1 : f;
//	int t2 = area[r+1][t]=='.' ? t-1 : t;
	int f2=f, t2=t;

	int q=INF;
	for(int i=f2; i<=t2; ++i) {
//		if (getH(r+2, i)>=F) continue;

		for(int j=i; j<=t2; ++j) {
			if (i==f2 && j==t2) continue;
			if (i==f2 && hs[r+2][j]>=F) continue;
			if (j==t2 && hs[r+2][i]>=F) continue;
			if (i==j && hs[r+2][i]>=F) continue;
			if (min(hs[r+2][i],hs[r+2][j])>=F) continue;
			int d = dfs(r+1, i, j) + j-i+1;
			q = min(q,d);
			if (hs[r+2][j]>=F) break;
		}
	}
	if (f2>0 && area[r][f2-1]=='.' && hs[r+1][f2-1] <= F)
		q = min(q, dfs(r+1, f2-1, f2-1));
	if (t<C-1 && area[r][t+1]=='.' && hs[r+1][t+1] <= F)
		q = min(q, dfs(r+1, t2+1, t2+1));
//	printf("got %d %d %d : %d ; %d %d\n", r,f,t,q,f2,t2);
	return digs[r][f][t]=q;
}

int main()
{
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>R>>C>>F;
		for(int i=0; i<R; ++i)
			cin>>area[i];
		memset(digs, -1, sizeof(digs));
		for(int i=0; i<=C; ++i) area[R][i]='#';
		for(int i=0; i<=C; ++i) hs[R][i]=0;
		for(int i=R-1; i>=0; --i)
			for(int j=0; j<C; ++j) hs[i][j]=area[i][j]=='#'?0:1+hs[i+1][j];

		/*
		int r;
		for(r=0; area[r+1][0]=='.'; ++r) ;
		int start;
		for(start=0; area[r][start+1]=='.' && area[r+1][start+1]=='#'; ++start) ;
		int d = dfs(r, 0, start);
		*/
		int d = hs[0][0]>F ? INF : dfs(0, 0, 0);
		if (d==INF) cout<<"Case #"<<a<<": No\n";
		else cout<<"Case #"<<a<<": Yes "<<d<<'\n';
	}
}
