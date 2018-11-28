#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

int n, res, x, S, X, M;

void single_case(int caseID) {
	S = 0, X = 0, M = 1000000000;
	scanf("%d",&n);
	for(int i = 0 ; i < n ; i++) {
		scanf("%d",&x);
		S += x;
		X ^= x;
		M = min(M,x);
	}
	if ( X )
		printf("Case #%d: NO\n",caseID);
	else
		printf("Case #%d: %d\n",caseID,S-M);
}

int main() {
	int z;
	scanf("%d",&z);
	for(int i = 1 ; i <= z ; i++) {
		single_case(i);
	}
}
