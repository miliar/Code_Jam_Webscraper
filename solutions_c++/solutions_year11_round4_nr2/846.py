#include <cstdio>
#include <vector>
#include <algorithm>
//#include <map>
//#include <set>

#define FOR(i,s,e) for (int i=(s);i<(e);i++)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define PB push_back

using namespace std;

int map[600][600];
int sum[600][600];
char line[1000];
int R,C,D;

int getsum(int a, int b) {
	if (a<0 || b<0) return 0;
	return sum[a][b];
}

bool sprawdz23(int a, int b, int k) {	
	int k2 = k/2;
	if (k%2 == 0) {
		if (a-k2 < -1 || b-k2 < -1 || a+k2 >= R || b+k2 >= C) return false;
		int g = getsum(a,b+k2) - getsum(a-k2,b+k2) - getsum(a,b-k2) + getsum(a-k2,b-k2) - map[a-k2+1][b-k2+1] - map[a-k2+1][b+k2-1];
		int d = getsum(a+k2,b+k2) - getsum(a,b+k2) - getsum(a+k2,b-k2) + getsum(a,b-k2) - map[a+k2][b-k2+1] - map[a+k2][b+k2-1];
		int l = getsum(a+k2,b) - getsum(a-k2,b) - getsum(a+k2,b-k2) + getsum(a-k2,b-k2) - map[a-k2+1][b-k2+1] - map[a+k2-1][b-k2+1];
		int r = getsum(a+k2,b+k2) - getsum(a-k2,b+k2) - getsum(a+k2,b) + getsum(a-k2,b) - map[a-k2+1][b+k2-1] - map[a+k2-1][b+k2-1];
		if (g == d && l == r) return true;
	}
	else {
		if (a-k2 < 0 || a+k2>=R || b-k2 , 0 || b+k2>=C) return false;
		int g = getsum(a-1,b+k2) - getsum(a-k2-1,b+k2) - getsum(a-1,b-k2-1) + getsum(a-k2-1,b-k2-1) - map[a-k2][b-k2] - map[a-k2][b+k2];
		int d = getsum(a+k2,b+k2) - getsum(a,b+k2) - getsum(a-k2-1,b+k2) + getsum(a,b-k2-1) -map[a+k2][b-k2] - map[a+k2][b+k2];
		int l = getsum(a+k2,b-1) - getsum(a-k2-1,b-1) - getsum(a+k2,b-k2-1) + getsum(a-k2-1,b-k2-1) - map[a-k2][b-k2] - map[a+k2][b-k2];
		int r = getsum(a+k2,b+k2) - getsum(a+k2,b) - getsum(a-k2-1,b+k2) + getsum(a-k2-1,b) - map[a-k2][b+k2] - map[a+k2][b+k2];
		if (g == d && l == r) return true;
	}
	return false;
}

bool sprawdz(int a, int b, int k) {
//if (k==5 && a==1 && b==1) printf("SZAKA\n");
	if (a+k > C || b+k > R) return false;
	int k2 = k/2;
	if (k%2 == 0) {
		int g = getsum(a+k2-1,b+k-1) - getsum(a-1,b+k-1) - getsum(a+k2-1,b-1) + getsum(a-1,b-1) - map[a][b] - map[a][b+k-1];
		int d = getsum(a+k-1,b+k-1) - getsum(a+k2-1,b+k-1) - getsum(a+k-1,b-1) + getsum(a+k2-1,b-1) - map[a+k-1][b+k-1] - map[a+k-1][b];
		int l = getsum(a+k-1,b+k2-1) - getsum(a-1,b+k2-1) - getsum(a+k-1,b-1) + getsum(a-1,b-1) - map[a][b] - map[a+k-1][b];
		int r = getsum(a+k-1,b+k-1) - getsum(a-1,b+k-1) - getsum(a+k-1,b+k2-1) + getsum(a-1,b+k2-1) - map[a][b+k-1] - map[a+k-1][b+k-1];
		if (g == d && l == r) return true;
	}
	else {
		int g = getsum(a+k2-1,b+k-1) - getsum(a-1,b+k-1) - getsum(a+k2-1,b-1) + getsum(a-1,b-1) - map[a][b] - map[a][b+k-1];
		int d = getsum(a+k-1,b+k-1) - getsum(a+k2,b+k-1) - getsum(a+k-1,b-1) + getsum(a+k2,b-1) - map[a+k-1][b+k-1] - map[a+k-1][b];
		int l = getsum(a+k-1,b+k2-1) - getsum(a-1,b+k2-1) - getsum(a+k-1,b-1) + getsum(a-1,b-1) - map[a][b] - map[a+k-1][b];
		int r = getsum(a+k-1,b+k-1) - getsum(a-1,b+k-1) - getsum(a+k-1,b+k2) + getsum(a-1,b+k2) - map[a][b+k-1] - map[a+k-1][b+k-1];
//		if (k==5 && a==1 && b==1) printf("%d %d %d %d\n", g,d,l,r);
		if (g == d && l == r) return true;
	}
	return false;
	
}

void test() {
	scanf("%d%d%d", &R, &C, &D);
	REP(i,R) {
		scanf("%s", line);
		int lin = 0;
		REP(j,C) {
			map[i][j] = line[j] - '0';
			lin += map[i][j];
			sum[i][j] = lin;
			if (i > 0) sum[i][j] += sum[i-1][j];
		}
	}
	int gg = min(R,C);
	int res = -1;
	REP(i,R) {
		REP(j,C) {
			FOR(k,3,gg+1) {
				if (sprawdz(i,j,k)) res = max(res,k);
			}
		}
	}
	if (res < 0) printf(" IMPOSSIBLE\n");
	else printf(" %d\n", res);
}

main() {
	int t; scanf("%d", &t);
	REP(i,t) { printf("Case #%d:", i+1); test(); }
}

