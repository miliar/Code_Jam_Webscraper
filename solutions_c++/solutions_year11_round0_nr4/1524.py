#include <iostream>
#include <cstdio>

using namespace std;

int solve(){
	int ans = 0,N;
	scanf("%d",&N);
	for (int i=1;i<=N;i++){
		int w;
		scanf("%d",&w);
		if (w!=i) ++ans;
	}
	return ans;
}

int main(){
	int testcase;
	scanf("%d",&testcase);
	for (int i=1;i<=testcase;i++)
		printf("Case #%d: %d.00000000\n",i,solve());
		
	return 0;
}