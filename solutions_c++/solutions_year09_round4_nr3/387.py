#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int nTC;
int hasil, N;
vector <int> M[50];
vector <int> daftar;
int dp [1 << 17];
int K;

int f (int bm) {
	if (bm == 0) return 0;
	
	int &ret = dp[bm];
	
	if (ret != -1) return ret;
	
	ret = 1000000;
	
	for (int i = 0; i < daftar.size(); i++) {
		int tmp = bm;
		for (int j = 0; j < N; j++) {
			if ((tmp & (1 << j)) > 0 && (daftar[i] & (1 << j)) > 0) {
				tmp ^= (1 << j);
			}
		}
		ret = min (ret, f(tmp) + 1);
	}
	
	return ret;
}

int main() {
	scanf ("%d", &nTC);
	
	for (int tc = 1; tc <= nTC; tc++) {
		memset (dp, -1, sizeof (dp));
		scanf ("%d%d", &N, &K);
		
		for (int i = 0; i < N; i++) {
			M[i].clear();
			for (int j = 0; j < K; j++) {
				int x;
				scanf ("%d", &x);
				M[i].push_back (x);
			}
		}
		
		sort (M, M + N);
		
		daftar.clear();
		for (int i = 0; i < (1 << N); i++) {
			bool flag = true;
			for (int k = 0; k < K; k++) {
				int bef = -1;
				for (int j = 0; j < N; j++) {
					if (i & (1 << j)) {
						if (M[j][k] <= bef) {
							flag = false;
							break;
						}
						bef = M[j][k];
					}
				}
				
				if (!flag) break;
			}
			
			if (flag) {
				daftar.push_back (i);
			}
		}
		
		for (int i = 0; i < daftar.size(); i++) {
			for (int j = i + 1; j < daftar.size(); j++) {
				if ((daftar[j] | daftar[i]) == daftar[j]) {
					daftar[i] = -1;
					break;
				}
			}
		}
		
		for (int i = 0; i < daftar.size(); i++) {
			if (daftar[i] == -1) {
				swap (daftar[i], daftar[daftar.size() - 1]);
				daftar.pop_back();
				i--;
			}
		}
		
		/*
		for (int i = 0; i < daftar.size(); i++) {
			cout << daftar[i] << endl;
		}*/
		
		hasil = f((1 << N) - 1);
		
		printf ("Case #%d: %d\n", tc, hasil);
	}
	
	return 0;
}
