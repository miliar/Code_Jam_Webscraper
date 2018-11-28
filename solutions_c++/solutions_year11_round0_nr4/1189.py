#include<cstdio>
#include<iostream>

using namespace std;

int n,A[1010];

double solve() {
	double rpta=0;
	for(int i=0;i<n;i++)
		rpta+=(A[i]!=i+1);
	return rpta;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++) {
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&A[i]);
		printf("Case #%d: %.6lf\n",caso,solve());
	}
}
