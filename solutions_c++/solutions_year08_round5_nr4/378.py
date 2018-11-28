#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
using namespace std;

// FEW defines

#define sqr(a) ((a)*(a))
#define FOR(i,n) for (long (i)=0; (i)<(n); (i)++)
#define pb push_back
#define mp make_pair
#define SET(a,k) memset((a),(k),sizeof((a)))
 
typedef long long ll;
// ------------

const int MaxN = 101;
const long MOD = 10007;

bool flag[MaxN][MaxN];
long dp[MaxN][MaxN];

bool moze[MaxN][MaxN];

int w, h, r;

FILE *fin, *fout;

long memoiz(int i, int j){
	if (i == w - 1 && j == h - 1) return 1;
	else if (flag[i][j]) return dp[i][j];
	else{
		long ukupno = 0;
		
		// dole
		if (i + 2 < w && j + 1 < h && moze[i+2][j+1]) ukupno += memoiz(i + 2, j + 1);
		
		// desno
		if (i + 1 < w && j + 2 < h && moze[i+1][j+2]) ukupno += memoiz(i + 1, j + 2);
		
		ukupno %= MOD;
		
		flag[i][j] = true;
		dp[i][j] = ukupno;
		return ukupno;
	}
}

void solve(int tt){
	SET(flag, 0);
	long res = memoiz(0, 0);
	fprintf(fout, "Case #%d: %ld\n", tt, res);
}

int main(){
	fin = fopen("D_small.in", "r");
	fout = fopen("D_small.out", "w");
	
	int test;
	fscanf(fin, "%d", &test);
	for (int tt = 1; tt <= test; tt++){
		FOR(i, MaxN) FOR(j, MaxN) moze[i][j] = true;
		
		fscanf(fin, "%d %d %d", &w, &h, &r);
		FOR(i, r){
			int x1, y1;
			fscanf(fin, "%d %d", &x1, &y1);
			moze[x1 - 1][y1 - 1] = false;
		}
		
		solve(tt);
	}

	fclose(fin); fclose(fout);
	return 0;
}

