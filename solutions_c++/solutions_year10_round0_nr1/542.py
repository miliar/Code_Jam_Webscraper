#include<cstdio>
#include<algorithm>

using namespace std;

int arr[50];

int main(){
	int X, T, i, N, K;
	bool on;

	//freopen("A-small.in", "r", stdin); freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	
	scanf("%d", &T);

	for(X = 1; X<=T; ++X){
		scanf("%d%d", &N, &K);
		
		
		for( i = 0; i<31; ++i){
			arr[i] = ((K &(1<<i))!=0);
		}

		on = true;
		for( i = 0; i<N; ++i){
			if( arr[i] == 0){
				on = false;
				break;
			}
		}

		printf("Case #%d: ", X);
		if( on ) puts("ON");
		else puts("OFF");


	}
	return 0;

}