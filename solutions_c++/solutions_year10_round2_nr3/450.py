#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <sstream>
#include <cmath>
#include <map>

using namespace std;

#define M(n) ((n)%100003)

int fat[600][600];
int res[600][600];

int S(int n, int k){
	if(res[n][k] != -1) return res[n][k];
	if(n == k+1 || k == 1) return res[n][k] = 1;
	int r = 0;
	for(int p = 1; p < k; p++){
		r = M(r+ M( M(S(k,p)) * fat[n-k-1][k-p-1]));
	}

	return res[n][k] = r;
}

int main(void){
	int T, N;
	cin >> T;
	memset(fat,0,sizeof(fat));
	memset(res,-1,sizeof(res));

	for(int i = 0; i < 600; i++) fat[i][0] = 1;
	for(int i = 1; i < 600; i++){
		for(int j = 1; j <= i; j++){
			fat[i][j] = M(fat[i-1][j] + fat[i-1][j-1]);
		}
	}

	for(int cas = 1; cas <= T; cas++){
		cin >> N;
		int r = 0;
		for(int p = 1; p < N; p++){
			r = M(r + M(S(N,p)));
		}
		printf("Case #%d: %d\n",cas,r);
		/*
		for(int i = 0; i <= N; i++){
				for(int j = 0; j <= N; j++){
					printf("%d ",res[i][j]);
				}
				printf("\n");
			}

			*/
	}


	return 0;


}
