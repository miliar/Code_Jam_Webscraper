#include <stdio.h>

char mat[50][50];

int countK(char key, int N){
	int ret = 0;
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			if (mat[i][j] != key) continue;
			int n = 1;
			for (int k = j - 1; k >= 0; k--){
				if (mat[i][k] == key) n++;
				else break;
			}
			for (int k = j + 1; k < N; k++){
				if (mat[i][k] == key) n++;
				else break;
			}
			if (n > ret) ret = n;

			n = 1;
			for (int k = i - 1; k >= 0; k--){
				if (mat[k][j] == key) n++;
				else break;
			}
			for (int k = i + 1; k < N; k++){
				if (mat[k][j] == key) n++;
				else break;
			}
			if (n > ret) ret = n;

			n = 1;
			for (int k = 1; i-k>=0 && j-k>=0; k++){
				if (mat[i - k][j - k] == key) n++;
				else break;
			}
			for (int k = 1; i+k<N && j+k<N; k++){
				if (mat[i+k][j+k] == key) n++;
				else break;
			}
			if (n > ret) ret = n;

			n = 1;
			for (int k = 1; i+k<N && j-k>=0; k++){
				if (mat[i+k][j-k] == key) n++;
				else break;
			}
			for (int k = 1; i-k>=0 && j+k < N; k++){
				if (mat[i-k][j+k] == key) n++;
				else break;
			}
			if (n > ret) ret = n;
		}
	}
	return ret;
}

int main(){
	int T;
	scanf("%d", &T);
	char ts[100];
	for (int ttt = 1; ttt <= T; ttt++){
		int N, K;
		scanf("%d%d", &N, &K);
		gets(ts);
		for (int i = N-1; i >= 0; i--){
			for (int j = 0; j < N; j++){
				mat[j][i] = getchar();
			}
			gets(ts);
		}
		for (int j = 0; j < N; j++){
			while (1){
				int i;
				for (i = N - 1; i >= 0; i--){
					if (mat[i][j] == '.') break;
				}
				if (i < 0) break;
				int p = i - 1;
				for (; p >= 0; p--){
					if (mat[p][j] != '.') break;
				}
				if (p < 0) break;
				mat[i][j] = mat[p][j];
				mat[p][j] = '.';
			}
		}
		int RK = countK('R', N);
		int BK = countK('B', N);
		char *s;
		if (RK >= K){
			if (BK >= K) s= "Both";
			else s = "Red";
		}else if (BK>=K) s = "Blue";
		else s = "Neither";
		printf("Case #%d: %s\n", ttt, s);
	}
	return 0;
}