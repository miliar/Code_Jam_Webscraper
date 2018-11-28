#include <cstdio>
#include <cctype>
#include <cstring>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define ROF(i,s,e) for(int i=(s);i>=(int)(e);i--)
int t, ans, m, n;
const int M = 1024;
bool v[M][M];
char s[M][M];
bool b[M][M];

bool chk(int x,int y,int c) {
	FOR(i,0,c) FOR(j,0,c) {
		if (v[x+i][y+j])	return 0;
		if ((i+j)%2 && b[x+i][y+j]==b[x][y])	return 0;
		if ((i+j)%2==0 && b[x+i][y+j]!=b[x][y])	return 0;
	}
	FOR(i,0,c) FOR(j,0,c) {
		v[x+i][y+j] = 1;
	}
	return 1;
}
void out() {
	FOR(i,0,m) {
		FOR(j,0,n) v[i][j] ? putchar(' ') : putchar(!b[i][j] ? '#' : '_');
		puts("");
	}
}
int main() {
	scanf("%d", &t);
	FOR(zz,1,t+1) {
		scanf("%d%d",&m,&n);
		int cnt[M] = {0};
		FOR(i,0,m) scanf("%s", s[i]);
		memset(v,0,sizeof(v));
		FOR(i,0,m) FOR(j,0,n/4) {
			int x;
			if (isalpha(s[i][j]))	x = s[i][j]-'A' + 10;
			else	x = s[i][j] - '0';
			FOR(k,0,4)
				b[i][j*4+(3-k)] = ((1<<k)&x) ? 1 : 0;
		}

		int mx = 32;
		while (mx) {
			bool f = 0;
			FOR(i,0,m-mx+1) {FOR(j,0,n-mx+1) {
				f = chk(i,j,mx);
				if (f) {
					cnt[mx]++;
//					printf("%d Found (%d,%d)\n", mx, i, j);
//					out();
					break;
				}
			}
			if (f)	break;
			}
			if (!f)	mx--;
		}
		int tot = 0;
		FOR(i,1,33) tot += cnt[i] > 0;
		printf("Case #%d: %d\n", zz, tot);
		FOR(i,1,33) if (cnt[33-i]) printf("%d %d\n", 33-i,cnt[33-i]);
	}
}
