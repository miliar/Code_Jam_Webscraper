#include<algorithm>
#include<string>
#include<cstdio>
#include<algorithm>

using namespace std;

int testcases, A, N, M;

bool FindSolution;

	FILE *fin = fopen("B-small-attempt0.in", "r");
	
	FILE *fout = fopen("B-small-attempt0.out", "w");


bool inRange(int x, int M) {
	
	if (x >= 0 && x <= M) return true; else return false;
}

void check(int cases, int A, int xa, int ya, int xb) {
	
	                if (FindSolution) return;

					int tmp = A + xb * ya;
					
					if (xa > 0 && tmp % xa != 0) return;
					
					if (xa == 0 && tmp != 0) return;
					
					int yb;

                    if (xa > 0) yb = tmp / xa; else yb = 0;
					
					int x1 = 0;
					
					int y1 = 0;
					
					if (ya < 0) y1 = -ya;
					
					if (yb < 0 && -yb > y1) y1 = -yb;
					
					int x2 = x1 + xa;
					
					int y2 = y1 + ya;
					
					int x3 = x1 + xb;
					
					int y3 = y1 + yb;
					
					if (inRange(x1, N) && inRange(x2, N) && inRange(x3, N) && inRange(y1, M) && inRange(y2, M)
						
						&& inRange(y3, M)) {
							
							FindSolution = true;
							
							fprintf(fout, "Case #%d: %d %d %d %d %d %d\n", cases,x1, y1, x2, y2, x3, y3);
						}

}

int main() {
	
	
	fscanf(fin, "%d", &testcases);
	
	for (int cases = 1; cases <= testcases; cases++) {
		
		fscanf(fin, "%d %d %d", &N, &M, &A);
		
		FindSolution = false;
		
		for (int xa = 0; xa <= N; xa++) if (!FindSolution)
			
			for (int xb = 0; xb <= N; xb++) if (!FindSolution)
				
				for (int ya = -M; ya <= M; ya++) if (!FindSolution) {
					
					check(cases,A, xa, ya, xb);
					
					check(cases, -A, xa, ya, xb);
				}
		
		if (!FindSolution) fprintf(fout, "Case #%d: IMPOSSIBLE\n", cases);
	}
    
	return 0;
}
