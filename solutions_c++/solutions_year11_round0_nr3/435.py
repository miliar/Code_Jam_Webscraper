#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
int T,N,Sum,Ans,now;
int main(){
	scanf("%d", &T);
	for (int t=1;t<=T;t++){
		Sum=now=0;
		Ans=100000000;
		scanf("%d", &N);
		for (int i=0;i<N;i++){
			int x;
			scanf("%d", &x);
			Sum+=x;
			Ans=min(Ans,x);
			now^=x;
		}
		if (now) printf("Case #%d: NO\n", t);else
		printf("Case #%d: %d\n", t, Sum-Ans);
	}
	return 0;
}
