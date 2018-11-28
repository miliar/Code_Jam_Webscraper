#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)

const int dx[]={-1, -1, 0, 1, 1, 1, 0, -1}, 
		dy[]={0, 1, 1, 1, 0, -1, -1, -1};

const int MAXN=60;

char s[MAXN][MAXN], a[MAXN][MAXN];
int n, k;

int check(int i, int j)
{
	int ret=-1;
	if (a[i][j]=='.') return -1;
	else ret=a[i][j]=='B';
	for(int d=0; d<8; ++d) {
		int x=i, y=j, t;
		for(t=0; t<k-1; ++t) {
			x+=dx[d], y+=dy[d];
			if (x<0 || y<0 || x>=n || y>=n || a[x][y]!=a[i][j]) break;
		}
		if (t==k-1) return ret;
	}
	return -1;
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T, tt=0;
	scanf("%d", &T);
	while (tt<T) {
		printf("Case #%d: ", ++tt);
		scanf("%d%d", &n, &k);
		REP(i, n) scanf("%s", s[i]);
		REP(i, n) REP(j, n) a[i][j]='.';
		REP(i, n) {
//			printf("%s", s[i]);
			int p=n-1;
			for(int j=n-1; j>=0; --j)
				if (s[i][j]!='.') {
					a[i][p--]=s[i][j];
//					printf("%c", s[i][j]);
			}
//			printf("%d\n", p);
		}
		/*
		printf("\n");
		REP(i, n) {
			REP(j, n)
				printf("%c", a[i][j]);
			printf("\n");
		}
		*/
		bool w[2]={false, false};
		REP(i, n) 
			REP(j, n) {
				int ret=check(i, j);
				if (ret!=-1) w[ret]=true;
		}
		if (w[0] && w[1]) 
			printf("Both\n");
		if (!w[0] && !w[1]) 
			printf("Neither\n");
		if (w[0] && !w[1]) 
			printf("Red\n");
		if (!w[0] && w[1]) 
			printf("Blue\n");
	}
	return 0;
}
