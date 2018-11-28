#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

int x[501][501];
int R, C;
long D;
long long acc_r[501][501];
long long acc_c[501][501];
long long acc[501][501];

char line[510];

int ok(int r, int c, int K){

	double Y = r + double(K - 1) / 2.;
	double X = c + double(K - 1) / 2.;

	long long t = acc[r + K][c + K] - acc[r][c + K] - acc[r + K][c] + acc[r][c] - (long long)(1) * (x[r + K - 1][c] + x[r + K - 1][c + K - 1]) - (long long)(1) * (x[r][c] + x[r][c + K - 1]);

	long long rt = acc_r[r + K][c + K] - acc_r[r][c + K] - acc_r[r + K][c] + acc_r[r][c] - (long long)(r + K - 1) * (x[r + K - 1][c] + x[r + K - 1][c + K - 1]) - (long long)(r) * (x[r][c] + x[r][c + K - 1]);

	long long ct = acc_c[r + K][c + K] - acc_c[r][c + K] - acc_c[r + K][c] + acc_c[r][c] - (long long)(c + K - 1) * (x[r + K - 1][c + K - 1] + x[r][c + K - 1]) - (long long)(c) * (x[r][c] + x[r + K - 1][c]);


	if(Y * double(t) != double(rt))	return 0;
	if(X * double(t) != double(ct))	return 0;

	return 1;

}

int main()
{

	int ncase;
	scanf("%d", &ncase);

	for(int caseidx = 1; caseidx <= ncase; caseidx++){

		scanf("%d %d %ld", &R, &C, &D);

		for(int i = 0; i < R; i++){

			scanf("%s", line);
			for(int j = 0; j < C; j++){
				//char c;
				//scanf("%c", &c);
				x[i][j] = line[j] - '0';
			}
		}


		memset(acc_r, 0, sizeof(acc_r));
		memset(acc_c, 0, sizeof(acc_c));
		memset(acc, 0, sizeof(acc));

		for(int i = 1; i <= R; i++){

			long long tmp_r = 0;
			long long tmp_c = 0;
			long long tmp = 0;

			for(int j = 1; j <= C; j++){

				tmp_r += ((long long)(i - 1) * (long long)(x[i - 1][j - 1]));
				tmp_c += ((long long)(j - 1) * (long long)(x[i - 1][j - 1]));
				tmp += (long long)(x[i - 1][j - 1]);

				acc_r[i][j] = acc_r[i - 1][j] + tmp_r;
				acc_c[i][j] = acc_c[i - 1][j] + tmp_c;
				acc[i][j] = acc[i - 1][j] + tmp;


			}
		}

		int K = MIN(R, C);
		int k;
		for(k = K; k >= 3; k--){

			for(int i = 0; i <= R - k; i++){
				for(int j = 0; j <= C - k; j++){

					if(ok(i, j, k))	goto done;
				}
			}
		}

done:
		printf("Case #%d: ", caseidx);
		if(k >= 3)	printf("%d", k);
		else	printf("IMPOSSIBLE");
		printf("\n");
	}
	
	return 0;
}

// vi: ts=2 sw=2
