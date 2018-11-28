#include <iostream>
#include <cmath>
#include <algorithm>
const int MaxN=10000;

using namespace std;
int T,Ans,N;
int main(){
	scanf("%d", &T);
	for (int t=1;t<=T;t++){
		scanf("%d", &N);
		int x;
		Ans=0;
		for (int i=1;i<=N;i++){
			scanf("%d", &x);
			if (x!=i) Ans++;
		}
		printf("Case #%d: %d.000000\n", t, Ans);
	}
	return 0;
}
