#pragma comment(linker,"/STACK:16000000")

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
#define fil(a,b) memset(a,b,sizeof(a))
#define cpy_to(a,b) memcpy(b,a,sizeof(a))
#define lld "%I64d"

struct point{
	int i,j;
	void init(int x,int y){
		i = x;
		j = y;
	}
};

char a[20][20];
struct Pos{
	bool isPortal;
	int r, c;
	int len;
	int i,j;
	void init(int x, int y, int l,int row, int col){
		i = x;
		j = y;
		len = l;
		r = row;
		c = col;
		if (r)
			isPortal = true;
	}
	void init(int x, int y, int l, point &p){
		i = x;
		j = y;
		len = l;
		r = p.i;
		c = p.j;
		isPortal = true;
	}
} s[65536];
int di[4] = {1,-1,0,0};
int dj[4] = {0,0,1,-1};
bool use[20][20][20][20];
int ds[20][20][20][20],ds2[20][20][20][20];
void floid2(int n, int m){
	for (int ki = 1; ki <=n ;ki++)
	for (int kj = 1; kj <=m ;kj++)
	for (int ii = 1; ii <=n ;ii++)
	for (int ij = 1; ij <=m ;ij++)
	for (int ji = 1; ji <=n ;ji++)
	for (int jj = 1; jj <=m ;jj++)
	if (ds2[ii][ij][ki][kj] + ds2[ki][kj][ji][jj] < ds2[ii][ij][ji][jj])
		ds2[ii][ij][ji][jj] = ds2[ii][ij][ki][kj] + ds2[ki][kj][ji][jj];
}
void floid(int n, int m){
	fil(ds,31);
	for (int i = 1; i<=n; i++)
	for (int j = 1; j<=m; j++)
		if (a[i][j] !='#'){
			ds[i][j][i][j] = 0;
			for (int d = 0; d < 4; d++)
			{
				if (a[i + di[d]][j + dj[d]] !='#')
					ds[i][j][i + di[d]][j + dj[d]] = 1;
			}
		}
	for (int ki = 1; ki <=n ;ki++)
	for (int kj = 1; kj <=m ;kj++)
	for (int ii = 1; ii <=n ;ii++)
	for (int ij = 1; ij <=m ;ij++)
	for (int ji = 1; ji <=n ;ji++)
	for (int jj = 1; jj <=m ;jj++)
	if (ds[ii][ij][ki][kj] + ds[ki][kj][ji][jj] < ds[ii][ij][ji][jj])
		ds[ii][ij][ji][jj] = ds[ii][ij][ki][kj] + ds[ki][kj][ji][jj];

}
point pu[20][20], pd[20][20], pl[20][20], pr[20][20];
int dist(int i,int j,int ei,int ej,point p,point p2){
	return min(ds[i][j][p.i][p.j] + ds[p2.i][p2.j][ei][ej],
		ds[i][j][p2.i][p2.j] + ds[p.i][p.j][ei][ej]);
}
int calc(int si,int sj,int ei, int ej){
	int res = ds[si][sj][ei][ej];
	nul(use);
	s[0].init(si,sj,0,0,0);
	use[si][sj][0][0] = true;
	int u = 1;
	for (int d = 0; d < u; d++){
		int i = s[d].i, j=s[d].j, len = s[d].len + 1;
		point p;
		p.init(s[d].r, s[d].c);
		if (!s[d].isPortal){
			for (int dir = 0; dir < 4;dir++)
				if (a[i + di[dir]][j + dj[dir]] != '#' && !use[i + di[dir]][j + dj[dir]][0][0]){
					use[i + di[dir]][j + dj[dir]][0][0] = true;
					s[u++].init(i + di[dir], j + dj[dir], len, 0, 0);
				}
			if (!use[i][j][pl[i][j].i][pl[i][j].j]){
				use[i][j][pl[i][j].i][pl[i][j].j] = true;
				s[u++].init(i,j,len,pl[i][j]);
			}
			if (!use[i][j][pr[i][j].i][pr[i][j].j]){
				use[i][j][pr[i][j].i][pr[i][j].j] = true;
				s[u++].init(i,j,len,pr[i][j]);
			}
			if (!use[i][j][pu[i][j].i][pu[i][j].j]){
				use[i][j][pu[i][j].i][pu[i][j].j] = true;
				s[u++].init(i,j,len,pu[i][j]);
			}
			if (!use[i][j][pd[i][j].i][pd[i][j].j]){
				use[i][j][pd[i][j].i][pd[i][j].j] = true;
				s[u++].init(i,j,len,pd[i][j]);
			}
			continue;
		}
		for (int dir = 0; dir < 4;dir++)
			if (a[i + di[dir]][j + dj[dir]] != '#' && !use[i + di[dir]][j + dj[dir]][p.i][p.j]){
				use[i + di[dir]][j + dj[dir]][p.i][p.j] = true;
				s[u++].init(i + di[dir], j + dj[dir], len, p);
			}
		point p2;
		p2 = pu[i][j];
		res = min(res, -1 + len + dist(i,j,ei,ej,p,p2));
		p2 = pl[i][j];
		res = min(res, -1 + len + dist(i,j,ei,ej,p,p2));
		p2 = pr[i][j];
		res = min(res, len - 1 + dist(i,j,ei,ej,p,p2));
		p2 = pd[i][j];
		res = min(res, -1 + len + dist(i,j,ei,ej,p,p2));
	}
	return res;
}
void solve()
{
	fil(a,'#');
	int n, m;
	scanf("%d%d", &n, &m);
	a[0][m+2] = 0;
	for (int i = 1; i <= n; i++){
		scanf("%s", a[i] + 1);
		a[i][m + 1] = '#';
		a[i][m + 2] = 0;
	}
	floid(n,m);
	int si, sj, ei, ej;
	for (int i = 1; i <= n; i++)
	for (int j = 1; j <= m; j++){
		if (a[i][j] == 'O'){
			si = i;
			sj = j;
		}
		if (a[i][j] == 'X'){
			ei = i;
			ej = j;
		}
	}
	if (ds[si][sj][ei][ej] > 1000){
		printf("THE CAKE IS A LIE");
		return;
	}
	for (int i = 1; i <=n ;i++)
		for (int j = 1; j <= m; j++){
			if (a[i-1][j] == '#')
				pu[i][j].init(i,j);
			else
				pu[i][j] = pu[i-1][j];
			if (a[i][j-1] == '#')
				pl[i][j].init(i,j);
			else
				pl[i][j] = pl[i][j-1];
		}
	for (int i = n; i >=1 ;i--)
		for (int j = m; j >= 1; j--){
			if (a[i + 1][j] == '#')
				pd[i][j].init(i,j);
			else
				pd[i][j] = pd[i + 1][j];
			if (a[i][j + 1] == '#')
				pr[i][j].init(i,j);
			else
				pr[i][j] = pr[i][j+1];
		}
	int res = ds[si][sj][ei][ej];
	fil(ds2,63);
	for (int si = 1; si<=n; si++)
	for (int sj = 1; sj<=m; sj++)
		if (a[si][sj]!='#')
			for (int ei = 1; ei<=n; ei++)
			for (int ej = 1; ej<=m; ej++)
				if (a[ei][ej]!='#')
					ds2[si][sj][ei][ej] = calc(si,sj,ei,ej);
	;
	calc(4,3,4,7);
	floid2(n,m);
	printf("%d",ds2[si][sj][ei][ej]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int iTest = 1; iTest <= nTests; iTest++){
		printf("Case #%d: ",iTest);
		solve();
		printf("\n");
	}
	return 0;
}