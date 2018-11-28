#include <iostream>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))

int H, W;
int A[128][128];
int G[128][128];
int T[128][128], R[128][128];

int g[4] = {-1,0,0,1},
	h[4] = {0,-1,1,0};

void dfs(int ht, int w, int c)
{
	T[ht][w] = c;
	FOR(k,0,4)
	{
		int nh = ht+g[k], nw = w+h[k];
		if(nh < 0 || nh >= H || nw < 0 || nw >= W) continue;
		if(G[nh][nw] == 3-k) dfs(nh,nw,c);
	}
}

int main()
{
	int Te, te = 1;
	cin >> Te;
	while(Te--)
	{
		cin >> H >> W;
		FOR(i,0,H) FOR(j,0,W) cin >> A[i][j];
		SET(G,-1);
		FOR(i,0,H) FOR(j,0,W)
		{
			int a = A[i][j], d = -1;
			FOR(k,0,4)
			{
				int ni = i+g[k], nj = j+h[k];
				if(ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
				if(A[ni][nj] < a) { a = A[ni][nj]; d = k;}
			}
			if(d != -1) G[i][j] = d;
		}
		SET(T,-1);
		int col = 0;
		FOR(i,0,H) FOR(j,0,W) if(G[i][j] == -1) dfs(i,j,col++);
		assert(col <= 26);
		vector<int> re(col,-1);
		col = 0;
		FOR(i,0,H) FOR(j,0,W) if(re[T[i][j]] == -1) re[T[i][j]] = col++;
		SET(R,-1);
		FOR(i,0,H) FOR(j,0,W) R[i][j] = re[T[i][j]];
		cout << "Case #" << te << ":" << endl;
		FOR(i,0,H)
		{
			cout << char('a'+R[i][0]);
			FOR(j,1,W) cout << " " << char('a'+R[i][j]);
			cout << endl;
		}
		te++;
	}
	return 0;
}
