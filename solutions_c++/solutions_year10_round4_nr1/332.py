#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

const int MaxN = 220;
const int MaxK = 55;
int start[MaxK][MaxN], size[MaxK], col[MaxK][MaxN];

int no;
int K, R;

int T[MaxN][MaxN], O[MaxN][MaxN], rem[MaxN];

int mark[MaxN][MaxN];

int check(int n) {
	for(int x = 0; x + K <= n; ++ x)
		for(int y = 0; y + K <= n; ++ y) {
			bool flag = true;
			for(int i = 0; i < n; ++ i)
				for(int j = 0; j < n; ++ j)
					mark[i][j] = -1;
			for(int i=0;i<K;++i)
				for(int j=0;j<K;++j)
					mark[x+i][y+j] = T[i][j];
			for(int i=0;i<K && flag;++i)
				for(int j=0;j<K && flag;++j) {
					int xx = x + i, yy = y + j;
					int tx = yy, ty = xx;
					if(mark[tx][ty] < 0) mark[tx][ty] = T[i][j];
					else
					if(mark[tx][ty] != T[i][j]) flag = false;
					tx = n - 1 - yy, ty = n - 1 - xx;
					if(mark[tx][ty] < 0) mark[tx][ty] = T[i][j];
					else
					if(mark[tx][ty] != T[i][j]) flag = false;
				}
			if(flag) return true;
		}
	return false;
}

int run() {
	scanf("%d", &K);
	R = size[K];
	if(R == 1) {
		int t; scanf("%d", &t);
		return 0;
	}
	for(int i=0;i<R;++i) {
		rem[i] = col[K][i];
		
	//	cout << "rem[ "<<i<<" ] = "<<col[K][i] << endl;
		
		for(int j = 0; j < col[K][i]; ++ j) 
			scanf("%d", &O[i][j]);
	}
	
	for(int i = 0; i < K; ++ i) {
		for(int x = i; x < i + K; ++ x)
			T[i][x-i] = O[x][--rem[x]];
	}
/*	cout << "O : "<<endl;
	for(int i=0;i<R;++i) {
		for(int j=0;j<col[K][i];++j)
			cout << O[i][j] << " ";
		cout << endl;
	}
	cout << "T : "<<endl;
	for(int i=0;i<K;++i) {
		for(int j=0;j<K;++j)
			cout << T[i][j] << " ";
		cout << endl;
	}
	
	*/
	int res;
	for(res = K; !check(res); ++ res);
	return res * res - K * K;
}

int main() {
	
	for(int k = 1; k < MaxK; ++ k) {
		size[k] = 2 * k - 1;
		for(int det = 0; det < k; ++ det) {
			start[k][k - 1 - det] = 
			start[k][k - 1 + det] = 2 * det;
			col[k][k - 1 + det] = 
			col[k][k - 1 - det] = k - det;
		}
	}
	
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int test; scanf("%d", &test);
	while(test--)printf("Case #%d: %d\n",++no,run());
}
