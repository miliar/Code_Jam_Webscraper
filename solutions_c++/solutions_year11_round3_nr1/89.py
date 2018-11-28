#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define eps	1e-15

typedef long long int lint;

int r, c;
char m[100][100];
char result[100][100];

int dr[4] = { 0, 0, 1, 1 };
int dc[4] = { 0, 1, 0, 1 };

bool find(int rr, int cc)
{
	if ( m[rr][cc] != '#' ) return false;

	REP(i,4) 
		if ( m[rr+dr[i]][cc+dc[i]] != '#' ) return false;

	m[rr][cc] = '/';
	m[rr][cc+1] = '\\';
	m[rr+1][cc] = '\\';
	m[rr+1][cc+1] = '/';
//	REP(i,r) printf("%s\n",m[i]);
	
	REP(i,r) REP(j,c)
		if ( m[i][j] == '#' )
				return find(i, j);


	return true;
}

void solve()
{
	scanf("%d%d",&r,&c);

	memset(m,0x00,sizeof(m));
	REP(i,r) scanf("%s",m[i]);

	memcpy(result, m, sizeof(m));

	bool flag = true;

	REP(i,r) REP(j,c) 
		if (m[i][j] == '#') {
			flag = find(i, j);
			break;
		}
	if ( !flag ) {
		printf("Impossible\n");
		return;
	}

	REP(i,r) printf("%s\n",m[i]);
}

int main(void)
{
	freopen("a-large.in","r",stdin);
	//freopen("ainput.in","r",stdin);
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d:\n", i+1 );

		solve();
	}

	fclose(stdin);

	return 0;
}

