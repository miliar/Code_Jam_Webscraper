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

const long MaxN = 12;


long dp[MaxN][MaxN][1<<MaxN][2];
bool flag[MaxN][MaxN][1<<MaxN][2];

bool sedi[MaxN][MaxN];

int m, n;
char lajn[MaxN];

FILE *fin, *fout;
	
int setbit(int s, int i, int v){
	if (v == 0){
		if (!(s & (1<<i))) return s;
		else return s ^ (1<<i);
	}
	else{
		if (s & (1<<i)) return s;
		else return s | (1<<i);
	}
}	

int memoiz(int i, int j, int s, int is1){
	if (i == m) return 0;
	else if (flag[i][j][s][is1]) return dp[i][j][s][is1];
	else{
		int best = 0;
		
		// preskachemo
		if (j == n - 1) best = memoiz(i + 1, 0, setbit(s, j, is1), 0);
		else best = memoiz(i, j + 1, setbit(s, j, is1), 0);
		
		// postavljamo
		if (sedi[i][j] && (!(s & (1<<j)))){
			int ns = setbit(s, j, is1);
			is1 = 0;
			
			// dole levo
			if (i < m - 1 && j > 0){
				ns = setbit(ns, j - 1, 1);
			}
				
			// dole desno
			if (i < m - 1 && j < n - 1){
				is1 = 1;
			}
				
			// desno
			if (j < n - 1){
				ns = setbit(ns, j + 1, 1);
			}
			
			if (j == n - 1) best >?= 1 + memoiz(i + 1, 0, ns, is1);
			else best >?= 1 + memoiz(i, j + 1, ns, is1);
		}
		
		flag[i][j][s][is1] = true;
		dp[i][j][s][is1] = best;
		
		return best;
	}
}

void solve(int tt){
	SET(flag, 0);
	int res = memoiz(0, 0, 0, 0);
	fprintf(fout, "Case #%d: %d\n", tt, res);
}

int main(){
	fin = fopen("C_small.in", "r");
	fout = fopen("C_small.out", "w");
	
	int test;
	fscanf(fin, "%d", &test);
	for (int tt = 1; tt <= test; tt++){
		fscanf(fin, "%d %d\n", &m, &n);
		for (int i = 0; i < m; i++){
			fgets(lajn, MaxN, fin);
			for (int j = 0; j < n; j++){
				sedi[i][j] = (lajn[j] == '.');
			}
		}
		
		solve(tt);
	}

	fclose(fin); fclose(fout);
	return 0;
}

