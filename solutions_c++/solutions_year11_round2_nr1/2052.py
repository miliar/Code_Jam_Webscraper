#include <cstdio>
using namespace std; 
const int maxn = 105; 
int win[maxn];
int con[maxn];
int match[maxn][maxn];
int N, T;
double owp[maxn];
double oowp[maxn];
//double rpi[maxn];
int main(){
	//freopen("D:\\input\\a.in", "r", stdin); 
	//freopen("D:\\input\\a.out", "w", stdout); 
	scanf("%ld", &T); 
	for (int cnt = 1; cnt <= T; cnt ++) {
		// input the graph 
		scanf("%ld", &N); 
		char c; 
		for (int i = 0; i < N; i++) {
			con[i] = win[i] = 0; 
			for (int j = 0; j < N; j++) {
				scanf(" %c", &c); 
				//printf("%c",c); 
				if (c == '.') match[i][j] = 0; 
				else {
					con[i] ++; 
					if (c == '1') {
						match[i][j] = 1; 
						win[i]++; 
					} else match[i][j] = -1; 
				}
			}
		}
		printf("Case #%ld:\n", cnt);
		for (int i = 0; i < N; i++) {
			double sum = 0; 
			int a, b; 
			for (int j = 0; j < N; j++) {
				if (j == i) continue; 
				a = (match[j][i] == 1);
				if (match[j][i] != 0) sum += (win[j] - a) * 1.0 / (con[j] - 1);
			}
			owp[i] = sum / con[i];
		}
		//for (int i = 0; i < N ;i++) printf("%.3lf\t", owp[i]); 
		//printf("\n");
		for (int i = 0; i < N; i++) {
			double sum = 0; 
			for (int j = 0; j < N; j++) 
				if (match[i][j] != 0) {
					sum += owp[j];
				}
			oowp[i] = sum / con[i];
		}
		
		for (int i = 0; i < N; i++) {
			// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
			double rpi = 0.25 * win[i] / con[i] + 0.5 * owp[i] + 0.25 * oowp[i]; 
			printf("%.12lf\n", rpi);
		}
	}
	//fclose(stdout); 
}