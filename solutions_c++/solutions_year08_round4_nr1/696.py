#include <iostream>
#include <cstdio>
using namespace std;

const long MaxN = 10005;

long n, v;
long dp[MaxN][2];
bool flag[MaxN][2];

int val[MaxN];
bool change[MaxN];
bool andG[MaxN];

FILE *fin, *fout;

long memoiz(long k, int v){
	if (k * 2 > n){
		if (val[k] == v) return 0;
		else return -1;
	}
	else if (flag[k][v]) return dp[k][v];
	else{
		long best = 1000000;

		long p[2], q[2];
		p[1] = memoiz(2 * k, 1), p[0] = memoiz(2 * k, 0);
		q[1] = memoiz(2 * k + 1, 1), q[0] = memoiz(2 * k + 1, 0);
		
		for (int vp = 0; vp <= 1; vp++) for (int vq = 0; vq <= 1; vq++){
			if (p[vp] == -1 || q[vq] == -1) continue;
			
			if (andG[k]){
				if ((vp & vq) == v) best <?= p[vp] + q[vq];
			}
			else{
				if ((vp | vq) == v) best <?= p[vp] + q[vq];
			}
			
			if (change[k]){
				if (!andG[k]){
					if ((vp & vq) == v) best <?= p[vp] + q[vq] + 1;
				}
				else{
					if ((vp | vq) == v) best <?= p[vp] + q[vq] + 1;
				}
			}
		}
				
		if (best == 1000000) best = -1;
		dp[k][v] = best;
		flag[k][v] = true;
		
		return best;
	}
}

void solve(int test){
	memset(flag, 0, sizeof(flag));
	long best = memoiz(1, v);
	fprintf(fout, "Case #%d: ", test);
	if (best == -1) fprintf(fout, "IMPOSSIBLE\n");
	else fprintf(fout, "%ld\n", best);
}


int main(){
	fin = fopen("A_small.in", "r");
	fout = fopen("A_small.out", "w");
	
	int test;
	fscanf(fin, "%d", &test);
	
	for (int tt = 1; tt <= test; tt++){
		fscanf(fin, "%ld %ld", &n, &v);
		long node = 1;
		for (long i = 0; i < (n-1)/2; i++){
			int g,c;
			fscanf(fin, "%d %d", &g, &c);
			
			andG[node] = (g == 1);
			change[node] = (c == 1);
			
			node++;
		}
		for (long i = 0; i < (n+1)/2; i++){
			fscanf(fin, "%d", &val[node]);
			node++;
		}
		solve(tt);
	}
	
	fclose(fin);
	fclose(fout);
	return 0;
}
