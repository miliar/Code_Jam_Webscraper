#include <stdio.h>
#include <string.h>

int a[128][128];
char s[1024];

inline int abs(int x){
	return x>0?x:-x;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int ttt =1 ; ttt <=T; ttt++){
		memset(a, 0, sizeof(a));
		int K, L;
		scanf("%d", &K);
		gets(s);
		L = 2*K - 1;
		for (int i = 0; i < L; i++){
			int j = 0;
			for (; j <= L; j++){
				int c;
				if ((c = getchar()) == '\n') break;
				if (c>='0' && c <= '9') a[i][j] = c;
			}
		}
		int idist = 1000;
		for (int i = 0; i < L; i++){
			int flag = 1;
			for (int j = 0; j < L; j++){
				for (int k = 0; i-k>=0&&i+k<L; k++){
					if (a[i-k][j]!=a[i+k][j] && a[i-k][j]*a[i+k][j]!=0){
						flag = 0;
						break;
					}
				}
				if (!flag) break;
			}
			if (flag && abs(i-K+1) < idist) idist = abs(i-K+1);
		}
		int jdist = 1000;
		for (int j = 0; j < L; j++){
			int flag = 1;
			for (int i = 0; i < L; i++){
				for (int k = 0; j-k>=0&&j+k<L; k++){
					if (a[i][j-k]!=a[i][j+k] && a[i][j-k]*a[i][j+k]!=0){
						flag = 0;
						break;
					}
				}
				if (!flag) break;
			}
			if (flag && abs(j-K+1) < jdist) jdist = abs(j-K+1);
		}
		int newK = K + idist + jdist;

		printf("Case #%d: %d\n", ttt, newK*newK-K*K);
	}
	return 0;
}