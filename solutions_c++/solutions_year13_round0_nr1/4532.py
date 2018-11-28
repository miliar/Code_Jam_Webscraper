#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
int n, m;
char s[10][10];

int check(int x){
	int ok = 1;
	FOR(i,0,4) if (s[i][i] != x && s[i][i] != 'T') ok = 0;
	if (ok) return 1;
	ok = 1;
	FOR(i,0,4) if (s[3 - i][i] != x && s[3 - i][i] != 'T') ok = 0;
	if (ok) return 1;
	FOR(i,0,4){
		ok = 1;
		FOR(j,0,4) if (s[i][j] != x && s[i][j] != 'T') ok = 0;
		if (ok) return 1;
	}
	FOR(j,0,4){
		ok = 1;
		FOR(i,0,4) if (s[i][j] != x && s[i][j] != 'T') ok = 0;
		if (ok) return 1;
	}
	return 0;
}

int comp(){
	FOR(i,0,4) FOR(j,0,4) if (s[i][j] == '.') return 0;
	return 1;
}

char gg[4][40] = {"Game has not completed", "Draw", "X won", "O won"};

int main(){
	int T, ans;
	scanf("%d", &T);
	FOE(cc,1,T){
		FOR(i,0,4) scanf("%s", s[i]);
		if (check('X')) ans = 2;
		else if (check('O')) ans = 3;
		else ans = comp();
		printf("Case #%d: %s\n", cc, gg[ans]);
	}
	return 0;
}
