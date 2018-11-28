/**********************************************************************
Author: LiuLixiang
Created Time:  2010/5/22 9:39:39
File Name: \TopCoder\gcj2010\Round1A\B.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;

const int maxint=0x7FFFFFFF;

const int MAXN = 100;

int D, I, M, N, n;
int val[MAXN+10];
int f[MAXN+10][255+5];


void get_input() {
	scanf("%d %d %d %d", &D, &I, &M, &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &val[i]);
	}
	n = N;
}

int dp() {
	if (D == 0) return 0;
	if (M != 0 && I == 0) return 0;
	
	//Insert
	for (int i = 0; i <= 255; i++) {
		f[0][i] = I;
//		cout << f[0][i] << " ";///
	}
	f[0][256] = 0;
//	cout << f[0][256] << endl;///
	
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= 256; j++) {
			f[i][j] = -1;
		}

//		cout << val[i] << " == " << endl;///
		//do nothing
		f[i][ val[i] ] = f[i-1][256];//FIXME
		for (int k = 0; k <= M; k++) {
			int pre = val[i]-k;
			if (pre >= 0) {
				if (f[i-1][pre] < 0) continue;
				if (f[i][ val[i] ] < 0) f[i][ val[i] ] = f[i-1][pre];
				else if (f[i][ val[i] ] > f[i-1][pre]) f[i][ val[i] ] = f[i-1][pre];
			}
		}
		for (int k = 0; k <= M; k++) {
			int pre = val[i]+k;
			if (pre <= 255) {
				if (f[i-1][pre]) continue;
				if (f[i][ val[i] ] < 0) f[i][ val[i] ] = f[i-1][pre];
				else if (f[i][ val[i] ] > f[i-1][pre]) f[i][ val[i] ] = f[i-1][pre];
			}
		}
		
		//change
		for (int j = 0; j <= 255; j++) {
			int cost = j-val[i];
			if (cost < 0) cost = -1 * cost;
			
			if (f[i][j] < 0) f[i][j] = f[i-1][256] + cost;
			else if (f[i][j] > f[i-1][256]+cost) f[i][j] = f[i-1][256]+cost;
			
			for (int k = 0; k <= M; k++) {
				int pre = j-k, tmp;
				if (pre >= 0) {
					if (f[i-1][pre] < 0) continue;
					tmp = f[i-1][pre] + cost;
					if (f[i][j] < 0) f[i][j] = tmp;
					else if (f[i][j] > tmp) f[i][j] = tmp;
				}
			}
			
			for (int k = 0; k <= M; k++) {
				int pre = j-k, tmp;
				pre = j+k;
				if (pre <= 255) {
					if (f[i-1][pre] < 0) continue;
					tmp = f[i-1][pre] + cost;
					if (f[i][j] < 0) f[i][j] = tmp;
					else if (f[i][j] > tmp) f[i][j] = tmp;
				}
			}
		}
		
		//delete
		for (int k = 0; k <= 256; k++) {
			int tmp;
			if (f[i-1][k] >= 0) {
				tmp = f[i-1][k] + D;
				if (f[i][k] < 0) f[i][k] = tmp;
				else if (f[i][k] > tmp) f[i][k] = tmp;
			}
		}
		
		//insert 可以insert多次
		if (M)
		for (int r = 255 / M + 3; r >= 0; r--) {//if M==0 ?
		for (int j = 0; j <= 255; j++) {
			
			if (f[i][j] < 0) f[i][j] = f[i][256] + I;
			else if (f[i][j] > f[i][256]+I) f[i][j] = f[i][256]+I;
			
			for (int k = 0; k <= M; k++) {
				int pre = j-k, tmp;
				if (pre >= 0) {
					if (f[i][pre] < 0) continue;
					tmp = f[i][pre] + I;
					if (f[i][j] < 0) f[i][j] = tmp;
					else if (f[i][j] > tmp) f[i][j] = tmp;
				}
			}
			for (int k = 0; k <= M; k++) {
				int pre = j-k, tmp;
				pre = j+k;
				if (pre <= 255) {
					if (f[i][pre] < 0) continue;
					tmp = f[i][pre] + I;
					if (f[i][j] < 0) f[i][j] = tmp;
					else if (f[i][j] > tmp) f[i][j] = tmp;
				}
			}
		}
		}
		
//		for (int j = 0; j <= 256; j++) {
//			cout << f[i][j] << " "; ///
//		}
//		cout << endl;///
	}
	
	
	int res = -1;
	for (int i = 0; i <= 256; i++) {
		if (res < 0) res = f[n][i];
		else if (res > f[n][i]) res = f[n][i];
	}
	return res;
}

int main() {
	freopen("B_oo.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		get_input();
		printf("Case #%d: %d\n", ca, dp());
	}
	
	fclose(stdout);
    return 0;
}

