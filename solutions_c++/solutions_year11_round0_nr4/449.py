#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int A[1000 + 10];
int B[1000 + 10];
int n;

int main(){
	int T;
	scanf("%d",&T);
	for(int i = 1;i<=T;i++){
		double ans = 0.0;
		scanf("%d",&n);
		for(int j=0;j<n;j++){
			scanf("%d",&A[j]);
			B[j] = A[j];
		}
		sort(B,B + n);
		for(int j=0;j<n;j++){
			ans += (lower_bound(B,B + n,A[j]) - B)!=j;
		}
		printf("Case #%d: ",i);
		printf("%.6lf\n",ans);
	}
	return 0;
}
