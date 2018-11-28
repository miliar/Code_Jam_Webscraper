#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

const int inf = 1000000; 

int M;
bool O[11000], S[11000], C[11000];
int SOL[11000][2];


void go(int k) {
	if(k <= (M - 1) / 2) {
		go(2 * k);
		go(2 * k + 1);
		if(O[k])
			S[k] = S[2 * k] & S[2 * k + 1];
		else
			S[k] = S[2 * k] | S[2 * k + 1];
	}
}

int solve(int n, bool s) {
	if(SOL[n][s] == -1) {
		SOL[n][s] = inf;
		if(S[n] == s)
			SOL[n][s] = 0;
		else {
			if(n <= (M - 1) / 2) {
				int t = solve(2 * n, false);
				t = solve(2 * n + 1, false);
				t = solve(2 * n, true);
				t = solve(2 * n + 1, true);
				if(s) {
					if(O[n]) {
						SOL[n][s] <?= SOL[2 * n][1] + SOL[2 * n + 1][1];
						if(C[n])
							SOL[n][s] <?= (SOL[2 * n][1] <? SOL[2 * n + 1][1]) + 1;
					}
					else {
						SOL[n][s] <?= (SOL[2 * n][1] <? SOL[2 * n + 1][1]);
						if(C[n])
								SOL[n][s] <?= SOL[2 * n][1] + SOL[2 * n + 1][1] + 1;
					}
				}
				else {
					if(O[n]) {
						SOL[n][s] <?= (SOL[2 * n][0] <? SOL[2 * n + 1][0]);
						if(C[n])
							SOL[n][s] <?= SOL[2 * n][0] + SOL[2 * n + 1][0] + 1;
					}
					else {
						SOL[n][s] <?= SOL[2 * n][0] + SOL[2 * n + 1][0];
						if(C[n])
								SOL[n][s] <?= (SOL[2 * n][0] <? SOL[2 * n + 1][0]) + 1;
					}
			
			
			
				}
			}	
		}
	}
	return SOL[n][s];
}


int main() {
	FILE *fin = fopen("a.in", "r");
	int N;
	fscanf(fin, "%d", &N);
	FILE *fout = fopen("a.out", "w");
	for(int i = 0; i < N; i++) {
		int V;
		fscanf(fin, "%d %d", &M, &V);
		for(int j = 1; j <= (M - 1) / 2; j++) {
			int g, c;
			fscanf(fin, "%d %d", &g, &c);
			O[j] = (g == 1);
			C[j] = (c == 1);
		}
		for(int j = (M - 1) / 2 + 1; j <= M; j++) {
			int s;
			fscanf(fin, "%d", &s);
			S[j] = (s == 1);
		}
		go(1);
		//cout << S[1] << " " << V << endl;
		for(int j = 1; j <= M; j++)
			for(int k = 0; k < 2; k++)
				SOL[j][k] = -1;
		int s = solve(1, V);
		if(s >= inf)
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", i + 1);
		else
			fprintf(fout, "Case #%d: %d\n", i + 1, s);
	}
	//system("pause");
	return 0;
}
