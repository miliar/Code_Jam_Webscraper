#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>

using namespace std;

const int maxN = 10000 + 10;

int testcases; 

int M, V;

int G[maxN], C[maxN];

int F[maxN][2];

const int inf = 20000;

void solve(int, int);

int main() {
	
	FILE *fin = fopen("A-large.in", "r");
	
	FILE *fout = fopen("A-large.out", "w");
	
	
	fscanf(fin, "%d", &testcases);
	
	for (int cases = 1; cases <= testcases; cases++) {
		
		fscanf(fin, "%d %d", &M, &V);
		
		for (int i = 1; i <= (M - 1) / 2; i++) fscanf(fin, "%d %d", &G[i], &C[i]);
		
		for (int i = (M -1) / 2 + 1; i <= M; i++) fscanf(fin, "%d", &G[i]);
		
		memset(F, 255, sizeof F);
		
		for (int i = (M - 1) / 2 + 1; i <= M; i++) {
			
			F[i][G[i]] = 0;
            
            F[i][1 - G[i]] = inf;
        }

		solve(1, V);
		
	    if (F[1][V] >= inf) fprintf(fout, "Case #%d: IMPOSSIBLE\n", cases); else fprintf(fout, "Case #%d: %d\n", cases, F[1][V]);
	}
	
	return 0;
}

int value(int type, int a, int b) {
	
	bool x, y;
	
	if (a == 1) x = true; else x = false;

    if (b == 1) y = true; else y = false;

    if (type == 1) return (int) (x && y); else return (int) (x || y);
}


void solve(int id, int v) {
	
	//fprintf(fout, "Enter %d %d\n", id,v );
	
	if (F[id][v] != -1) return;
	
	F[id][v] = inf;
	
	for (int a = 0; a < 2; a++) {
		
		solve(2 * id, a);
		
		for (int b = 0; b < 2; b++) {
			
			solve(2 * id + 1, b);
			
			int tmp = F[2 * id][a] + F[2 * id + 1][b];
			
			if (value(G[id], a, b) == v) 
				
				if (tmp < F[id][v]) F[id][v] = tmp;
			
			if (C[id] && value(1 - G[id], a, b) == v) 
				
				if (tmp + 1 < F[id][v]) F[id][v] = tmp + 1;
		}
	}
	
	if (F[id][v] > inf) F[id][v] = inf;

	//fprintf(fout, "%d %d %d\n", id, v, F[id][v]);
}
