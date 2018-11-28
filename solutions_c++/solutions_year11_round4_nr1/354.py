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

int B[2000], E[2000], W[2000], L[2000];

int N, S, R, X, T;

int arr[2000];

inline int cmp(int a, int b){
	return W[a] < W[b];
}

double run() {
	scanf("%d %d %d %d %d", &X, &S, &R, &T, &N);
	int tot=X;
	for(int i=1;i<=N;++i) {
		scanf("%d %d %d", B+i, E+i, W+i);
		tot -= (L[i]=E[i] - B[i]);
		arr[i]=i;
	}
	W[0]=0;L[0]=tot;
	arr[0]=0;
	sort(arr,arr+N+1,cmp);
	double now = 0;
	double v = R;
	for(int i=0;i<=N;++i) {
		int k = arr[i];
		double t = L[k]/ (double)(R + W[k]);
		if(t + now <= T) {
			now += t;
			continue;
		}
		double det = T-now;
		now = T + (L[k] - det * (R + W[k])) / (S + W[k]);
		for(int j=i+1;j<=N;++j) {
			int k = arr[j];
			now += L[arr[j]] / (double)(S + W[arr[j]]);
		}
		break;
	}
	return now;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test; scanf("%d", &test);
	for(int no=1;no<=test;++no)
		printf("Case #%d: %.9lf\n", no, run());
}
