#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

void ans(int cnt, int ch){
	printf("Case #%d: %s\n", cnt, (ch?"ON":"OFF"));
}

int main(){
	int T, N, K, cnt=0;
	scanf("%d", &T);
	while(T--){
		cnt++;
		scanf("%d %d", &N, &K);
		long int p=1;
		while(N--){p=p<<1;}
		//cout<<p<<endl;
		//case 1
		if (K < p-1) {ans(cnt, 0);continue;}
		if (K == p-1){ans(cnt, 1);continue;}
		K -= p - 1;
		if (K%p == 0){ans(cnt, 1);}else{ans(cnt, 0);}
	}
	return 1;
}
