#include <iostream>
using namespace std;

int win[110];
int mat[110][110];
double owp[110];
double oowp[110];
double wp[110];
int tanding[110];

int main() {
	int ntc;
	char dumi;
	
	scanf("%d", &ntc);
	
	for (int tc = 1; tc <= ntc; ++tc) {
		int n;
		
		scanf("%d%c", &n, &dumi);
		for (int i = 0;i < n; ++i){
			win[i] = 0;
			tanding[i] = n;
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			for (int j = 0; j < n; ++j){
				mat[i][j] = -1;
			}
		}
		char temp;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				scanf("%c", &temp);
				if (temp == '0')
					mat[i][j] = 0;
				else if (temp == '1') {
					mat[i][j] = 1;
					++win[i];
				} else {
					--tanding[i];
				}
			}
			
			scanf("%c", &dumi);
		}
		
		for (int i = 0; i < n; ++i) {
			wp[i] = win[i] / (double)tanding[i];
			
			double top = 0;
			for (int j = 0; j < n; ++j) {
				if (j == i) continue;
				
				if (mat[i][j] == -1) continue;
				
				if (mat[j][i]) 
					top += (win[j] - 1) / (double) (tanding[j] - 1);
				else
					top += win[j] / (double) (tanding[j] - 1);
			}
			
			owp[i] = top / (double)tanding[i];
		}
		
		for (int i = 0; i < n; ++i){
			double top = 0;
			for (int j = 0; j < n; ++j) {
				if (j == i) continue;
				if (mat[i][j] == -1) continue;
				
				oowp[i] += owp[j];
			}
			
			oowp[i] = oowp[i] / (double)tanding[i];
		}
		
		printf("Case #%d:\n", tc);
		for (int i = 0; i < n; ++i) {
			cout << wp[i] * 0.25f + owp[i] * 0.5f + oowp[i] * 0.25f << endl;
		}
	}
 	return 0;
}
