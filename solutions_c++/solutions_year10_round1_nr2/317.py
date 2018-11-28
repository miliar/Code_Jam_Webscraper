#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <queue> 
#include <cstring> 
using namespace std;
int DP[101][256], N, M, D, I;
int F[101];

int cal(int p, int v){
	if (DP[p][v] != -1) return DP[p][v];
	if (p < 0) return 0;
	if (p == 0) return min(abs(F[p]-v), I+D);
	int ret = 1<<29;
	int Dcost = 0;
	for (int  k = p-1; k >= 0; --k){
		for (int i = 0 ; i < 256; ++i){
			int diff = abs(v-i);
			int Icost = 0;
			if (M){
				if (diff/M > 0) Icost = I * (diff/M - (diff%M == 0));
			}else if (diff) continue;
			//Icost = I * (max(0, abs(v-i)-1));
			//printf("%d-%d cost %d\n", v, i, Icost);
			int ort = ret;
			ret = min(ret, Dcost + abs(v-F[p]) + Icost +  cal(k, i));
			/*
			if (ort != ret){
				printf("%d %d --> %d %d %d\n", p, v, k, i, ret);
			}*/
		}
		Dcost += D;
	}
	ret = min(ret, Dcost + abs(v-F[p]));
	//printf("%d %d => %d\n", p, v, ret);
	return DP[p][v] = ret;
}

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 0 ; i < N; ++i) scanf("%d", F+i);
		memset(DP, -1, sizeof(DP));
		int res = 1<<29, dd = 0;
		for (int k = N-1; k >= 0; --k){
			for (int i = 0 ; i < 256; ++i)
				res = min(res, dd + cal(k, i));
			dd += D;
		}
		printf("%d\n", res);
	}
	return 0;
}
