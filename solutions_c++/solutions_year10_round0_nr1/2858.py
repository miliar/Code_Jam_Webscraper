#include<cstdio>
using namespace std;

int main(){
	int N, K, t;
	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		scanf("%d %d", &N, &K);
		int Mod = 1 << N;
		if(K % Mod == Mod - 1)
			printf("Case #%d: ON\n", i);
		else
			printf("Case #%d: OFF\n", i);	
	}
}
