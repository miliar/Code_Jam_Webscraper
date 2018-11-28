#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXN 60

char s[MAXN][MAXN];
int N,K;

void rotate() {
	char tmp[MAXN][MAXN];
	int i,j;
	rep(i,N) rep(j,N) tmp[j][N-1-i] = s[i][j];
	rep(i,N) rep(j,N) s[i][j] = tmp[i][j];
}

void gravity() {
	int i,j,k;
	char tmp[MAXN][MAXN];
	rep(i,N) rep(j,N) tmp[i][j] = '.';
	rep(j,N) {
		k = N - 1;
		for(i = N-1; i>= 0; i--) {
			if(s[i][j] != '.') tmp[k--][j] = s[i][j];
		}
	}
	rep(i,N) rep(j,N) s[i][j] = tmp[i][j];
}

int count(int x, int y, int dx, int dy) {
	int ct = 0;
	int i,j;
	for(i = x, j = y; i < N && i >= 0 && j < N && j >= 0; i += dx, j += dy) {
		if(s[i][j] == s[x][y]) ct++;
		else break;
	}
	return ct;
}

string find_res() {
	int i,j,ct;
	bool fb, fr;
	fb = fr = false;
	rep(i,N) rep(j,N) if(s[i][j] != '.') {
		ct = count(i,j,0,1);
		if(ct >= K) {
			if(s[i][j] == 'B') fb = true;
			else fr = true;
		}

		ct = count(i,j,1,0);
		if(ct >= K) {
			if(s[i][j] == 'B') fb = true;
			else fr = true;
		}

		ct = count(i,j,1,1);
		if(ct >= K) {
			if(s[i][j] == 'B') fb = true;
			else fr = true;
		}

		ct = count(i,j,1,-1);
		if(ct >= K) {
			if(s[i][j] == 'B') fb = true;
			else fr = true;
		}
	}
	if(fb && fr) return "Both";
	if(fb) return "Blue";
	if(fr) return "Red";
	return "Neither";
}

int main() {
	int i,T;
	int kase = 1;
	scanf("%d",&T);
	while(T--) {
		scanf(" %d %d",&N,&K);
		rep(i,N) scanf(" %s",s[i]);
		printf("Case #%d: ",kase++);
		rotate();
		gravity();
		printf("%s\n",find_res().c_str());
	}
	return 0;
}