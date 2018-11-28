#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
int L[1005], P[1005];
int A[1005];
bool cmp(int a,int b) {
	if(P[a] != P[b]) return P[a] > P[b];
	return a < b;
}
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N;
		scanf("%d",&N);
		for(int i=0;i<N;++i) scanf("%d",&L[i]);
		for(int i=0;i<N;++i) {
			scanf("%d",&P[i]);
			A[i] = i;
		}
		sort(A,A+N,cmp);
		printf("Case #%d:",cn);
		for(int i=0;i<N;++i) printf(" %d",A[i]);
		printf("\n");
	}
}

