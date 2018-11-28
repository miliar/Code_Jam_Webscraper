#include <stdio.h>
#define FOR(A, B) for(A = 0; A < B; A++)

int main()
{
	int T, z;
	scanf("%d", &T);
	FOR(z, T) {
		printf("Case #%d:\n", z+1);
		int N, i, j, k;
		int table[101][101];
		double wps[101], owps[101];
		scanf("%d\n", &N);
		FOR(i, N) {
			char c;
			FOR(j, N) { scanf("%c", &c); if(c == '.') table[i][j] = -1; if(c == '1') table[i][j] = 1; if(c == '0') table[i][j] = 0;}
			scanf("\n");
		}
	//	FOR(i, N) { FOR(j, N) printf("%d ", table[i][j]); printf("\n");}
		FOR(i, N) {
			double wp;
			int a = 0, b = 0;
			FOR(j, N) { if(i == j) continue; if(table[i][j] == 0 || table[i][j] == 1) b++; if(table[i][j] == 1) a++; }
			wp = ((double)a)/b;
			wps[i] = wp;	
		}
		
		
		FOR(i, N) {
			double sum = 0;
			int count = 0;
			FOR(j, N) { 
				if(table[i][j] != -1) {
					int a = 0, b = 0;
					FOR(k, N) { 
						if(i == k) continue;
						if(table[j][k] == 0 || table[j][k] == 1) b++;
						if(table[j][k] == 1) a++;
					}
					count++;
					sum += ((double)a)/b;
				}				
			}
			owps[i] = sum/count;
		}
		FOR(i, N) {
			double sum = 0; int count = 0;
			FOR(j, N) {if(table[i][j] != -1) { count++; sum += owps[j]; } }
			double ans = 0.25*wps[i]+0.5*owps[i]+0.25*(sum/count);
			printf("%.12lf\n", ans);
		}
	}	
	return 0;
}
