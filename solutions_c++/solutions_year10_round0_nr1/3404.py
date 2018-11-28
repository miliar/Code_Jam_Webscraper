#include<iostream>
using namespace std;
int main(){
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout); 
	int T, K, N;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		scanf("%d %d",&N, &K);
		printf("Case #%d: ", i);
		if(K%(1<<N) == ((1<<N)-1)){
			printf("ON\n");
		}
		else{
			printf("OFF\n");
		}
	}
	return 0;
}
